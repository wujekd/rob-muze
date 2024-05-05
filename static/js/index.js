console.log('Initial hideSplashScreen value:', localStorage.getItem('hideSplashScreen'));

if (!localStorage.getItem('hideSplashScreen')) {
    var loadingScreen = document.getElementById('loading-screen');
    loadingScreen.style.display = 'block';
    console.log('Splash screen is shown');

    console.log('Setting hideSplashScreen flag in local storage');
    localStorage.setItem('hideSplashScreen', 'true');
    console.log('hideSplashScreen flag set in local storage');
} else {
    console.log('Splash screen is not shown because hideSplashScreen flag is set in local storage');
}

console.log('Final hideSplashScreen value:', localStorage.getItem('hideSplashScreen'));

window.addEventListener('load', function() {
    var loadingScreen = document.getElementById('loading-screen');
    loadingScreen.style.display = 'none';
    console.log('Page finished loading, splash screen is hidden');
});


    window.addEventListener('load', function() {
        setTimeout(function() {
            document.body.classList.add('loaded');
        }, 650);  
    });
    
    window.onload = function() {
        var slideIndex = 0;
        var upperSlides = document.getElementsByClassName("slides");
        var lowerSlides = document.getElementsByClassName("slidesLower");
        var dots = document.getElementsByClassName('dot');
        var slideInterval;
    
        function showSlide(n){
            var i;
            for (i = 0; i < upperSlides.length; i++) {
                upperSlides[i].classList.remove("active-slide");
                lowerSlides[i].classList.remove("active-slide-lower");
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active-dot", "");
            }
            upperSlides[n].classList.add("active-slide");
            lowerSlides[n].classList.add("active-slide-lower");
            dots[n].className += " active-dot";
        }
    
        showSlide(slideIndex);
    
        function nextSlide() {
            slideIndex++;
            if (slideIndex >= upperSlides.length) {slideIndex = 0}
            showSlide(slideIndex);
        }
    
        // Delay 
        setTimeout(function() {
            slideInterval = setInterval(nextSlide, 5000);
        }, 40);
    
        for (let i = 0; i < dots.length; i++) {
            dots[i].addEventListener('click', function() {
                slideIndex = i;
                showSlide(i);
                clearInterval(slideInterval); // Clear the existing interval
                slideInterval = setInterval(nextSlide, 9700); // Start a new interval
                setTimeout(function() { // back to normal timing
                    clearInterval(slideInterval);
                    slideInterval = setInterval(nextSlide, 4600);
                }, 6000);
            });
        }
    }