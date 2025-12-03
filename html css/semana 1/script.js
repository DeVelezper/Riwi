const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Cargar tema guardado
const savedTheme = localStorage.getItem('theme') || 'light';
if (savedTheme === 'dark') {
    body.classList.add('dark-mode');
}
updateButton(savedTheme);

// Evento de clic en el botón
themeToggle.addEventListener('click', () => {
    if (body.classList.contains('dark-mode')) {
        body.classList.remove('dark-mode');
        updateButton('light');
        localStorage.setItem('theme', 'light');
    } else {
        body.classList.add('dark-mode');
        updateButton('dark');
        localStorage.setItem('theme', 'dark');
    }
});

// Actualizar texto del botón
function updateButton(theme) {
    if (theme === 'dark') {
        themeToggle.textContent = 'Modo Claro';
    } else {
        themeToggle.textContent = 'Modo Oscuro';
    }
}