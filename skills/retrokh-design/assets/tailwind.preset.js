/**
 * RetroKh Tailwind v3 preset.
 *   // tailwind.config.js
 *   module.exports = { presets: [require('./retrokh.preset.js')], content: [...] }
 * Fonts: <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400..700&display=swap" rel="stylesheet">
 * Pair with retrokh.css (for the dark-mode CSS variables, patterns, and base) or the plugin below.
 */
const plugin = require('tailwindcss/plugin');

module.exports = {
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        rk: {
          ground: 'var(--rk-bg, #EADBB8)',
          paper: '#F1E4C6',
          sheet: 'var(--rk-sheet, #FBF5E6)',
          'paper-muted': '#D9C7A0',
          ink: '#2A1D14',
          'ink-muted': '#5A4632',
          'ink-faint': '#6E5B45',
          red: '#9E2F18',
          'red-deep': '#6E1F0F',
          'red-night': '#E2735A',
          turmeric: '#E0A526',
          'turmeric-light': '#E9B94A',
          teal: '#245A57',
          'teal-halftone': '#2F6E6A',
          plum: '#7A3E8E',
          night: '#1C130D',
          accent: 'var(--rk-accent, #9E2F18)',
          'on-accent': 'var(--rk-on-accent, #F1E4C6)',
          surface: 'var(--rk-surface, #F1E4C6)',
          text: 'var(--rk-text, #2A1D14)',
          'text-muted': 'var(--rk-text-muted, #5A4632)',
          edge: 'var(--rk-edge, #2A1D14)',
        },
      },
      // One typeface. Roles come from weight: font-normal (body), font-medium (Latin caps labels), font-bold (headings, numerals).
      fontFamily: {
        sans: ['"Google Sans"', 'sans-serif'],
      },
      lineHeight: { km: '1.7', 'km-display': '1.6' },
      boxShadow: {
        'rk-1': '3px 3px 0 var(--rk-shadow-color, #2A1D14)',
        'rk-2': '8px 8px 0 var(--rk-shadow-color, #2A1D14)',
        'rk-primary': '3px 3px 0 var(--rk-primary-shadow, #9E2F18)',
        'rk-drawer': '8px 0 0 rgba(42,29,20,.6)',
      },
      borderRadius: { none: '0' },
      minHeight: { touch: '44px', 'touch-lg': '48px' },
      height: { touch: '44px', 'touch-lg': '48px' },
      width: { touch: '44px', 'touch-lg': '48px' },
      letterSpacing: { latin: '.18em' },
    },
  },
  plugins: [
    plugin(({ addComponents, addUtilities }) => {
      addUtilities({
        '.bg-rk-zigzag': {
          background:
            'linear-gradient(135deg,#E0A526 25%,transparent 25%) -10px 0/20px 20px,linear-gradient(225deg,#E0A526 25%,transparent 25%) -10px 0/20px 20px,#9E2F18',
        },
        '.bg-rk-halftone': {
          background: 'radial-gradient(circle,rgba(20,52,50,.25) 1.3px,transparent 1.6px) 0 0/8px 8px,#2F6E6A',
        },
        '.bg-rk-rays': {
          background: 'repeating-conic-gradient(from 0deg at 50% 38%,#E0A526 0deg 9deg,#E9B94A 9deg 18deg)',
        },
        '.bg-rk-ruled': {
          background: 'repeating-linear-gradient(to bottom,transparent 0 43px,rgba(36,90,87,.22) 43px 44px)',
        },
        '.bg-rk-diamonds': {
          background:
            'linear-gradient(45deg,transparent 42%,#2A1D14 42% 58%,transparent 58%) 0 0/12px 12px,linear-gradient(-45deg,transparent 42%,#2A1D14 42% 58%,transparent 58%) 0 0/12px 12px',
        },
        '.bg-rk-hatch': {
          background: 'repeating-linear-gradient(-45deg,#2A1D14 0 6px,#5A4632 6px 12px)',
        },
        '.border-rk-double': { border: '4px double var(--rk-edge, #2A1D14)' },
        '.press': {
          '&:active': { transform: 'translate(3px,3px)', boxShadow: 'none' },
        },
      });
      addComponents({
        '.rk-stamp': {
          display: 'inline-block', padding: '0 6px', border: '2px solid currentColor',
          fontWeight: '700', fontVariantNumeric: 'tabular-nums', fontSize: '14px', lineHeight: '1.5', transform: 'rotate(-5deg)',
        },
      });
    }),
  ],
};
