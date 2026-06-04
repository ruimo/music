// Theme toggle functionality
(function() {
    'use strict';
    
    function initThemeToggle() {
        const themeToggle = document.getElementById('theme-toggle');
        if (!themeToggle) {
            console.error('Theme toggle button not found');
            return;
        }
        
        const themeIcon = themeToggle.querySelector('.theme-toggle-icon');
        if (!themeIcon) {
            console.error('Theme toggle icon not found');
            return;
        }
        
        const html = document.documentElement;
        
        function updateIcon(theme) {
            themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
        }
        
        function setTheme(theme) {
            html.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
            updateIcon(theme);
        }
        
        // Check for saved theme preference or default to system preference
        const savedTheme = localStorage.getItem('theme');
        const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        
        if (savedTheme) {
            setTheme(savedTheme);
        } else if (systemPrefersDark) {
            setTheme('dark');
        } else {
            setTheme('light');
        }
        
        // Add click event listener
        themeToggle.addEventListener('click', function(e) {
            console.log('Button clicked!');
            e.preventDefault();
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            console.log('Switching from', currentTheme, 'to', newTheme);
            setTheme(newTheme);
        });
        
        console.log('Theme toggle initialized successfully');
        console.log('Button element:', themeToggle);
        console.log('Button computed style:', window.getComputedStyle(themeToggle));
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initThemeToggle);
    } else {
        initThemeToggle();
    }
})();

// Made with Bob
