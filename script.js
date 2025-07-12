document.getElementById("auth-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const email = document.getElementById("email").value;

  const endpoint = isLogin ? "login.php" : "signup.php";

  const response = await fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: username=${username}&password=${password}&email=${email}
  });

  const data = await response.json();
  alert(data.message);
});