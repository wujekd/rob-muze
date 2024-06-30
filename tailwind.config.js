/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html, js}"],
  theme: {
    extend: {
      colors: {
"druk": "#c9cfc22",

"background": "#3f7072",
// compl #4C425B
'offblue' : '#488083',

"primary": "#1b3031",
// comp #301C1B

"warning" : "#8F3739",

"secondary": "#2d5052",

"bone" : "#F2EBE3",

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

