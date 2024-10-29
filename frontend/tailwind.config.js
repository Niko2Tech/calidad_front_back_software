/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        inter: ['Inter', 'sans-serif'],
      },
      animation: {
        'infinite-scroll': 'infinite-scroll 40s linear infinite',
      },
      keyframes: {
        'infinite-scroll': {
          from: { transform: 'translateX(0)' },
          to: { transform: 'translateX(-100%)' },
        }
      },
      colors: {
        'green-conaf': {
          '50': '#ecfff5',
          '100': '#d3ffe8',
          '200': '#aaffd4',
          '300': '#69ffb3',
          '400': '#21ff8b',
          '500': '#00f26a',
          '600': '#00ca54',
          '700': '#009e45',
          '800': '#00833f',
          '900': '#026533',
          '950': '#00391a',
        },
      }
    },
  },
  plugins: [],
}

