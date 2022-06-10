// Simple script to make dropdown button functional
var dropdown = document.querySelector('.dropdown');
console.log(dropdown);
dropdown.addEventListener('click', function(event) {
    event.stopPropagation();
    dropdown.classList.toggle('is-active');
});
