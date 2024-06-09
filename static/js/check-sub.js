const volumeSlider = document.getElementById("id_volumeOffset");
const infoThing = document.getElementById("info");
const playBtn = document.getElementById("play");
const audioBacking = document.getElementById("backing");
const audioSub = document.getElementById("submitted");
const progSlider = document.getElementById("progress");
let playing = false;

const confirmBox = document.getElementById('confirm-box');
const confirmBtn = document.getElementById('confirm-btn');
const submitBtn = document.getElementById("submit");
const warning = document.getElementById("warning");
const cancel = document.getElementById("cancel");





confirmBtn.addEventListener("click", ()=>{
    boxHeight = confirmBox.offsetHeight;
    confirmBox.style.display = 'none'
    submitBtn.style.display = '';
    warning.style.display = '';
    warning.style.minHeight = boxHeight + 'px';
    confirmBtn.style.display = "none";
})

cancel.addEventListener("click", function(e){
    e.preventDefault();
    confirmBox.style.display = ''
    submitBtn.style.display = 'none';
    warning.style.display = 'none';
    confirmBtn.style.display = "";

})



function updateInfo(){
    infoThing.textContent = volumeSlider.value;
}
volumeSlider.addEventListener("input", updateInfo)






playBtn.addEventListener("click", function(){
    if (playing == false){
        playing = true;
        audioBacking.play();
        audioSub.play();
        playBtn.textContent = "STOP";
    } else if (playing == true) {
        playing = false;
        audioBacking.pause();
        audioSub.pause();
        playBtn.textContent = "PLAY"
    }
})


audioBacking.addEventListener("timeupdate", updateProgress);

function updateProgress(e) {
    const {duration, currentTime} = e.srcElement;
    const progress = (currentTime / duration);
    progSlider.value = progress;
}

progSlider.addEventListener("input", ()=>{
        
    duration = audioBacking.duration;
    const timeVal = duration * progSlider.value;
    audioBacking.currentTime = timeVal
    audioSub.currentTime = timeVal
})


const audioContext = new AudioContext();
const subGain = audioContext.createGain();
const source = audioContext.createMediaElementSource(audioSub);
source.connect(subGain);
subGain.connect(audioContext.destination);

volumeSlider.addEventListener('input', function(){
    subGain.gain.value = volumeSlider.value;
})


function initiateSlider(){
    subGain.gain.value = parseFloat(volumeOffsetFloat);
    volumeSlider.value = volumeOffsetFloat;
}
initiateSlider()

