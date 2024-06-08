var originalContent = null;

    function showConfirmation() {
        var content = document.getElementById('dynamic');
        originalContent = content.innerHTML; 
        var height = content.offsetHeight;  
        content.style.opacity = '0';
        setTimeout(function() {
            content.style.display = 'flex'; 
            content.style.justifyContent = 'center';  
            content.style.alignItems = 'center';  
            content.innerHTML = '<p>Upewnij sie, ze masz stabilne polaczenie poniewaz domyslnie mozesz pobrac kazdy sampel tylko raz!</p>' +
            '<button id="countdownButton" style="width: 168px; opacity: 0.65; transition: opacity 0.45s ease-in-out" disabled class="btn-primary">5</button>' +
            '<button onclick="goBack()" class="btn-primary">Powrot</button>';
            content.style.minHeight = height + 'px';  
            content.style.opacity = '1';
    
           
            var countdown = 5;
            var countdownButton = document.getElementById('countdownButton');
            var countdownInterval = setInterval(function() {
                countdown--;
                if (countdown >= 1) {
                    countdownButton.style.opacity = '0.65';
                    countdownButton.innerText = countdown;
                } else {
                  
                    clearInterval(countdownInterval);
                    countdownButton.innerText = 'Pobierz!';
                    countdownButton.style.opacity = 1; 
                    countdownButton.disabled = false;
                    countdownButton.onclick = function() {
                        window.location.href = downloadUrl;
                    };
                }
            }, 1000);
        }, 500);  
    }

    function goBack() {
        var content = document.getElementById('dynamic');
        content.style.opacity = '0';
        setTimeout(function() {
            content.style.display = 'block';
            content.innerHTML = originalContent;
            content.style.opacity = '1';
        }, 500);
    }