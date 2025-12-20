// Modal de bienvenida
window.addEventListener('load', () => {
    setTimeout(() => {
        // Crear modal de bienvenida estilizado
        const modalBienvenida = document.createElement('div');
        modalBienvenida.className = 'modal-bienvenida-overlay';
        modalBienvenida.innerHTML = `
            <div class="modal-bienvenida-content">
                <div class="modal-icon">👋</div>
                <h2>¡Bienvenido a mi Portafolio!</h2>
                <p>Soy Juan Pablo Velez, desarrollador de software</p>
                <div class="modal-input-group">
                    <input type="text" id="nombre-visitante" placeholder="¿Cuál es tu nombre?" autocomplete="off">
                    <button id="btn-continuar" class="btn-modal-primary">Continuar</button>
                </div>
                <button id="btn-omitir" class="btn-modal-secondary">Omitir</button>
            </div>
        `;
        
        document.body.appendChild(modalBienvenida);
        
        // Focus en el input
        const inputNombre = document.getElementById('nombre-visitante');
        setTimeout(() => inputNombre.focus(), 100);
        
        // Función para cerrar modal
        const cerrarModal = (nombre = null) => {
            modalBienvenida.classList.add('fade-out');
            setTimeout(() => modalBienvenida.remove(), 500);
            
            if (nombre) {
                mostrarMensajePersonalizado(nombre);
            }
        };
        
        // Botón continuar
        document.getElementById('btn-continuar').addEventListener('click', () => {
            const nombre = inputNombre.value.trim();
            if (nombre) {
                cerrarModal(nombre);
            } else {
                inputNombre.classList.add('shake');
                inputNombre.placeholder = 'Por favor, ingresa tu nombre';
                setTimeout(() => inputNombre.classList.remove('shake'), 500);
            }
        });
        
        // Botón omitir
        document.getElementById('btn-omitir').addEventListener('click', () => {
            cerrarModal(null);
        });
        
        // Enter para continuar
        inputNombre.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                document.getElementById('btn-continuar').click();
            }
        });
        
    }, 800);
});

// Mostrar mensaje personalizado flotante
function mostrarMensajePersonalizado(nombre) {
    // Guardar nombre en localStorage para usarlo en otras páginas
    localStorage.setItem('nombreVisitante', nombre);
    
    const mensaje = document.createElement('div');
    mensaje.className = 'mensaje-personalizado';
    mensaje.innerHTML = `
        <div class="mensaje-content">
            <span class="mensaje-icon">✨</span>
            <p>¡Hola <strong>${nombre}</strong>! Gracias por visitar</p>
        </div>
    `;
    
    document.body.appendChild(mensaje);
    
    // Aparecer con animación
    setTimeout(() => mensaje.classList.add('visible'), 100);
    
    // Auto-ocultar después de 4 segundos
    setTimeout(() => {
        mensaje.classList.remove('visible');
        setTimeout(() => mensaje.remove(), 500);
    }, 4000);
}
