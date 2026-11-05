# Channel → Sub-tag → Writing Model Mapping

## Lookup Table

| Channel | Sub-tag | Model | Rationale |
|---------|---------|-------|-----------|
| **Markets** | Earnings | A — Wire | EPS, revenue, guidance — pure data |
| | Analyst Moves | A — Wire | Rating change, PT, upside % |
| | Market Moves | **E — Equity Market** | Index levels, sector rotation, VIX — NOT crypto on-chain |
| | IPO & M&A | B — Macro | Deal structure requires cause-effect analysis |
| | Shareholder Actions | A — Wire | Buyback amount, dividend yield, share count |
| **Economy** | Central Banks | B — Macro | Policy → rates → cross-asset chain |
| | Economic Data | B — Macro | Release → interpretation → market impact |
| | Trade & Tariffs | B — Macro | Geopolitical cause → economic effect |
| | Geopolitics | B — Macro | Event → multi-market impact → scenarios |
| | Regulation | B — Macro | Policy change → industry/market implication |
| **Tech & AI** | AI & ML | C — Industry | Technology + competitive landscape + investment |
| | Cloud & Data Centers | C — Industry | Infrastructure + CapEx + competition |
| | Semiconductors | C — Industry | Product cycle + supply chain + demand |
| | Software & Cyber | C — Industry | Platform + TAM + moat |
| | Hardware & Devices | C — Industry | Product + adoption + comparison |
| **Crypto** | Bitcoin & Macro | **F — Crypto** | Price, OI, funding, whale flows, levels |
| | Altcoins & DeFi | **F — Crypto** | Token, TVL, protocol metrics, levels |
| | Exchanges & Platforms | **F — Crypto** | Volume, listings, revenue, on-chain data |
| | Stablecoins & CBDC | **F — Crypto** | Supply data, peg stability, policy + on-chain |
| | Regulation & Policy | **F — Crypto** | Regulatory event → on-chain impact |
| **Energy** | Oil & Gas | B — Macro | Supply/demand + geopolitics + price |
| | Mining & Commodities | D — Mining & Commodities | Spot price, inventory, supply/demand |
| | EV & Battery | C — Industry | Technology + adoption + competition |
| | Clean Energy | C — Industry | Project + policy + cost curve |
| | Nuclear | C — Industry | Technology (SMR) + policy + demand |
| | Utilities & Grid | A — Wire | Rate changes, capex, demand growth |
| **Healthcare** | Pharma | A — Wire | Trial results, FDA dates, efficacy data |
| | Biotech | C — Industry | Science + pipeline + competition |
| | Health Services | B — Macro | Structure + cost + policy |
| | Medical Devices | C — Industry | Product + market + competition |
| **HK & China** | HK Stocks | E — Equity Market | HSI/HSTECH 行情, sector rotation, Stock Connect |
| | HK IPO | A — Wire | 招股价, oversubscription, cornerstone investors |
| | HK Earnings | A — Wire | EPS/revenue beat-miss for HKEX-listed companies |
| | China Macro | B — Macro | PMI, LPR, PBoC policy → cross-asset chain |
| **Finance** | Banking | B — Macro | NIM/credit + rate sensitivity + regulation |
| | Real Estate | B — Macro | Rate impact + supply/demand + valuation |
| | Asset Management | B — Macro | Flows + strategy + structure |
| | Insurance | A — Wire | Combined ratio, premium, loss ratio |
| | Fintech & Payments | C — Industry | Product + TAM + disruption |

## Quick Routing Decision Tree

```
Is the story about HK-LISTED STOCKS, HK IPO, or CHINA MACRO (PBoC, PMI, LPR)?
  YES → HK & China channel (E for HK Stocks, A for HK IPO/Earnings, B for China Macro)
  NO  → Is the story about CRYPTO (any token, DeFi, exchange, stablecoin, crypto regulation)?
  YES → Model F (Crypto)
  NO  → Is it about EQUITY INDEX moves (S&P, Dow, Nasdaq, sector rotation)?
    YES → Model E (Equity Market)
    NO  → Is it about MINING or COMMODITY prices/inventory?
      YES → Model D (Mining & Commodities)
      NO  → Is it about a SPECIFIC NUMBER (earnings, price target, FDA data)?
        YES → Model A (Wire)
        NO  → Is it about a POLICY, MACRO EVENT, or DEAL STRUCTURE?
          YES → Model B (Macro)
          NO  → Model C (Industry)
```

## Key Changes from v1.0

### Model E (new): Equity Market
Markets > Market Moves was incorrectly routed to Model D in v1.0.
Model E handles equity market stories with the data precision of Model D
but the cross-asset awareness of Model B.

### Model F (new): Crypto
All 5 Crypto sub-tags now route to Model F. Crypto has its own model because:
- Distinct audience (crypto-native, data-literate, skeptical of hype)
- Unique data sources (on-chain, Coinglass, Arkham, DefiLlama)
- 24/7 trading requires UTC timestamps on every data point
- Token-specific price precision rules
- Chain-specific attribution ("DeFi on Ethereum" not just "DeFi")

### Model D (renamed): Mining & Commodities
Formerly "On-chain". Now covers Energy > Mining & Commodities only.
Crypto content removed to Model F. Commodity-specific data sources
(LME, COMEX, LBMA, Fastmarkets) and price precision tables.
