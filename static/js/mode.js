const btn = document.getElementById('mode-switch');
const body = document.getElementById('main-body');
btn.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    body.classList.toggle('light-mode');
});
