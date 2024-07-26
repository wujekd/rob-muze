document.addEventListener('DOMContentLoaded', function() {

    // const backBtn = document.getElementById("back-btn");
    // const fwdBtn = document.getElementById("fwd-btn");
    // const progSlider = document.getElementById("progress");
    // const title = document.getElementById("title");
    // const author = document.getElementById("author");
    // const cover = document.getElementById("cover");
    // const vol = document.getElementById("volume");
    // const currTime = document.getElementById("current-time");
    // const fullTime = document.getElementById("duration");
    const playBtnMain = document.getElementById("play-btn");
    const audioSubmission = document.getElementById("audioAPI");
    const audioBacking = document.getElementById("audio-backing");
    var playButtonsUnlistened = document.querySelectorAll('.play-unlistened-btn');
    var playButtonsFavs = document.querySelectorAll(".play-fav-btn")


    // states
    let nowPlayingButton = null;
    let playing = false;
    let totalInSeconds = null;

    let volOffset = 1;
    let volValue = 1;


    function changeButtonText(button, newText) {
        const spanElement = button.querySelector('.btn-txt');

        if (spanElement) {
            spanElement.textContent = newText;
        }
    }
    

    function play(){
        if (playing == false) {
            audioBacking.play();
            audioSubmission.play();
            playing = true;
            changeButtonText(nowPlayingButton, 'stop')
            gui_transport_play(1);
            console.log('url: ', nowPlayingButton.getAttribute('data-audio-url'))
        } else {
            audioBacking.pause();
            audioSubmission.pause();
            playing = false;
            gui_transport_play(0);
            changeButtonText(nowPlayingButton, 'play')
        }   
    }

    playButtonsFavs.forEach(function(button) {
        const submissionUrl = button.getAttribute('data-audio-url');
        button.addEventListener('click', function() {
            if (nowPlayingButton !== this) {
                changeButtonText(nowPlayingButton, 'play');
                nowPlayingButton = button;
                audioSubmission.src = submissionUrl;
                playing = false;
                audioBacking.currentTime = 0;
                play();
            } else {
                play()
            }
        })
    })

    playButtonsUnlistened.forEach(function(button) {
        const submissionUrl = button.getAttribute('data-audio-url');
        button.addEventListener('click', function() {

            if(nowPlayingButton !== this) { //new button selected
                changeButtonText(nowPlayingButton, 'play');
                nowPlayingButton = button;
                audioSubmission.src = submissionUrl;
                playing = false;
                audioBacking.currentTime = 0;
                play();

            } else { //same button pressed again
                console.log('hi mom');
                play();
            }

        })
    })

    function gui_transport_play(x){
        if (x == 0){
            playBtnMain.textContent = "PLAY"
        } else if (x == 1) {
            playBtnMain.textContent = "STOP"
        }
    }



function initPlayer(){
    nowPlayingButton = playButtonsUnlistened[0];
    const submissionUrl = nowPlayingButton.getAttribute('data-audio-url');
    audioSubmission.url = submissionUrl;
}
initPlayer();

    playBtnMain.addEventListener('click', play);
    

});
