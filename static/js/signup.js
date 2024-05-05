

var originalContent = null;

function showConfirmation() {
    var content = document.getElementById('dyn');
    originalContent = content.innerHTML; 
    var height = content.offsetHeight;  
    content.style.opacity = '0';
    setTimeout(function() {
        content.style.display = 'flex'; 
        content.style.justifyContent = 'flex-start';
        content.style.alignItems = 'flex-start';
        content.innerHTML = policy + '<button onclick="goBack()" class="btn-primary-light">Powrot</button>';
        
        content.style.flexDirection = 'column';
        content.style.overflow = 'auto';
        content.style.maxHeight = height + 'px';  
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
    var content = document.getElementById('dyn');
    content.style.transition = 'opacity 0.4s ease-in-out'; 
    content.style.opacity = '0';
    setTimeout(function() {
        content.style.display = 'block';  // restore the original display value
        content.innerHTML = originalContent;  // restore the original content of the div
        content.style.opacity = '1';
    }, 500);
}



var checkboxDiv = document.querySelector('.checkbox-div');

document.getElementById('privacyPolicyCheckbox').addEventListener('invalid', function() {
    checkboxDiv.style.backgroundColor = 'red';
    this.setCustomValidity('{% trans "Musisz zgodzic sie na warunki uzywania serwisu zeby zarejestrowac konto." %}');
});

document.getElementById('privacyPolicyCheckbox').addEventListener('change', function() {
    console.log('changed');
    checkboxDiv.style.backgroundColor = '';
    this.setCustomValidity('');
});
