/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html, js}"],
  theme: {
    extend: {
      colors: {
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

