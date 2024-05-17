function updateCountdownTimer() {
    var days = Math.floor(timeRemaining / (3600 * 24));
    var hours = Math.floor((timeRemaining % (3600 * 24)) / 3600);
    var minutes = Math.floor((timeRemaining % 3600) / 60);
    var seconds = Math.floor(timeRemaining % 60);

    document.getElementById('countdown-timer').textContent = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

    if (timeRemaining <= 0) {
        clearInterval(countdownTimer);
        document.getElementById('countdown-timer').textContent = "Submission closed";
    }
}

updateCountdownTimer();

var countdownTimer = setInterval(function() {
timeRemaining--;
    updateCountdownTimer();
}, 1000);
