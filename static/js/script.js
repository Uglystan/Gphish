function showpass() {
  var passwordField = document.getElementById("password");
  var checkbox = document.getElementById("custom-checkbox");

  if (checkbox.checked) {
      passwordField.type = "text";
  } else {
      passwordField.type = "password";
  }
}

function redirectToHome() {
  window.location.href = "https://gphish.onrender.com";
}

function fixoverride() {
  var input_element = document.querySelector("input");

  document.addEventListener("click", function () {
    input_element.setAttribute("value", input_element.value);
    document.getElementById("placeholder_").style.cssText = "font-size:12px;";
  });
}

document.addEventListener("DOMContentLoaded", function () {
  const emailInput = document.getElementById('email');

  checkInputValue(emailInput);

  emailInput.addEventListener('input', function () {
      checkInputValue(emailInput);
  });

  function checkInputValue(input) {
      if (input.value.trim() !== "") {
          input.classList.add('has-value');
      } else {
          input.classList.remove('has-value');
      }
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const passwordInput = document.getElementById('password');

  checkInputValue(passwordInput);

  passwordInput.addEventListener('input', function () {
      checkInputValue(passwordInput);
  });

  function checkInputValue(input) {
      if (input.value.trim() !== "") {
          input.classList.add('has-value');
      } else {
          input.classList.remove('has-value');
      }
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById('form');
  const emailInput = document.getElementById('email');
  const txtForm = document.getElementById('placeholder_');
  const errorMessage = document.getElementById('error-message');
  const link = document.getElementById('linkk');

  form.addEventListener('submit', function (e) {
      if (!emailInput.value || !validateEmail(emailInput.value)) {
          e.preventDefault();
          emailInput.style.borderColor = '#b3261e';
          txtForm.style.color = '#b3261e';
          errorMessage.style.display = 'block';
          link.style.paddingTop = "32px";
      }
  });

  function validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(String(email).toLowerCase());
  }
});