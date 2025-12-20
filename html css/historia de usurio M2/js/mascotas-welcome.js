// Personalización del título
const tituloBienvenida = document.getElementById('titulo-bienvenida');
if (tituloBienvenida) {
    // Recuperar nombre del localStorage
    const nombreGuardado = localStorage.getItem('nombreVisitante');
    
    if (nombreGuardado) {
        // Personalizar el título con el nombre del visitante
        tituloBienvenida.innerHTML = `Bienvenida <span style="color: var(--primary-color); font-weight: bold;">${nombreGuardado}</span> a mi Galería de Mascotas`;
        
        // Agregar animación de entrada
        tituloBienvenida.style.animation = 'fadeIn 1s ease';
    }
}
