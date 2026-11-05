# {Product} UI Component Generator

React/Next.js component library derived from the product's Figma design files, production website, and component specifications.

## Design System

### Colors (Example Palette — swap for your brand tokens)
```javascript
colors: {
  background: {
    primary: '#0B0D10',       // Main app background
    card: '#15181D',          // Card backgrounds
    elevated: '#1F232A',      // Modals, elevated cards
    border: '#3A3F47'         // Card borders
  },
  accent: {
    primary: '#4F8CFF',         // Primary brand accent
    green: '#22C55E',        // Gains, buy signals, positive numbers
    red: '#EF4444',          // Losses, sell signals, negative numbers
    warning: '#F59E0B'       // Warning states
  },
  text: {
    primary: '#ffffff',       // Primary text
    secondary: '#ffffffcc',   // Secondary text (80% opacity)
    muted: '#ffffff66'        // Muted text (40% opacity)
  }
}
```

### Typography ({Brand Sans} Font Family)
Load the brand font family (weights 300–900) via your font provider or self-hosted files, and set it as the Tailwind `fontFamily.sans`.

- **Headlines**: font-bold ({Brand Sans} Bold)
- **Body Text**: font-normal ({Brand Sans} Regular)
- **UI Labels**: font-medium ({Brand Sans} Medium)
- **Emphasis**: font-semibold ({Brand Sans} SemiBold)

## Core Components

### 1. Button System (Complete Implementation)

```jsx
import React from 'react';

// Button variants based on exact specifications
export const AppButton = ({
  variant = 'primary',
  size = 'medium',
  children,
  disabled = false,
  icon = null,
  iconPosition = 'left',
  onClick,
  className = ''
}) => {
  const baseStyles = 'inline-flex items-center justify-center font-medium transition-all duration-200 rounded-lg';

  // Size variations
  const sizeStyles = {
    small: 'h-8 px-3 text-sm',
    medium: 'h-10 px-4 text-sm',
    large: 'h-12 px-6 text-base'
  };

  // Variant styles based on specifications
  const variantStyles = {
    // Text buttons based on the button component spec
    primary: 'bg-white text-[#0B0D10] hover:bg-white/70 disabled:bg-white/20',
    secondary: 'bg-transparent text-white border border-white/20 hover:bg-white/5 disabled:border-white/10 disabled:text-white/60',
    tonal: 'bg-[#4F8CFF]/20 text-[#4F8CFF] hover:bg-[#4F8CFF]/30 disabled:bg-[#4F8CFF]/10 disabled:text-[#4F8CFF]/40',
    text_general: 'bg-transparent text-white hover:bg-white/10 disabled:text-white/40',
    text_brand: 'bg-transparent text-[#4F8CFF] hover:bg-[#4F8CFF]/10 disabled:text-[#4F8CFF]/40',
    emphasis: 'bg-[#1F232A] border-2 border-[#4F8CFF]/40 text-transparent bg-clip-text bg-gradient-to-r from-[#4F8CFF] to-white hover:border-[#4F8CFF]/60 hover:brightness-110 disabled:opacity-40',
    ai: 'bg-[#4F8CFF]/20 text-white hover:bg-[#4F8CFF]/40 disabled:bg-[#4F8CFF]/10 disabled:text-white/60'
  };

  const combinedStyles = `${baseStyles} ${sizeStyles[size]} ${variantStyles[variant]} ${disabled ? 'cursor-not-allowed' : 'cursor-pointer'} ${className}`;

  return (
    <button
      className={combinedStyles}
      disabled={disabled}
      onClick={onClick}
    >
      {icon && iconPosition === 'left' && <span className="mr-2">{icon}</span>}
      {children}
      {icon && iconPosition === 'right' && <span className="ml-2">{icon}</span>}
    </button>
  );
};

// Icon button variants
export const AppIconButton = ({
  variant = 'tonal',
  size = 'medium',
  children,
  disabled = false,
  onClick,
  className = ''
}) => {
  const baseStyles = 'inline-flex items-center justify-center font-medium transition-all duration-200 rounded-lg';

  const sizeStyles = {
    small: 'w-8 h-8',
    medium: 'w-10 h-10',
    large: 'w-12 h-12'
  };

  const variantStyles = {
    tonal: 'bg-[#4F8CFF]/20 text-[#4F8CFF] hover:bg-[#4F8CFF]/30',
    outline: 'border border-[#3A3F47] text-white hover:border-[#4F8CFF]',
    solid: 'bg-[#4F8CFF] text-black hover:bg-[#4F8CFF]/80'
  };

  return (
    <button
      className={`${baseStyles} ${sizeStyles[size]} ${variantStyles[variant]} ${disabled ? 'opacity-40 cursor-not-allowed' : ''} ${className}`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
};
```

