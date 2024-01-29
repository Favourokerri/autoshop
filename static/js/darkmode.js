document.addEventListener('DOMContentLoaded', function() {
  const themeToggle = document.querySelector('.theme-toggle');
  const body = document.body;

  // Function to set the theme based on user preference
  const setTheme = (theme) => {
    body.classList.remove('light-mode', 'dark-mode');
    body.classList.add(theme);
    localStorage.setItem('theme', theme);
  };

  // Check for user's saved theme preference
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    setTheme(savedTheme);
    // Set the themeToggle state based on the saved theme
    themeToggle.checked = savedTheme === 'dark-mode';
  }

  // Event listener for theme toggle switch
  themeToggle.addEventListener('change', function() {
    const selectedTheme = themeToggle.checked ? 'dark-mode' : 'light-mode';
    setTheme(selectedTheme);
  });
});