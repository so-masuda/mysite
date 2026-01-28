/* Project specific Javascript goes here. */

document.addEventListener('DOMContentLoaded', () => {
  const togglePassword = document.querySelector('#togglePassword');
  const password = document.querySelector('#id_password');

  if (togglePassword) {
    togglePassword.addEventListener('click', function (e) {
      // toggle the type attribute
      const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
      password.setAttribute('type', type);
      // toggle the button text
      this.textContent = type === 'password' ? 'Show' : 'Hide';
      // toggle the aria-label
      this.setAttribute('aria-label', type === 'password' ? 'Show password' : 'Hide password');
      // toggle the aria-pressed state
      this.setAttribute('aria-pressed', type !== 'password');
    });
  }

  const forms = document.querySelectorAll('form');

  forms.forEach(form => {
    form.addEventListener('submit', () => {
      const submitButton = form.querySelector('button[type="submit"][data-on-click-disable]');

      if (submitButton) {
        submitButton.disabled = true;

        const spinner = submitButton.querySelector('.spinner');
        const buttonLabel = submitButton.querySelector('.button-label');

        if (spinner && buttonLabel) {
          spinner.style.display = 'inline-block';
          buttonLabel.style.display = 'none';
        }
      }
    });
  });
});
