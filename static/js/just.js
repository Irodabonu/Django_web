// JavaScript to handle automatic sliding
let currentIndex = 0;
const slides = document.querySelectorAll('.slide'); // Select all slides

function showNextSlide() {
    // Hide the current slide
    slides[currentIndex].classList.remove('active');
    slides[currentIndex].classList.add('hidden');

    // Move to the next slide
    currentIndex = (currentIndex + 1) % slides.length;

    // Show the next slide
    slides[currentIndex].classList.add('active');
    slides[currentIndex].classList.remove('hidden');
}

// Initialize first slide as visible
slides[currentIndex].classList.add('active');

// Change slide every 3 seconds (3000 milliseconds)
setInterval(showNextSlide, 3000);
