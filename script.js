let isLogin = true; // Track current mode

document.getElementById("toggle-link").addEventListener("click", function (e) {
  e.preventDefault();
  isLogin = !isLogin;

  document.getElementById("form-title").textContent = isLogin ? "Login" : "Sign Up";
  document.querySelector("button[type=submit]").textContent = isLogin ? "Login" : "Sign Up";
  document.getElementById("toggle-text").innerHTML = isLogin
    ? `Don't have an account? <a href="#" id="toggle-link">Sign Up</a>`
    : `Already have an account? <a href="#" id="toggle-link">Login</a>`;

  // Show email field only for signup
  document.getElementById("email").style.display = isLogin ? "none" : "block";
});

// Hide email on load
document.getElementById("email").style.display = "none";

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
