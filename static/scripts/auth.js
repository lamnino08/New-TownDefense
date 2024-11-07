// auth.js

document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const errorMessage = document.getElementById("error-message");

    loginForm.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        try {
            // Send the login data to the server
            const response = await fetch("/auth/api/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password }),
            });

            // Parse the JSON response
            const result = await response.json();

            if (response.ok) {
                errorMessage.style.display = "none";
                const firstPage = result.firstPage || "/";
                window.location.assign(firstPage);
            } else {
                errorMessage.textContent = result.message || "Login failed. Please check your credentials.";
                errorMessage.style.display = "block";
            }
        } catch (error) {
            console.error("Error during login:", error);
            errorMessage.textContent = "An error occurred. Please try again later.";
            errorMessage.style.display = "block";
        }
    });
});
