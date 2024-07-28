/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        'elding-blue': '#000e52',
      },
    },

  },
  plugins: [
    require('flowbite/plugin'),
  ],
}

