// =========================================
// LÓGICA PARA RECUPERACIÓN DE CONTRASEÑA
// =========================================

document.addEventListener('DOMContentLoaded', () => {
    const toggleButtons = document.querySelectorAll('.toggle-password');

    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            // 1. Obtener el ID del input objetivo
            const targetId = this.getAttribute('data-target');
            const passwordInput = document.getElementById(targetId);

            // 2. Alternar el tipo de input ('password' <-> 'text')
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);

            // 3. Alternar los íconos SVG
            const iconEyeOpen = this.querySelector('.icon-eye-open');
            const iconEyeClosed = this.querySelector('.icon-eye-closed');

            iconEyeOpen.classList.toggle('d-none');
            iconEyeClosed.classList.toggle('d-none');

            // 4. Actualizar accesibilidad
            this.setAttribute('title', type === 'password' ? 'Mostrar contraseña' : 'Ocultar contraseña');
        });
    });
});