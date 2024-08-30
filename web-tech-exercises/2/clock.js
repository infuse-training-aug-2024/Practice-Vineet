function clock_time() {
    const clock = document.getElementById('clock');
    const now = new Date();
    clock.textContent = now.toLocaleTimeString('en-US');
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
  document.getElementById('toggle-theme').addEventListener('click', toggleTheme);