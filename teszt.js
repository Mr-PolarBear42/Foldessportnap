// script.js

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    const loginForm = document.getElementById('teszt');

    // Add an event listener for the form submission
    loginForm.addEventListener('submit', function(event) {
        // Prevent the form from submitting the traditional way
        event.preventDefault();

        // Access the input values
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Do something with the values (e.g., log them to the console)
        console.log('Username:', username);
        console.log('Password:', password);

        // You can also perform validation or send the data to a server here
    });
});