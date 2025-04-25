document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('toggle-theme');
  const icon = document.getElementById('toggle-icon');
  const body = document.body;

  // Aplica tema salvo
  const savedTheme = localStorage.getItem('theme') || 'light-mode';
  body.classList.add(savedTheme);
  toggle.checked = savedTheme === 'dark-mode';
  icon.className = savedTheme === 'dark-mode' ? 'fas fa-sun' : 'fas fa-moon';

  toggle.addEventListener('change', function () {
    const isDark = this.checked;
    body.classList.remove('dark-mode', 'light-mode');
    body.classList.add(isDark ? 'dark-mode' : 'light-mode');
    localStorage.setItem('theme', isDark ? 'dark-mode' : 'light-mode');
    icon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
  });
});