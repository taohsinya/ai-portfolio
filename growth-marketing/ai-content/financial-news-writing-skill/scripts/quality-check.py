#!/usr/bin/env python3
"""
Financial News Quality Check v2.0
================================
Synchronized with references/banned-words.md v2.0.
Supports 6 models: A (Wire), B (Macro), C (Industry), D (Mining & Commodities), E (Equity Market), F (Crypto).

Usage:
    python3 quality-check.py "path/to/article.md"
    python3 quality-check.py "path/to/article.md" --model C
    python3 quality-check.py "path/to/article.md" --verbose
    python3 quality-check.py "path/to/article.md" --json
"""

import re
import sys
import argparse
import json
from pathlib import Path

# ─── Banned Words — SYNCED with references/banned-words.md v2.0 ───

TIER1_UNIVERSAL = [
    "delve", "realm", "tapestry", "landscape", "leverage",
    "utilize", "robust", "seamless", "comprehensive", "cutting-edge",
    "holistic", "synergy", "paradigm", "empower", "innovative",
    "transformative", "spearhead", "pivotal",
]

TIER1_HOUSE = [
    "signaling", "positioning",  # as in "positioning the company to"
    "underscores", "underscoring",
    "amplifies", "amplifying",
    "validates", "validation",
    "amid", "amidst",
    "catalyst",  # name the specific event instead
    "sparked", "sparks",
    "bolsters", "bolstering",
    "poised",
]

TIER2_PHRASES = [
    "it's important to note",
    "in today's",
    "let's dive", "let's delve",
    "without further ado",
    "in this article, we will",
    "it's worth mentioning",
    "it goes without saying",
    "as we all know",
    "to be fair", "to be honest",
    "at the end of the day",
    "when it comes to",
    "in terms of",
    "with respect to",
    "this is a game-changer",
    "and that's a good thing",
    "here's the thing",
    "moving forward", "going forward",
    "at this point in time",
    "due to the fact that",
    "in order to",
    "in the wake of", "on the heels of",
    "in a world where", "in an era of",
    "sends a clear message",
    "positioning the company to",
    "this development underscores",
    "signaling", "to the market",
    "validates the", "thesis",
    "amplifies concerns",
]

TIER3_STARTERS = [
    r"^so,\s",
    r"^well,\s",
    r"^now,\s(?!that|the\s(?:data|report|number))",
    r"^look,\s",
    r"^listen,\s",
    r"^basically,\s",
    r"^essentially,\s",
    r"^interestingly,\s",
    r"^notably,\s",
    r"^importantly,\s",
]

TIER3_ENDERS = [
    r"\.\.\.right\?\s*$",
    r"\.\.\.you know\?\s*$",
    r"if you will\.?\s*$",
    r"only time will tell\.?\s*$",
    r"remains to be seen\.?\s*$",
    r"watch this space\.?\s*$",
    r"stay tuned\.?\s*$",
]

TIER4_MODEL_C = [
    "disruptive", "disruption",
    "ecosystem",
    "game-changer", "game changer",
    "revolutionary",
    "groundbreaking",
    "next-generation", "next generation",
    "state-of-the-art", "state of the art",
]

SENTIMENT_LEDE_WORDS = [
    "surged", "plummeted", "soared", "tanked",
    "skyrocketed", "crashed", "rallied", "tumbled",
]

CRYPTO_BANNED_WORDS = [
    "digital gold",
    "store of value",
    "institutional adoption",
    "market sentiment",
    "massive",
    "moon", "mooning", "to the moon",
    "wagmi", "ngmi", "diamond hands",
]

# ─── Scoring Weights by Model ───

MODEL_WEIGHTS = {
    "A": {"lede": 20, "title": 10, "data_density": 25, "ai_traces": 15, "structure": 10, "attribution": 20},
    "B": {"lede": 15, "title": 15, "data_density": 15, "ai_traces": 15, "structure": 20, "attribution": 20},
    "C": {"lede": 10, "title": 15, "data_density": 15, "ai_traces": 20, "structure": 20, "attribution": 20},
    "D": {"lede": 15, "title": 10, "data_density": 25, "ai_traces": 15, "structure": 15, "attribution": 20},
    "E": {"lede": 15, "title": 10, "data_density": 25, "ai_traces": 10, "structure": 20, "attribution": 20},
    "F": {"lede": 15, "title": 10, "data_density": 25, "ai_traces": 15, "structure": 15, "attribution": 20},
}

WORD_COUNT_TARGETS = {
    "A": (400, 600),
    "B": (600, 900),
    "C": (600, 1000),
    "D": (400, 700),
    "E": (500, 800),
    "F": (400, 800),
}


