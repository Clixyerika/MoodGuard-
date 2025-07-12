let isLogin = true; // Track current mode

// Setup toggle once
const toggleLink = document.getElementById("toggle-link");
const toggleText = document.getElementById("toggle-text");
const emailInput = document.getElementById("email");
const formTitle = document.getElementById("form-title");
const submitButton = document.querySelector("button[type=submit]");

// Hide email on load
emailInput.style.display = "none";

toggleLink.addEventListener("click", function (e) {
  e.preventDefault();
  isLogin = !isLogin;

  formTitle.textContent = isLogin ? "Login" : "Sign Up";
  submitButton.textContent = isLogin ? "Login" : "Sign Up";
  toggleLink.textContent = isLogin ? "Sign Up" : "Login";
  // Change the text node before the link
  toggleText.childNodes[0].textContent = isLogin
    ? "Don't have an account? "
    : "Already have an account? ";
  emailInput.style.display = isLogin ? "none" : "block";
});

document.getElementById("auth-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const email = document.getElementById("email").value;

  const endpoint = isLogin ? "login.php" : "signup.php";
  let body = `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`;
  if (!isLogin) {
    body += `&email=${encodeURIComponent(email)}`;
  }

  const response = await fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: body
  });

  const data = await response.json();
  alert(data.message);
});
