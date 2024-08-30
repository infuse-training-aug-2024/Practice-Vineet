function clock_time() {
    const clock = document.getElementById('clock');
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    clock.textContent = `${hours}:${minutes}:${seconds}`;
  }
  function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode');
 
    const button = document.getElementById('toggle-theme');
    if (body.classList.contains('dark-mode')) {
      button.textContent = 'Light Mode';
    } else {
      button.textContent = 'Dark Mode';
    }
  }
  setInterval(clock_time, 1000);  
  clock_time();
  document.getElementById('toggle-theme').addEventListener('click', toggleTheme);