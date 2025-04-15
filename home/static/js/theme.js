document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.getElementById('toggle-theme');
    const icon = document.getElementById('toggle-icon');
    const body = document.body;
  
    // Aplica tema salvo
    const savedTheme = localStorage.getItem('theme') || 'light-mode';
    body.className = savedTheme;
    toggle.checked = savedTheme === 'dark-mode';
    icon.className = savedTheme === 'dark-mode' ? 'fas fa-sun' : 'fas fa-moon';
  
    toggle.addEventListener('change', function () {
      const isDark = this.checked;
      body.className = isDark ? 'dark-mode' : 'light-mode';
      localStorage.setItem('theme', isDark ? 'dark-mode' : 'light-mode');
      icon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
    });
  });  