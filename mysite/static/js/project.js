/* Project specific Javascript goes here. */

document.addEventListener('DOMContentLoaded', () => {
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
