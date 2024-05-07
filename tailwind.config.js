/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html, js}"],
  theme: {
    extend: {
      colors: {
        "druk": "#c9cfc22",

"background": "#515b42",
// compl #4C425B

"primary": "#1b3031",
// comp #301C1B


"secondary": "#2d5052",
"accent": "#691313",
        "color-primary" : "#01051e",
        "white" : "#EEEEEE"
      }
    },
    container: {
      center: true,
      padding: {
        DEFAULT: '20px',
        md: '50px'
      }
    }
  },
  plugins: [],
}

