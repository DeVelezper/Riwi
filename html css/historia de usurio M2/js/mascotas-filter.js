// Sistema de filtrado de mascotas
const btnFiltrar = document.getElementById('btn-filtrar');
const panelFiltros = document.getElementById('panel-filtros');
const mensajeFiltro = document.getElementById('mensaje-filtro');
const totalMascotasElement = document.getElementById('total-mascotas');
const mascotasVisiblesElement = document.getElementById('mascotas-visibles');
const botonesFiltro = document.querySelectorAll('.btn-filtro');
const tarjetasMascotas = document.querySelectorAll('.mascota-card');

let filtroActual = 'todas';

// Mensajes dinámicos según el filtro
const mensajesFiltro = {
    'todas': 'Mostrando todas las mascotas 🐾',
    'perro': 'Mostrando solo perros 🐕',
    'gato': 'Mostrando solo gatos 🐈'
};

// Mostrar/Ocultar panel de filtros
if (btnFiltrar && panelFiltros) {
    btnFiltrar.addEventListener('click', () => {
        panelFiltros.classList.toggle('hidden');
        
        if (!panelFiltros.classList.contains('hidden')) {
            btnFiltrar.innerHTML = '<span class="btn-icon">✖️</span> Cerrar Filtros';
        } else {
            btnFiltrar.innerHTML = '<span class="btn-icon">🔍</span> Filtrar Mascotas';
        }
    });
}

// Función para filtrar mascotas
function filtrarMascotas(tipo) {
    filtroActual = tipo;
    let mascotasVisibles = 0;
    
    tarjetasMascotas.forEach(mascota => {
        if (tipo === 'todas' || mascota.dataset.tipo === tipo) {
            mascota.style.display = 'block';
            mascota.style.animation = 'fadeIn 0.5s ease';
            mascotasVisibles++;
        } else {
            mascota.style.display = 'none';
        }
    });
    
    // Actualizar mensaje y contador
    mensajeFiltro.textContent = mensajesFiltro[tipo];
    mensajeFiltro.style.opacity = '0';
    setTimeout(() => {
        mensajeFiltro.style.opacity = '1';
    }, 100);
    
    mascotasVisiblesElement.textContent = mascotasVisibles;
    
    // Resaltar botón activo
    botonesFiltro.forEach(btn => {
        if (btn.dataset.tipo === tipo) {
            btn.style.background = 'linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%)';
            btn.style.color = 'white';
            btn.style.transform = 'scale(1.05)';
        } else {
            btn.style.background = 'transparent';
            btn.style.color = 'var(--primary-color)';
            btn.style.transform = 'scale(1)';
        }
    });
}

// Event listeners para botones de filtro
botonesFiltro.forEach(boton => {
    boton.addEventListener('click', () => {
        const tipo = boton.dataset.tipo;
        filtrarMascotas(tipo);
        
        // Efecto de clic en el botón
        boton.style.transform = 'scale(0.95)';
        setTimeout(() => {
            boton.style.transform = filtroActual === tipo ? 'scale(1.05)' : 'scale(1)';
        }, 150);
    });
});

// Inicializar contador total de mascotas
if (totalMascotasElement) {
    totalMascotasElement.textContent = tarjetasMascotas.length;
}
