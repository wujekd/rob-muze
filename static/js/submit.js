// document.addEventListener('DOMContentLoaded', () => {
//     const userAudioInput = document.getElementById('userAudio');
//     const responseAudio = document.getElementById('response');
//     const backingAudio = document.getElementById("backing");
//     const playButton = document.getElementById("play");
//     const progSlider = document.getElementById("progress");
//     let playing = false;
//     const volumeContainer = document.getElementById("volume_container")
//     const vol = document.getElementById("volume");
//     const volumeOffsetField = document.getElementById("volumeOffset");
//     const responseBox = document.getElementById("respBox");

//     let fileLoaded = false
//     const loadingContainer = document.getElementById("loadingContainer");
//     const progressBar = document.getElementById("loadingBar");
//     const audioContext = new AudioContext();
//     const gainNode = audioContext.createGain();
//     const source = audioContext.createMediaElementSource(responseAudio);
//     source.connect(gainNode);
//     gainNode.connect(audioContext.destination);

//     const submitBtn = document.getElementById("submit-btn");

// //  FORM SUBMISSION 
//     const submissionForm = document.getElementById("submissionForm");
//     const collabId = submissionForm.getAttribute("data-collab-id");

//     submissionForm.addEventListener("submit", async (event) => {
//         event.preventDefault();
//         submitBtn.disabled = true;
//         const formData = new FormData(submissionForm);
//         const height = volumeContainer.offsetHeight;
//         loadingContainer.style.minHeight = height + 'px';
//         loadingContainer.style.display = 'block';
//         volumeContainer.style.display = "none";


    
//         console.log(`collabId: ${collabId}`); 
        
//         // const fullUrl = `/collabs/${collabId}/przeslij`; // Construct the full URL
//         // let uploadStarted = false;
//         // const startTime = Date.now();

    
//     //     try {
//     //         const response = await axios.post(fullUrl, formData, {
//     //             onUploadProgress: function(progressEvent) {
                    
//     //                 uploadStarted = true;

//     //                 if (progressEvent.lengthComputable) {
//     //                     const percentComplete = (progressEvent.loaded / progressEvent.total) * 100;
//     //                     updateProgressBar(percentComplete);
//     //                     submitBtn.textContent = `${Math.round(percentComplete)}%`;
//     //                 }
//     //             }
//     //         });
    
//     //         if (response.status === 200) {
//     //             submitBtn.textContent = "SUCCESS! Click to continue...";
//     //             updateProgressBar(100);
//     //             submitBtn.addEventListener("click", (e) => {
//     //                 e.preventDefault();
//     //                 window.location.href = successUrl;
                    
//     //             });
//     //             submitBtn.disabled = false;
//     //         } else {
//     //             alert("Submission failed!");
//     //         }
//     //     } catch (error) {
//     //         console.error('Error:', error);
//     //         alert("Submission failed!");
//     //     }

//     //     setTimeout(()=> {
//     //         if (!uploadStarted) {
//     //             console.log("simulated triggered")
//     //             const duration = Date.now() - startTime;
//     //             let simulated = 0;

//     //             const interval = setInterval(()=> {
//     //                 simulated += 10;
//     //                 updateProgressBar(simulated);
//     //                 submitBtn.textContent = `${simulated}`;
//     //                 if (simulated >= 100) {
//     //                     clearInterval(interval)
//     //                 }
//     //             }, Math.min(100, duration / 10));
//     //         }
//     //     }, 100);
//     // });



//     document.getElementById('yourForm').addEventListener('submit', async function(event) {
//         event.preventDefault();
    
//         const formData = new FormData(this);
//         const fullUrl = `/collabs/${collabId}/przeslij`; // Construct the full URL
    
//         let uploadStarted = false;
//         let uploadFinished = false;
//         const startTime = Date.now();
    
//         try {
//             const response = await axios.post(fullUrl, formData, {
//                 onUploadProgress: function(progressEvent) {
//                     uploadStarted = true;
    
//                     if (progressEvent.lengthComputable) {
//                         const percentComplete = (progressEvent.loaded / progressEvent.total) * 100;
//                         updateProgressBar(percentComplete);
//                         submitBtn.textContent = `${Math.round(percentComplete)}%`;
//                         console.log(`Upload Progress: ${percentComplete}%`);
//                     }
//                 }
//             });
    