def extract_title(text):
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_lede(text):
    lines = text.split("\n")
    lede_lines = []
    past_title = False
    for line in lines:
        if line.startswith("# ") and not past_title:
            past_title = True
            continue
        if past_title:
            stripped = line.strip()
            if stripped == "":
                if lede_lines:
                    break
                continue
            if stripped.startswith("**Key Takeaways") or stripped.startswith("- ") or stripped.startswith("## "):
                break
            lede_lines.append(stripped)
    return " ".join(lede_lines)


def extract_h2s(text):
    return re.findall(r"^##\s+(.+)$", text, re.MULTILINE)


def count_words(text):
    clean = re.sub(r"^---.*?---", "", text, flags=re.DOTALL)
    clean = re.sub(r"^\*.*?disclaimer.*?\*$", "", clean, flags=re.MULTILINE | re.IGNORECASE)
    clean = re.sub(r"^\*.*?does not constitute.*?\*$", "", clean, flags=re.MULTILINE | re.IGNORECASE)
    clean = re.sub(r"[#*_\[\]\(\)`>|]", " ", clean)
    return len(clean.split())


def find_numbers(text):
    patterns = [
        r"\$[\d,.]+[BMKTbmkt]?\b",
        r"[\d,.]+\s*(?:percent|%)",
        r"[\d,.]+x\b",
        r"\d{1,3}(?:,\d{3})+",
        r"(?:Q[1-4]|FY)\s*\d{2,4}",
    ]
    all_numbers = []
    for p in patterns:
        all_numbers.extend(re.findall(p, text))
    return all_numbers


def check_banned_words(text, model="A"):
    text_lower = text.lower()
    findings = {"tier1": [], "tier2": [], "tier3": [], "tier4": []}

    for word in TIER1_UNIVERSAL + TIER1_HOUSE:
        if re.search(r"\b" + re.escape(word.lower()) + r"\b", text_lower):
            findings["tier1"].append(word)

    for phrase in TIER2_PHRASES:
        if phrase.lower() in text_lower:
            findings["tier2"].append(phrase)

    sentences = re.split(r"(?<=[.!?])\s+", text)
    for sentence in sentences:
        s_lower = sentence.strip().lower()
        for pattern in TIER3_STARTERS:
            if re.match(pattern, s_lower):
                findings["tier3"].append(f"Starter: {sentence[:60]}...")
                break
        for pattern in TIER3_ENDERS:
            if re.search(pattern, s_lower):
                findings["tier3"].append(f"Ender: ...{sentence[-60:]}")
                break

    if model == "C":
        for word in TIER4_MODEL_C:
            if word.lower() in text_lower:
                findings["tier4"].append(word)

    if model == "F":
        for phrase in CRYPTO_BANNED_WORDS:
            if phrase.lower() in text_lower:
                findings["tier4"].append(f"Crypto ban: {phrase}")

    return findings


def check_attribution(text):
    # Named person + "said"
    said_count = len(re.findall(r"[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\s+said\b", text))
    # "according to [Named Entity]"
    according_count = len(re.findall(r"according to\s+[A-Z]", text))
    # Named data sources
    data_sources = [
        "Goldman", "Morgan Stanley", "JP Morgan", "JPMorgan", "Citi", "BofA",
        "Barclays", "UBS", "Deutsche", "Jefferies", "Bernstein", "Wells Fargo",
        "RBC", "BMO", "HSBC", "Mizuho", "Nomura", "Wedbush", "Stifel",
        "Cowen", "KeyBanc", "Baird", "Needham", "Evercore", "Lazard",
        "Glassnode", "CryptoQuant", "Arkham", "Nansen", "Coinglass",
        "DefiLlama", "CoinGecko", "Whale Alert", "Hashrate Index",
        "S3 Partners", "Quiver Quantitative", "TrendForce", "IDC",
        "Gartner", "Counterpoint", "Bain", "McKinsey", "BCG",
        "PitchBook", "Debtwire", "Cambridge Associates", "Kaiko",
        "Structure Research", "Drewry", "AM Best", "Marsh McLennan",
        "FactSet", "S&P Global", "Moody's", "Fitch",
    ]
    source_count = sum(1 for s in data_sources if s in text)

    return {
        "said_attributions": said_count,
        "according_to": according_count,
        "named_sources": source_count,
        "total": said_count + according_count + source_count,
    }


