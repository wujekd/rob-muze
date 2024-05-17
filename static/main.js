// Toggle theme

console.log('My script is being imported and executed in the browser.');


const html = document.querySelector('html');
const toggleTheme = document.querySelector('#toggle-theme');
const toggleThemeIcon = toggleTheme.querySelector('img');

toggleTheme.addEventListener('click', () => {
    const isDark = html.classList.contains('dark')
    const themeIcon = isDark ? 'light' : 'dark'
    toggleThemeIcon.src = 'images/icons/icon-${themeIcon}.svg';
})





