// Efecto rotación en imagen de perfil
const profileImg = document.getElementById('profile-img');

if (profileImg) {
    let rotation = 0;
    
    profileImg.addEventListener('click', () => {
        rotation += 360;
        profileImg.style.transform = `scale(1.1) rotate(${rotation}deg)`;
        
        setTimeout(() => {
            profileImg.style.transform = 'scale(1) rotate(0deg)';
        }, 600);
    });
}