### 2. Input Components (3 Types)

```jsx
import React, { useState } from 'react';

// Regular Input Field with 6 states
export const AppInput = ({
  type = 'text',
  placeholder,
  value,
  onChange,
  disabled = false,
  error = false,
  errorMessage,
  label,
  className = ''
}) => {
  const [focused, setFocused] = useState(false);
  const [filled, setFilled] = useState(!!value);

  const inputStyles = `
    w-full h-12 px-4 py-3 bg-[#15181D] border rounded-lg
    text-white placeholder-[#ffffffcc] font-normal text-sm
    transition-all duration-200 outline-none
    ${error ? 'border-[#EF4444] focus:border-[#EF4444]' :
      focused ? 'border-[#4F8CFF] bg-[#4F8CFF]/5' :
      filled ? 'border-[#3A3F47]' :
      disabled ? 'border-[#3A3F47] bg-[#3A3F47]/20 cursor-not-allowed' :
      'border-[#3A3F47] hover:border-[#3A3F47]/80'}
  `;

  return (
    <div className={className}>
      {label && <label className="block text-sm font-medium text-white mb-2">{label}</label>}
      <input
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={(e) => {
          onChange(e);
          setFilled(!!e.target.value);
        }}
        onFocus={() => setFocused(true)}
        onBlur={() => setFocused(false)}
        disabled={disabled}
        className={inputStyles}
      />
      {error && errorMessage && (
        <p className="text-[#EF4444] text-xs mt-1">{errorMessage}</p>
      )}
    </div>
  );
};

// AI Chat Input Desktop (expandable 88px → 249px)
export const AppAIChatInputDesktop = ({
  value,
  onChange,
  onSubmit,
  placeholder = "Ask me anything about the market...",
  className = ''
}) => {
  const [focused, setFocused] = useState(false);
  const [expanded, setExpanded] = useState(false);

  return (
    <div className={`relative ${className}`}>
      <div className={`
        bg-[#15181D] border-2 border-transparent rounded-xl p-4
        transition-all duration-300 ease-out
        ${focused || expanded ?
          'border-[#4F8CFF] bg-gradient-to-r from-[#4F8CFF]/10 to-[#22C55E]/5' :
          'border-[#3A3F47]'
        }
        ${expanded ? 'h-[249px]' : 'h-[88px]'}
      `}>
        <textarea
          value={value}
          onChange={onChange}
          onFocus={() => {
            setFocused(true);
            setExpanded(true);
          }}
          onBlur={() => setFocused(false)}
          placeholder={placeholder}
          className="w-full h-full bg-transparent text-white placeholder-[#ffffffcc] resize-none outline-none"
          rows={expanded ? 8 : 2}
        />
        <button
          onClick={onSubmit}
          className="absolute bottom-4 right-4 w-8 h-8 bg-[#4F8CFF] rounded-full flex items-center justify-center text-black hover:scale-105 transition-transform"
        >
          →
        </button>
      </div>
    </div>
  );
};

// AI Chat Input App (compact 52-56px)
export const AppAIChatInputApp = ({
  value,
  onChange,
  onSubmit,
  placeholder = "Ask AI...",
  className = ''
}) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className={`relative ${className}`}>
      {!isOpen ? (
        <button
          onClick={() => setIsOpen(true)}
          className="w-full h-[52px] bg-[#15181D] border border-[#3A3F47] rounded-lg px-4 flex items-center justify-between hover:border-[#4F8CFF]/50 transition-colors"
        >
          <span className="text-[#ffffffcc] text-sm">{placeholder}</span>
          <div className="w-6 h-6 bg-[#4F8CFF] rounded-full flex items-center justify-center">
            <span className="text-black text-xs font-bold">AI</span>
          </div>
        </button>
      ) : (
        <div className="bg-[#15181D] border border-[#4F8CFF] rounded-lg p-3">
          <input
            type="text"
            value={value}
            onChange={onChange}
            placeholder={placeholder}
            className="w-full bg-transparent text-white placeholder-[#ffffffcc] outline-none text-sm mb-3"
            autoFocus
          />
          <div className="flex justify-end gap-2">
            <button
              onClick={() => setIsOpen(false)}
              className="text-[#ffffffcc] text-sm hover:text-white"
            >
              Cancel
            </button>
            <button
              onClick={onSubmit}
              className="bg-[#4F8CFF] text-black px-3 py-1 rounded text-sm font-medium hover:bg-[#4F8CFF]/80"
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
```

### 3. Notification Components

```jsx
import React, { useState, useEffect } from 'react';

// Snackbar with 3 variants (auto-dismiss after 3s)
export const AppSnackbar = ({
  variant = 'success',
  message,
  visible = false,
  onClose,
  className = ''
}) => {
  useEffect(() => {
    if (visible) {
      const timer = setTimeout(onClose, 3000);
      return () => clearTimeout(timer);
    }
  }, [visible, onClose]);

  const variantStyles = {
    success: 'bg-[#22C55E] text-black',
    error: 'bg-[#EF4444] text-white',
    warning: 'bg-[#F59E0B] text-black'
  };

  const icons = {
    success: '✓',
    error: '✕',
    warning: '⚠'
  };

  if (!visible) return null;

  return (
    <div className={`fixed bottom-6 left-1/2 transform -translate-x-1/2 z-50 animate-slide-up ${className}`}>
      <div className={`${variantStyles[variant]} px-4 py-3 rounded-lg flex items-center gap-2 shadow-lg max-w-sm`}>
        <span className="text-lg">{icons[variant]}</span>
        <span className="text-sm font-medium">{message}</span>
        <button
          onClick={onClose}
          className="ml-2 opacity-70 hover:opacity-100"
        >
          ✕
        </button>
      </div>
    </div>
  );
};

// Tooltip with Simple and Paragraph variants
export const AppTooltip = ({
  children,
  content,
  variant = 'simple',
  position = 'top',
  className = ''
}) => {
  const [visible, setVisible] = useState(false);

  const positionStyles = {
    top: 'bottom-full left-1/2 transform -translate-x-1/2 mb-2',
    bottom: 'top-full left-1/2 transform -translate-x-1/2 mt-2',
    left: 'right-full top-1/2 transform -translate-y-1/2 mr-2',
    right: 'left-full top-1/2 transform -translate-y-1/2 ml-2'
  };

  return (
    <div
      className={`relative inline-block ${className}`}
      onMouseEnter={() => setVisible(true)}
      onMouseLeave={() => setVisible(false)}
    >
      {children}
      {visible && (
        <div className={`absolute ${positionStyles[position]} z-50`}>
          <div className="bg-[#1F232A] text-white text-sm px-3 py-2 rounded-lg shadow-lg max-w-xs">
            {variant === 'paragraph' && (
              <div className="flex items-start gap-2">
                <div className="w-4 h-4 bg-[#4F8CFF] rounded-full flex items-center justify-center text-black text-xs">i</div>
                <div>{content}</div>
              </div>
            )}
            {variant === 'simple' && content}
          </div>
        </div>
      )}
    </div>
  );
};

// Alert Message for page-level notifications
export const AppAlert = ({
  variant = 'brand',
  title,
  message,
  onClose,
  actions,
  className = ''
}) => {
  const variantStyles = {
    brand: 'bg-[#4F8CFF]/10 border-[#4F8CFF]/20 text-white',
    error: 'bg-[#EF4444]/10 border-[#EF4444]/20 text-white',
    success: 'bg-[#22C55E]/10 border-[#22C55E]/20 text-white',
    warning: 'bg-[#F59E0B]/10 border-[#F59E0B]/20 text-white'
  };

  const iconColors = {
    brand: 'text-[#4F8CFF]',
    error: 'text-[#EF4444]',
    success: 'text-[#22C55E]',
    warning: 'text-[#F59E0B]'
  };

  return (
    <div className={`border rounded-lg p-4 ${variantStyles[variant]} ${className}`}>
      <div className="flex items-start justify-between">
        <div className="flex items-start gap-3">
          <div className={`text-lg ${iconColors[variant]}`}>
            {variant === 'success' ? '✓' : variant === 'error' ? '✕' : variant === 'warning' ? '⚠' : 'i'}
          </div>
          <div>
            {title && <h4 className="font-medium mb-1">{title}</h4>}
            <p className="text-sm text-[#ffffffcc]">{message}</p>
            {actions && (
              <div className="flex gap-2 mt-3">
                {actions.map((action, index) => (
                  <button
                    key={index}
                    onClick={action.onClick}
                    className={`px-3 py-1 text-sm rounded ${action.primary ?
                      `bg-${variant === 'brand' ? '[#4F8CFF]' : variant === 'success' ? '[#22C55E]' : variant === 'error' ? '[#EF4444]' : '[#F59E0B]'} text-black` :
                      'bg-transparent border border-[#3A3F47] text-white hover:border-[#4F8CFF]'
                    }`}
                  >
                    {action.label}
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>
        {onClose && (
          <button
            onClick={onClose}
            className="text-[#ffffffcc] hover:text-white"
          >
            ✕
          </button>
        )}
      </div>
    </div>
  );
};
```

### 4. Tab System (3 Styles)

```jsx
import React from 'react';

// General Tab for content navigation
export const AppGeneralTabs = ({
  tabs,
  activeTab,
  onChange,
  className = ''
}) => {
  return (
    <div className={`relative ${className}`}>
      <div className="flex border-b border-[#3A3F47]">
        {tabs.map((tab, index) => (
          <button
            key={index}
            onClick={() => onChange(index)}
            className={`px-4 py-3 text-sm font-medium transition-colors relative ${
              activeTab === index
                ? 'text-[#4F8CFF]'
                : 'text-[#ffffffcc] hover:text-white'
            }`}
          >
            {tab.label}
            {activeTab === index && (
              <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-[#4F8CFF] transition-all duration-200" />
            )}
          </button>
        ))}
      </div>
      <div className="mt-4">
        {tabs[activeTab]?.content}
      </div>
    </div>
  );
};

// Filter Group for time filtering
export const AppFilterGroup = ({
  options,
  selected,
  onChange,
  className = ''
}) => {
  return (
    <div className={`inline-flex bg-[#15181D] border border-[#3A3F47] rounded-lg p-1 ${className}`}>
      {options.map((option, index) => (
        <button
          key={index}
          onClick={() => onChange(option.value)}
          className={`px-3 py-2 text-sm font-medium rounded transition-all duration-200 ${
            selected === option.value
              ? 'bg-[#4F8CFF] text-black'
              : 'text-[#ffffffcc] hover:text-white hover:bg-white/5'
          }`}
        >
          {option.label}
        </button>
      ))}
    </div>
  );
};

// Switch/Toggle Group for binary choices
export const AppSwitchGroup = ({
  options,
  selected,
  onChange,
  className = ''
}) => {
  return (
    <div className={`relative inline-flex bg-[#15181D] border border-[#3A3F47] rounded-lg p-1 ${className}`}>
      <div
        className="absolute top-1 bottom-1 bg-white rounded transition-all duration-300 ease-out"
        style={{
          left: `${(selected === options[0].value ? 0 : 50)}%`,
          width: '50%',
          transform: `translateX(${selected === options[0].value ? '4px' : '-4px'})`
        }}
      />
      {options.map((option, index) => (
        <button
          key={index}
          onClick={() => onChange(option.value)}
          className={`relative z-10 px-4 py-2 text-sm font-medium transition-colors duration-200 ${
            selected === option.value
              ? 'text-black'
              : 'text-[#ffffffcc] hover:text-white'
          }`}
        >
          {option.label}
        </button>
      ))}
    </div>
  );
};
```

### 5. Toggle Switch

```jsx
import React, { useState } from 'react';

export const AppToggle = ({
  label,
  checked = false,
  disabled = false,
  onChange,
  id,
  className = ''
}) => {
  const [isChecked, setIsChecked] = useState(checked);

  const toggleId = id || `toggle-${Math.random().toString(36).substr(2, 9)}`;

  const handleChange = (e) => {
    if (!disabled) {
      const newChecked = e.target.checked;
      setIsChecked(newChecked);
      if (onChange) {
        onChange(newChecked);
      }
    }
  };

  return (
    <label className={`flex items-center gap-3 cursor-pointer select-none ${className}`}>
      <input
        type="checkbox"
        id={toggleId}
        checked={isChecked}
        disabled={disabled}
        onChange={handleChange}
        className="sr-only"
      />
      <div className={`
        relative w-11 h-6 rounded-full transition-all duration-300 ease-out
        ${isChecked
          ? 'bg-[#4F8CFF]'
          : 'bg-transparent border border-[#3A3F47]'
        }
        ${disabled ? 'opacity-40 cursor-not-allowed' : ''}
      `}>
        <div className={`
          absolute top-1 w-4 h-4 bg-white rounded-full transition-all duration-300 ease-out
          shadow-sm
          ${isChecked
            ? 'left-6 bg-[#0B0D10]'
            : 'left-1 bg-white/60'
          }
        `} />
      </div>
      {label && (
        <span className={`text-sm text-white ${disabled ? 'opacity-40' : ''}`}>
          {label}
        </span>
      )}
    </label>
  );
};
```

### 6. Stock Pick Card (Enhanced)

```jsx
import React from 'react';

export const AppStockPickCard = ({
  ticker,
  companyName,
  entryPrice,
  stopLoss,
  currentPrice,
  potential,
  thesis,
  winRate,
  rating = 'Strong Buy',
  className = ''
}) => {
  return (
    <div className={`bg-[#15181D] border border-[#3A3F47] rounded-xl p-4 min-w-[280px] flex-shrink-0 ${className}`}>
      <div className="flex items-start justify-between mb-3">
        <div>
          <div className="flex items-center gap-2">
            <h3 className="text-white font-bold text-lg">{ticker}</h3>
            <div className="w-8 h-8 border border-[#4F8CFF] rounded-full flex items-center justify-center">
              <span className="text-[#4F8CFF] text-xs font-bold">{winRate}</span>
            </div>
          </div>
          <p className="text-[#ffffffcc] text-sm">{companyName}</p>
          <div className={`inline-block px-2 py-1 rounded text-xs font-bold mt-1 ${
            rating.includes('Strong') ? 'bg-[#22C55E]/20 text-[#22C55E]' : 'bg-[#4F8CFF]/20 text-[#4F8CFF]'
          }`}>
            {rating}
          </div>
        </div>
      </div>

      <div className="space-y-2 text-sm mb-4">
        <div className="flex justify-between">
          <span className="text-[#ffffffcc]">Entry</span>
          <span className="text-white font-medium">${entryPrice}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-[#ffffffcc]">Stop</span>
          <span className="text-white font-medium">${stopLoss}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-[#ffffffcc]">Current</span>
          <span className="text-white font-medium">${currentPrice}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-[#ffffffcc]">Potential</span>
          <span className="text-[#4F8CFF] font-bold">{potential}</span>
        </div>
      </div>

      <div className="border-t border-[#3A3F47] pt-3">
        <div className="text-[#ffffffcc] text-xs font-bold mb-2">THE THESIS</div>
        <p className="text-[#ffffffcc] text-sm leading-relaxed">{thesis}</p>
      </div>
    </div>
  );
};
```

### 7. Section Header Component

```jsx
import React from 'react';

export const AppSectionHeader = ({
  title,
  subtitle,
  winRate,
  onViewMore,
  className = ''
}) => (
  <div className={`flex items-center justify-between mb-4 ${className}`}>
    <div>
      <div className="flex items-center gap-3">
        <h2 className="text-lg font-bold text-white">{title}</h2>
        {winRate && (
          <div className="w-10 h-10 border-2 border-[#4F8CFF] rounded-full flex items-center justify-center">
            <span className="text-[#4F8CFF] text-xs font-bold">{winRate}</span>
          </div>
        )}
      </div>
      {subtitle && <p className="text-[#ffffffcc] text-sm mt-1">{subtitle}</p>}
    </div>
    {onViewMore && (
      <button
        onClick={onViewMore}
        className="text-[#4F8CFF] text-sm font-medium hover:text-[#4F8CFF]/80 transition-colors"
      >
        View More →
      </button>
    )}
  </div>
);
```

### 8. Signal Banner

```jsx
import React from 'react';

export const AppSignalBanner = ({
  signalCount,
  currentTicker,
  currentEvent,
  className = ''
}) => (
  <div className={`bg-gradient-to-r from-[#4F8CFF]/20 to-[#22C55E]/20 border border-[#4F8CFF]/30 rounded-xl p-4 ${className}`}>
    <div className="flex items-center gap-3">
      <div className="w-3 h-3 bg-[#4F8CFF] rounded-full animate-pulse"></div>
      <div className="text-white">
        <span className="font-bold">{signalCount.toLocaleString()}</span> signals scanned today
      </div>
    </div>
    <div className="mt-2 text-[#ffffffcc] text-sm">
      · Analyzing <span className="text-[#4F8CFF] font-medium">{currentTicker}</span> {currentEvent}...
    </div>
  </div>
);
```

### 9. Mission Card

```jsx
import React from 'react';

export const AppMissionCard = ({
  title,
  description,
  credits,
  status = 'pending',
  progress = 0,
  maxProgress = 1,
  category,
  onAction,
  className = ''
}) => (
  <div className={`bg-[#15181D] border border-[#3A3F47] rounded-xl p-4 ${className}`}>
    <div className="flex items-start justify-between mb-3">
      <div className="text-[#22C55E] text-lg font-bold">+{credits}</div>
      <div className="text-[#ffffffcc] text-xs">{category}</div>
    </div>

    <h3 className="text-white font-medium mb-2">{title}</h3>
    <p className="text-[#ffffffcc] text-sm mb-4">{description}</p>

    {status === 'completed' ? (
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-4 h-4 bg-[#22C55E] rounded-full flex items-center justify-center">
            <svg width="10" height="8" viewBox="0 0 10 8" fill="none">
              <path d="M1 4L3.5 6.5L9 1" stroke="black" strokeWidth="2"/>
            </svg>
          </div>
          <span className="text-[#22C55E] text-sm font-bold">COMPLETED</span>
        </div>
        <button className="bg-[#22C55E] text-black px-4 py-2 rounded-lg text-sm font-bold">
          Claim
        </button>
      </div>
    ) : (
      <>
        {maxProgress > 1 && (
          <div className="mb-4">
            <div className="flex justify-between text-sm mb-1">
              <span className="text-[#ffffffcc]">Progress: {progress}/{maxProgress}</span>
            </div>
            <div className="w-full bg-[#3A3F47] rounded-full h-2">
              <div
                className="bg-[#4F8CFF] h-2 rounded-full transition-all duration-300"
                style={{ width: `${(progress / maxProgress) * 100}%` }}
              ></div>
            </div>
          </div>
        )}
        <button
          onClick={onAction}
          className="bg-[#1F232A] border border-[#3A3F47] text-white px-4 py-2 rounded-lg text-sm font-medium hover:border-[#4F8CFF] transition-colors w-full"
        >
          Go
        </button>
      </>
    )}
  </div>
);
```

### 10. AI Chat Interface

```jsx
import React from 'react';

export const AppAIChat = ({
  isOpen,
  onToggle,
  greeting,
  suggestedPrompts,
  className = ''
}) => (
  <>
    {/* Chat Button */}
    {!isOpen && (
      <button
        onClick={onToggle}
        className="fixed bottom-6 right-6 w-14 h-14 bg-gradient-to-r from-[#4F8CFF] to-[#22C55E] rounded-full flex items-center justify-center shadow-lg hover:scale-105 transition-transform z-50"
      >
        <div className="text-black font-bold text-sm">AI</div>
      </button>
    )}

    {/* Chat Interface */}
    {isOpen && (
      <div className="fixed bottom-6 right-6 w-80 bg-[#15181D] border border-[#3A3F47] rounded-xl shadow-xl z-50">
        <div className="flex items-center justify-between p-4 border-b border-[#3A3F47]">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-gradient-to-r from-[#4F8CFF] to-[#22C55E] rounded-full flex items-center justify-center">
              <span className="text-black text-sm font-bold">AI</span>
            </div>
            <span className="text-white font-medium">{Assistant}</span>
          </div>
          <button
            onClick={onToggle}
            className="text-[#ffffffcc] hover:text-white transition-colors"
          >
            ✕
          </button>
        </div>

        <div className="p-4">
          <p className="text-[#ffffffcc] text-sm mb-4">{greeting}</p>
          <div className="space-y-2">
            {suggestedPrompts.map((prompt, index) => (
              <button
                key={index}
                className="w-full text-left bg-[#1F232A] border border-[#3A3F47] rounded-lg p-3 text-[#ffffffcc] text-sm hover:text-white hover:border-[#4F8CFF] transition-colors"
              >
                {prompt}
              </button>
            ))}
          </div>
        </div>
      </div>
    )}
  </>
);
```

## Layout Patterns

### Horizontal Scroll Cards
```jsx
// Standard pattern for card collections
<div className="overflow-x-auto">
  <div className="flex gap-4 pb-4">
    {cards.map((card, index) => (
      <Card key={index} {...card} />
    ))}
  </div>
</div>
```

### Grid Layouts
```jsx
// Responsive grid patterns
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  {items.map((item, index) => (
    <Item key={index} {...item} />
  ))}
</div>
```

## Usage Examples

### Complete Page Layout
```jsx
import React, { useState } from 'react';

const MarketIntelligencePage = () => {
  const [chatOpen, setChatOpen] = useState(false);

  return (
    <div className="min-h-screen bg-[#0B0D10] text-white">
      {/* Header */}
      <header className="sticky top-0 bg-[#0B0D10]/90 backdrop-blur border-b border-[#3A3F47] p-4">
        <div className="max-w-6xl mx-auto flex justify-between items-center">
          <div>
            <h1 className="text-2xl font-bold">Market Intelligence</h1>
            <p className="text-[#ffffffcc] text-sm">AI-powered market analysis and high-conviction signals</p>
          </div>
          <div className="flex gap-2">
            <AppButton variant="secondary">Filters</AppButton>
            <AppButton variant="primary">View All</AppButton>
          </div>
        </div>
      </header>

      {/* Signal Banner */}
      <div className="max-w-6xl mx-auto px-4 py-6">
        <AppSignalBanner
          signalCount={2847}
          currentTicker="NVDA"
          currentEvent="Institutional Flow Analysis"
        />
      </div>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-4 space-y-8">
        {/* High-Conviction Signals */}
        <section>
          <AppSectionHeader
            title="High-Conviction Signals"
            winRate="91%"
            onViewMore={() => console.log('View more')}
          />

          <div className="overflow-x-auto">
            <div className="flex gap-4 pb-4">
              <AppStockPickCard
                ticker="NVDA"
                companyName="NVIDIA Corporation"
                entryPrice="875.00"
                stopLoss="820.00"
                currentPrice="892.50"
                potential="+8.2%"
                thesis="Data center demand accelerating. Q4 guidance beats 15%."
                winRate="94%"
                rating="Strong Buy"
              />
              <AppStockPickCard
                ticker="AMD"
                companyName="Advanced Micro Devices"
                entryPrice="142.00"
                stopLoss="135.00"
                currentPrice="148.75"
                potential="+12.8%"
                thesis="MI350 orders beating expectations. NVDA premium rotation."
                winRate="89%"
                rating="Strong Buy"
              />
            </div>
          </div>
        </section>
      </main>

      {/* AI Chat */}
      <AppAIChat
        isOpen={chatOpen}
        onToggle={() => setChatOpen(!chatOpen)}
        greeting="How can I help you analyze the market today?"
        suggestedPrompts={[
          "What's driving NVDA today?",
          "Show me high-momentum stocks",
          "Analyze crypto correlation"
        ]}
      />
    </div>
  );
};
```

## Component Decision Tree

### When to Use Which Component

**Buttons:**
- Primary: Main CTAs, form submissions
- Secondary: Secondary actions, cancellation
- Tonal: Subtle actions, filters
- Text: Minimal actions, navigation
- AI: Chat interactions, AI features

**Inputs:**
- Regular: Forms, settings
- AI Desktop: Chat interfaces on desktop
- AI App: Chat interfaces in mobile app

**Notifications:**
- Snackbar: Success/error feedback
- Tooltip: Help text, additional info
- Alert: Important page-level messages

**Tabs:**
- General: Content navigation
- Filter: Time periods, categories
- Switch: Binary toggles with labels

**Toggle:**
- Settings that take effect immediately
- Binary on/off states

This complete component library ensures 100% brand consistency and production-ready quality for all {Product} UI development work.