//             if (response.status === 200) {
//                 submitBtn.textContent = "SUCCESS! Click to continue...";
//                 updateProgressBar(100);
//                 submitBtn.addEventListener("click", (e) => {
//                     e.preventDefault();
//                     window.location.href = successUrl;
//                 });
//                 submitBtn.disabled = false;
//                 uploadFinished = true;
//             } else {
//                 alert("Submission failed!");
//             }
//         } catch (error) {
//             console.error('Error:', error);
//             alert("Submission failed!");
//         }
    
//         // Simulate progress for quick uploads
//         setTimeout(() => {
//             if (!uploadStarted) {
//                 console.log("Simulation triggered");
//                 const duration = Date.now() - startTime;
//                 let simulatedProgress = 0;
    
//                 const interval = setInterval(() => {
//                     simulatedProgress += 10;
//                     updateProgressBar(simulatedProgress);
//                     submitBtn.textContent = `${simulatedProgress}%`;
//                     if (simulatedProgress >= 100 || uploadFinished) {
//                         clearInterval(interval);
//                         if (uploadFinished) {
//                             updateProgressBar(100);
//                             submitBtn.textContent = "SUCCESS! Click to continue...";
//                         }
//                     }
//                 }, Math.min(100, duration / 10)); // Adjust interval based on upload speed
//             }
//         }, 100);
//     });
    
//     // function updateProgressBar(percent) {
//     //     const progressBar = document.getElementById('progressBar');
//     //     progressBar.style.width = percent + '%';
//     //     progressBar.textContent = Math.round(percent) + '%';
//     // }
    


//     function updateProgressBar(percent) {
//         loadingBar.style.width = percent + "%";

//     }


//     vol.addEventListener("input", function() {
//         gainNode.gain.value = vol.value;
//         volumeOffsetField.value = vol.value;
//     })



//     playButton.addEventListener("click", (e) => {

//         e.preventDefault();
//         if (fileLoaded){
//             if (playing) {
//                 responseAudio.pause();
//                 backingAudio.pause();
//                 playButton.textContent = "PLAY";
//                 playing = false;
//             } else {
//                 responseAudio.play();
//                 backingAudio.play();
//                 playButton.textContent = "PAUSE";
//                 playing = true;
//             }
//         }
//     });




//     userAudioInput.addEventListener('change', function(event) {
//         const file = event.target.files[0];
//         if (file) {
//             const objectURL = URL.createObjectURL(file);
//             responseAudio.src = objectURL;
//             responseAudio.load();
//             backingAudio.currentTime = 0;
//             progSlider.value = 0;
//             fileLoaded = true;
//             submitBtn.style.backgroundColor = 'green'


//         }
//     });



//     responseAudio.addEventListener('loadedmetadata', () => {
//         console.log('Metadata loaded:');
//         console.log('Duration:', responseAudio.duration);

//         submitBtn.textContent = "SUBMIT"
//         submitBtn.classList.add("bg-green-900")
//         submitBtn.classList.add("hover:bg-green-800")
//         playButton.textContent = "PLAY";

//         responseAudio.addEventListener('error', (e) => {
//             console.error('Error loading audio:', e);
//         });
    

//     });

    


//     backingAudio.addEventListener('timeupdate', updateProgress);
//     function updateProgress(e) {
//         const { duration, currentTime } = e.srcElement;
//         const progress = (currentTime / duration) || 0;
//         progSlider.value = progress;

//         const percentValue = progress * 100;
//     }

//     progSlider.addEventListener("input", () => {
//         const duration = backingAudio.duration;
//         const timeVal = duration * progSlider.value;
//         responseAudio.currentTime = timeVal;
//         backingAudio.currentTime = timeVal;
//     });
// });


