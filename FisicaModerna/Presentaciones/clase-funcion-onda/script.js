let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const totalSlides = slides.length;

function showSlide(index) {
    slides.forEach((slide, i) => {
        if (i === index) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });
    updateNavButtons();
}

function changeSlide(n) {
    currentSlide += n;
    if (currentSlide < 0) {
        currentSlide = 0;
    }
    if (currentSlide >= totalSlides) {
        currentSlide = totalSlides - 1;
    }
    showSlide(currentSlide);
}

function updateNavButtons() {
    if (currentSlide === 0) {
        prevBtn.disabled = true;
    } else {
        prevBtn.disabled = false;
    }

    if (currentSlide === totalSlides - 1) {
        nextBtn.disabled = true;
    } else {
        nextBtn.disabled = false;
    }
}

// Inicializar la primera diapositiva
document.addEventListener('DOMContentLoaded', () => {
    if (slides.length > 0) {
        showSlide(currentSlide);
    } else {
        console.error("No slides found!");
        prevBtn.style.display = 'none';
        nextBtn.style.display = 'none';
    }
});