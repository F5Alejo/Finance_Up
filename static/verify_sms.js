// =========================================
// static/verify_sms.js
// LÓGICA EXCLUSIVA PARA LOS CUADROS DE CÓDIGO
// =========================================

document.addEventListener('DOMContentLoaded', () => {
    // Busca los inputs de la clase .code-box (los cuadritos)
    const inputs = document.querySelectorAll('.code-box');
    
    // Solo si existen los cuadritos en esta página
    if (inputs.length > 0) {
        inputs.forEach((input, index) => {
            // Cuando escribes, salta al siguiente
            input.addEventListener('input', function() {
                if (this.value.length === 1 && index < inputs.length - 1) {
                    inputs[index + 1].focus();
                }
            });
            
            // Cuando borras con Backspace
            input.addEventListener('keydown', function(e) {
                if (e.key === 'Backspace' && this.value.length === 0 && index > 0) {
                    inputs[index - 1].focus();
                }
            });
        });

        // Focus automático al primer cuadro al cargar
        inputs[0].focus();
    }
});