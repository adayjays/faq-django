// JavaScript for the accordion
const accordionToggles = document.querySelectorAll('.accordion-toggle');

function toggleAccordion() {
  const targetContent = document.getElementById(this.dataset.target);
  
  if (targetContent.style.display === 'block') {
    targetContent.style.display = 'none';
    this.classList.remove('active');
  } else {
    targetContent.style.display = 'block';
    this.classList.add('active');
  }
}

accordionToggles.forEach((toggle) => {
  toggle.addEventListener('click', toggleAccordion);
});