def score_article(text, model="A"):
    weights = MODEL_WEIGHTS[model]
    results = {}
    total = 0

    # 1. LEDE
    lede = extract_lede(text)
    lede_words = len(lede.split()) if lede else 0
    max_lede = 25 if model in ("A", "D", "E", "F") else 35

    lede_score = weights["lede"]
    lede_issues = []
    if not lede:
        lede_score = 0
        lede_issues.append("No lede found")
    else:
        if lede_words > max_lede:
            lede_score -= weights["lede"] * 0.3
            lede_issues.append(f"Lede too long: {lede_words} words (max {max_lede})")
        if model in ("A", "D", "E", "F") and not re.search(r"[\$\d]", lede[:50]):
            lede_score -= weights["lede"] * 0.2
            lede_issues.append("Lede doesn't lead with data")
        if model in ("D", "F"):
            for sw in SENTIMENT_LEDE_WORDS:
                if sw.lower() in lede.lower():
                    lede_score -= 3
                    lede_issues.append(f"Sentiment word in lede: '{sw}'")

    lede_score = max(0, round(lede_score, 1))
    results["lede"] = {"score": lede_score, "max": weights["lede"], "words": lede_words, "issues": lede_issues}
    total += lede_score

    # 2. TITLE
    title = extract_title(text)
    title_words = len(title.split()) if title else 0

    title_score = weights["title"]
    title_issues = []
    if not title:
        title_score = 0
        title_issues.append("No title found")
    else:
        if title_words > 11:
            title_score -= weights["title"] * 0.4
            title_issues.append(f"Title too long: {title_words} words (max 11)")
        if not re.search(r"[\$\d%]", title):
            title_score -= weights["title"] * 0.3
            title_issues.append("Title missing a number ($, %, or digit)")
        words_in_title = title.split()
        if len(words_in_title) > 1:
            upper_words = [w for w in words_in_title[1:] if w[0].isupper() and not re.match(r"^[A-Z]{2,}", w) and w not in ("I",)]
            if len(upper_words) > len(words_in_title) * 0.7:
                title_score -= 2
                title_issues.append("Possible title case instead of sentence case")

    title_score = max(0, round(title_score, 1))
    results["title"] = {"score": title_score, "max": weights["title"], "words": title_words, "issues": title_issues}
    total += title_score

    # 3. DATA DENSITY
    numbers = find_numbers(text)
    word_count = count_words(text)
    density = (len(numbers) / max(word_count, 1)) * 100

    data_score = weights["data_density"]
    data_issues = []
    min_density = {"A": 8, "B": 5, "C": 5, "D": 10, "E": 8, "F": 10}
    if density < min_density[model]:
        penalty = (min_density[model] - density) / min_density[model]
        data_score -= weights["data_density"] * penalty * 0.5
        data_issues.append(f"Low data density: {density:.1f}/100w (target: >= {min_density[model]})")

    wc_min, wc_max = WORD_COUNT_TARGETS[model]
    if word_count < wc_min * 0.8:
        data_score -= 3
        data_issues.append(f"Too short: {word_count} words (target: {wc_min}-{wc_max})")
    elif word_count > wc_max * 1.2:
        data_score -= 2
        data_issues.append(f"Too long: {word_count} words (target: {wc_min}-{wc_max})")

    data_score = max(0, round(data_score, 1))
    results["data_density"] = {
        "score": data_score, "max": weights["data_density"],
        "numbers_found": len(numbers), "word_count": word_count,
        "density": round(density, 1), "issues": data_issues,
    }
    total += data_score

    # 4. AI TRACES
    banned = check_banned_words(text, model)
    total_banned = sum(len(v) for v in banned.values())

    ai_score = weights["ai_traces"]
    ai_issues = []
    if total_banned > 0:
        ai_score -= len(banned["tier1"]) * 3
        ai_score -= len(banned["tier2"]) * 2
        ai_score -= len(banned["tier3"]) * 1.5
        ai_score -= len(banned["tier4"]) * 4
        if banned["tier1"]:
            ai_issues.append(f"Tier 1 banned: {', '.join(banned['tier1'])}")
        if banned["tier2"]:
            ai_issues.append(f"Tier 2 phrases: {', '.join(banned['tier2'][:3])}")
        if banned["tier3"]:
            ai_issues.append(f"Tier 3 structures: {len(banned['tier3'])} found")
        if banned["tier4"]:
            ai_issues.append(f"Tier 4 (Model C): {', '.join(banned['tier4'])}")

    ai_score = max(0, round(ai_score, 1))
    results["ai_traces"] = {"score": ai_score, "max": weights["ai_traces"], "banned_count": total_banned, "issues": ai_issues}
    total += ai_score

    # 5. STRUCTURE
    h2s = extract_h2s(text)
    has_kt = bool(re.search(r"\*\*Key Takeaways", text))
    has_disclaimer = bool(re.search(r"(?:disclaimer|does not constitute|for information)", text, re.IGNORECASE))

    struct_score = weights["structure"]
    struct_issues = []
    expected_h2 = {"A": 2, "B": 2, "C": 3, "D": 3, "E": 3, "F": 3}
    if len(h2s) < expected_h2[model]:
        struct_score -= weights["structure"] * 0.3
        struct_issues.append(f"H2s: {len(h2s)} (expected >= {expected_h2[model]})")
    if not has_kt:
        struct_score -= weights["structure"] * 0.2
        struct_issues.append("Missing Key Takeaways")
    if not has_disclaimer:
        struct_score -= weights["structure"] * 0.1
        struct_issues.append("Missing disclaimer")

    struct_score = max(0, round(struct_score, 1))
    results["structure"] = {
        "score": struct_score, "max": weights["structure"],
        "h2_count": len(h2s), "has_key_takeaways": has_kt,
        "has_disclaimer": has_disclaimer, "issues": struct_issues,
    }
    total += struct_score

    # 6. ATTRIBUTION
    attr = check_attribution(text)
    attr_score = weights["attribution"]
    attr_issues = []
    min_sources = {"A": 2, "B": 2, "C": 2, "D": 2, "E": 2, "F": 2}
    if attr["total"] < min_sources[model]:
        penalty = (min_sources[model] - attr["total"]) / min_sources[model]
        attr_score -= weights["attribution"] * penalty * 0.6
        attr_issues.append(f"Sources: {attr['total']} (target: >= {min_sources[model]})")

    attr_score = max(0, round(attr_score, 1))
    results["attribution"] = {"score": attr_score, "max": weights["attribution"], "details": attr, "issues": attr_issues}
    total += attr_score

    total = round(total, 1)
    grade = (
        "A+" if total >= 95 else "A" if total >= 85 else
        "B+" if total >= 78 else "B" if total >= 70 else
        "C+" if total >= 63 else "C" if total >= 55 else
        "D" if total >= 45 else "F"
    )

    return {"total": total, "grade": grade, "model": model, "word_count": word_count, "dimensions": results}


