function showpass() {
  var passwordField = document.getElementById("password");
  var checkbox = document.getElementById("custom-checkbox");

  // Si la case est cochée, on affiche le mot de passe en clair
  if (checkbox.checked) {
      passwordField.type = "text";
  } else {
      // Sinon, on le masque
      passwordField.type = "password";
  }
}

function redirectToHome() {
  // Rediriger vers localhost:8000
  window.location.href = "http://localhost:8000";
}

function fixoverride() {
  var input_element = document.querySelector("input");

  document.addEventListener("click", function () {
    input_element.setAttribute("value", input_element.value);
    document.getElementById("placeholder_").style.cssText = "font-size:12px;";
  });
}