document.addEventListener('DOMContentLoaded', () => {
    const userAudioInput = document.getElementById('userAudio');
    const responseAudio = document.getElementById('response');
    const backingAudio = document.getElementById('backing');
    const playButton = document.getElementById('play');
    const progSlider = document.getElementById('progress');
    let playing = false;
    const volumeContainer = document.getElementById('volume_container');
    const vol = document.getElementById('volume');
    const volumeOffsetField = document.getElementById('volumeOffset');
    const responseBox = document.getElementById('respBox');

    let fileLoaded = false;
    const loadingContainer = document.getElementById('loadingContainer');
    const progressBar = document.getElementById('loadingBar');
    const audioContext = new AudioContext();
    const gainNode = audioContext.createGain();
    const source = audioContext.createMediaElementSource(responseAudio);
    source.connect(gainNode);
    gainNode.connect(audioContext.destination);

    const submitBtn = document.getElementById('submit-btn');

    // FORM SUBMISSION
    const submissionForm = document.getElementById('submissionForm');
    const collabId = submissionForm.getAttribute('data-collab-id');

    submissionForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        submitBtn.disabled = true;
        const formData = new FormData(submissionForm);
        const height = volumeContainer.offsetHeight;
        loadingContainer.style.minHeight = height + 'px';
        loadingContainer.style.display = 'block';
        volumeContainer.style.display = 'none';

        const fullUrl = `/collabs/${collabId}/przeslij`; // Construct the full URL
        let uploadStarted = false;
        let uploadFinished = false;
        const startTime = Date.now();

        try {
            const response = await axios.post(fullUrl, formData, {
                onUploadProgress: function(progressEvent) {
                    uploadStarted = true;

                    if (progressEvent.lengthComputable) {
                        const percentComplete = (progressEvent.loaded / progressEvent.total) * 100;
                        updateProgressBar(percentComplete);
                        submitBtn.textContent = `${Math.round(percentComplete)}%`;
                        console.log(`Upload Progress: ${percentComplete}%`);
                    }
                }
            });

            if (response.status === 200) {
                submitBtn.textContent = 'SUCCESS! Click to continue...';
                updateProgressBar(100);
                submitBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    window.location.href = successUrl; // Make sure successUrl is defined
                });
                submitBtn.disabled = false;
                uploadFinished = true;
            } else {
                alert('Submission failed!');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Submission failed!');
        }

        // Simulate progress for quick uploads
        setTimeout(() => {
            if (!uploadStarted) {
                console.log('Simulation triggered');
                const duration = Date.now() - startTime;
                let simulatedProgress = 0;

                const interval = setInterval(() => {
                    simulatedProgress += 10;
                    updateProgressBar(simulatedProgress);
                    submitBtn.textContent = `${simulatedProgress}%`;
                    if (simulatedProgress >= 100 || uploadFinished) {
                        clearInterval(interval);
                        if (uploadFinished) {
                            updateProgressBar(100);
                            submitBtn.textContent = 'SUCCESS! Click to continue...';
                        }
                    }
                }, Math.min(100, duration / 10)); // Adjust interval based on upload speed
            }
        }, 100);
    });

    function updateProgressBar(percent) {
        progressBar.style.width = percent + '%';
    }

    vol.addEventListener('input', function() {
        gainNode.gain.value = vol.value;
        volumeOffsetField.value = vol.value;
    });

    playButton.addEventListener('click', (e) => {
        e.preventDefault();
        if (fileLoaded) {
            if (playing) {
                responseAudio.pause();
                backingAudio.pause();
                playButton.textContent = 'PLAY';
                playing = false;
            } else {
                responseAudio.play();
                backingAudio.play();
                playButton.textContent = 'PAUSE';
                playing = true;
            }
        }
    });

    userAudioInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const objectURL = URL.createObjectURL(file);
            responseAudio.src = objectURL;
            responseAudio.load();
            backingAudio.currentTime = 0;
            progSlider.value = 0;
            fileLoaded = true;
            submitBtn.style.backgroundColor = 'green';
        }
    });

    responseAudio.addEventListener('loadedmetadata', () => {
        console.log('Metadata loaded:');
        console.log('Duration:', responseAudio.duration);

        submitBtn.textContent = 'SUBMIT';
        submitBtn.classList.add('bg-green-900');
        submitBtn.classList.add('hover:bg-green-800');
        playButton.textContent = 'PLAY';

        responseAudio.addEventListener('error', (e) => {
            console.error('Error loading audio:', e);
        });
    });

    backingAudio.addEventListener('timeupdate', updateProgress);

    function updateProgress(e) {
        const { duration, currentTime } = e.srcElement;
        const progress = (currentTime / duration) || 0;
        progSlider.value = progress;
    }

    progSlider.addEventListener('input', () => {
        const duration = backingAudio.duration;
        const timeVal = duration * progSlider.value;
        responseAudio.currentTime = timeVal;
        backingAudio.currentTime = timeVal;
    });
});