def print_report(result, verbose=False):
    print("=" * 60)
    print(f"  FINANCIAL NEWS QUALITY CHECK v2.0 — Model {result['model']}")
    print("=" * 60)
    print(f"  Score: {result['total']}/100  |  Grade: {result['grade']}  |  Words: {result['word_count']}")
    print("-" * 60)

    for name, data in result["dimensions"].items():
        pct = (data["score"] / data["max"] * 100) if data["max"] > 0 else 0
        bar = "\u2588" * int(pct / 5) + "\u2591" * (20 - int(pct / 5))
        icon = "\u2705" if pct >= 80 else "\u26a0\ufe0f" if pct >= 60 else "\u274c"
        print(f"  {icon} {name:<16} {data['score']:>5.1f}/{data['max']:<4} {bar}")
        if verbose and data.get("issues"):
            for issue in data["issues"]:
                print(f"     \u21b3 {issue}")

    print("-" * 60)
    all_issues = [i for d in result["dimensions"].values() for i in d.get("issues", [])]
    if all_issues:
        print(f"\n  {len(all_issues)} issue(s):")
        for idx, issue in enumerate(all_issues[:10], 1):
            print(f"     {idx}. {issue}")
        if len(all_issues) > 10:
            print(f"     ... +{len(all_issues) - 10} more (use --verbose)")
    else:
        print("\n  Clean article!")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Financial News Quality Check v2.0")
    parser.add_argument("article", help="Path to markdown article")
    parser.add_argument("--model", choices=["A", "B", "C", "D", "E", "F"], default=None)
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    text = Path(args.article).read_text(encoding="utf-8")

    model = args.model
    if not model:
        tl = text.lower()
        if any(w in tl for w in ["bitcoin", "btc", "ethereum", "eth", "on-chain", "funding rate",
                                  "liquidation", "defi", "stablecoin", "usdt", "usdc", "solana",
                                  "altcoin", "token", "crypto"]):
            model = "F"
        elif any(w in tl for w in ["copper", "gold", "iron ore", "lithium", "uranium", "lme",
                                    "comex", "mining", "commodity", "commodities", "alumin"]):
            model = "D"
        elif any(w in tl for w in ["s&p 500", "dow jones", "nasdaq", "sector rotation", "vix"]):
            model = "E"
        elif any(w in tl for w in ["gdp", "cpi", "fed", "inflation", "central bank", "monetary policy"]):
            model = "B"
        elif any(w in tl for w in ["chip", "gpu", "ai model", "semiconductor", "biotech", "ev ", "clean energy"]):
            model = "C"
        else:
            model = "A"
        if not args.json:
            print(f"  [Auto-detected model: {model}]\n")

    result = score_article(text, model)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_report(result, args.verbose)


if __name__ == "__main__":
    main()
