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
    var playButtonsListened = document.querySelectorAll(".play-listened-btn");
    var playButtonsFavs = document.querySelectorAll(".play-fav-btn");
    let addFavActiveBtns = document.querySelectorAll(".add-fav-btn");
    let favouritesSection = document.getElementById("favourites");



    // states
    let nowPlayingButton = null;
    let nowPlayingItem = null;
    let playing = false;
    let totalInSeconds = null;
    let playing_unlistened = true;

    let total_listened = 0;
    let listen_started;

    let volOffset = 1;
    let volValue = 1;


    function changeButtonText(button, newText) {
        const spanElement = button.querySelector('.btn-txt');

        if (spanElement) {
            spanElement.textContent = newText;
        }
    };
    

    function play(){
        if (playing == false) {
            audioBacking.play();
            audioSubmission.play();
            playing = true;
            changeButtonText(nowPlayingButton, 'stop')
            gui_transport_play(1);
            console.log('url: ', nowPlayingButton.getAttribute('data-audio-url'))
            listen_started = Date.now()
        } else {
            audioBacking.pause();
            audioSubmission.pause();
            playing = false;
            gui_transport_play(0);
            changeButtonText(nowPlayingButton, 'play')
            total_listened += Date.now() - listen_started;
            listen_started = null;
            console.log('total_listened:' + total_listened);
        }   
    }


    addFavActiveBtns.forEach(function(button){
        button.addEventListener('click', function() {
            const parent = button.parentElement;
            const playBtn = parent.querySelector(".play-listened-btn");
            addFavourite(button, playBtn);
        })
    })


const favEmptyDivCopy = document.getElementById('fav-empty')

function createListened(playBtn){
    const container = document.createElement('div');
    container.classList.add("response-listened");
    const hiddenP = document.createElement('p');
    hiddenP.className = 'absolute';
    hiddenP.style.left = '4px';
    hiddenP.style.display = 'none';
    hiddenP.textContent = 'o';
    sub_id = playBtn.getAttribute("data-sub-id")
    let addFavBtn = createAddToFavBtn(sub_id);
    addFavBtn.addEventListener("click", function() {
        addFavourite(addFavBtn, playBtn)
    })

    container.appendChild(playBtn);
    container.appendChild(hiddenP);
    container.appendChild(addFavBtn);

    return container;

}
function createAddToFavBtn(subId) {
    // Create a new button element
    let button = document.createElement("button");

    // Set the button's attributes
    button.setAttribute("data-select-id", subId);
    button.classList.add("addFav", "add-fav-btn");

    // Set the button's text content
    button.textContent = "Add to favourites";

    return button;
}


function removeFavourite(x) {
    const fav_item = x.parentNode;
    let favourites = fav_item.parentNode;
    const playBtn = fav_item.querySelector('.play-fav-btn');
    const sub_id = playBtn.getAttribute("data-sub-id");
    playBtn.classList.remove("play-fav-btn");
    playBtn.classList.add("play-listened-btn");

    axios.post('/collabs/del-fav/', {
        submission_id : sub_id
    }, {
        headers: {'X-CSRFToken' : csrftoken }
    })
    .then(response => {
        if (response.status == 200){
            console.log('delete success.')
        }
        else {
            console.log("not created: ", response.status);
        }
    })
    .catch(error => {
        console.log("cholibka no nie dziala: ", error)
    })
    

    console.log("fav item ", fav_item);
    fav_item.classList.add("fade-out");

    const responses = document.querySelector('.responses');
    const new_response = createListened(playBtn);
    new_response.offsetHeight;


    const oldFlexItemsInfo = getFlexItemsInfo(favourites);

    // Force reflow to ensure transition works
    responses.appendChild(new_response);
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            new_response.classList.add("show");
        });
    });


    fav_item.addEventListener('transitionend', function() {
        fav_item.remove();
        const newFlexItemsInfo = getFlexItemsInfo(favourites);
        animateFlexItems(oldFlexItemsInfo, newFlexItemsInfo);
    });


    
}


function addFavourite(button, playBtn){ //button here is the addFavBtn
    
    if (!playBtn){
        parent = button.parentNode;
        playBtn = parent.querySelector(".play-unlistened-button");
    }
    console.log("button: ", button);
    console.log("playBtn: ", playBtn);

    emptyFav = document.querySelector(".fav-empty")
    const emptyFavCopy = emptyFav.cloneNode(true);
    favEmptyActivate(emptyFav);
    sub_id = button.getAttribute("data-select-id");

    axios.post(add_fav_url,{
        submission_id : sub_id
    }, {
        headers: {'X-CSRFToken' : csrftoken }
    })
    .then(response => {
        if (response.status == 201){
            sub_item = button.parentNode;
            // console.log(sub_item)
            sub_play = playBtn
            sub_play.classList.remove("play-listened-btn");
            sub_play.classList.add("play-fav-btn");
            emptyFav.innerHTML = "";
            emptyFav.appendChild(sub_play);
            emptyFav.classList.remove("fav-empty")
            emptyFav.classList.add("fav-selected", "relative", "fav-selected")
            emptyFav.insertBefore(createXfav(), emptyFav.firstChild)

            var x = emptyFav.querySelector(".x")
            x.addEventListener('click', function(){
                removeFavourite(x)
            })
            
            let favs = emptyFav.parentNode;
            let subs = sub_item.parentNode;
            
            console.log("add favourite SUCCESS")
            sub_item.classList.remove("show")
            sub_item.classList.add("fade-out");
            sub_item.addEventListener('transitionend', function(){
                const oldFlexItemsInfo = getFlexItemsInfo(subs);
                sub_item.remove();
                const newFlexItemsInfo = getFlexItemsInfo(subs);
                animateFlexItems(oldFlexItemsInfo, newFlexItemsInfo);
                favs.appendChild(emptyFavCopy);
            })
            
        } else {
            console.log('not created ', response.status);
        }
    })
    .catch(error => {
        console.log("no i chuj, nie dziala ", error)
    })
}





function mark_listened(button, item){
    item.querySelector('p').style.display = "block"
        const submissionId = button.getAttribute("data-sub-id");
        

        axios.post(markListenedUrl, {
            submission_id : submissionId
        }, {
            headers: {'X-CSRFToken' : csrftoken }
        })
        .then(response => {
            if (response.status == 201){
                console.log("POST mark as listened 200")
                //activate addFav button
                addFavBtn = item.querySelector(".addFavUnlistened")
                addFavBtn.disabled = false;
                addFavBtn.classList.remove('add-fav-btn-dis', 'addFavUnlistened')
                addFavBtn.classList.add("add-fav-btn", "addFav");
                // addFavBtn.addEventListener("click", function() {
                //         addFavourite(addFavBtn)
                // })
                addFavBtn.addEventListener('click', function() {
                    const parent = button.parentElement;
                    const playBtn = parent.querySelector("button");
                    addFavourite(addFavBtn, playBtn);
                })
            } else {
                console.log("not created - ", response.status)
            }
        })
        .catch(error => {
            console.error("shieeeeet ", error)
        })
}

playButtonsListened.forEach(function(button) {
    const submissionUrl = button.getAttribute('data-audio-url');
    // if (nowPlayingButton == null) {
    //     nowPlayingButton = button
    // } 
    button.addEventListener('click', function() {
        playing_unlistened = false;
        if(nowPlayingButton !== this) { //new button selected
            listened_POST = false;
            if (nowPlayingButton){
                changeButtonText(nowPlayingButton, 'play');
            }
            nowPlayingButton = button;
            nowPlayingItem = nowPlayingButton.parentNode;
            audioSubmission.src = submissionUrl;
            playing = false;
            audioBacking.currentTime = 0;
            total_listened = 0;
            play();

        } else { //same button pressed again
            console.log('hi mom, same button pressed again');
            play();
        }
    })
})


    playButtonsUnlistened.forEach(function(button) {
        const submissionUrl = button.getAttribute('data-audio-url');

        // if (nowPlayingButton == null) {
        //     nowPlayingButton = button
        // } 

        button.addEventListener('click', function() {
            playing_unlistened = true;
            if(nowPlayingButton !== this) { //new button selected
                listened_POST = false;
                if (nowPlayingButton){
                    changeButtonText(nowPlayingButton, 'play');
                    nowPlayingItem.classList.remove('border-2');
                }
                nowPlayingButton = button;
                
                nowPlayingItem = nowPlayingButton.parentNode;
                nowPlayingItem.classList.add("border-2");
                audioSubmission.src = submissionUrl;
                playing = false;
                audioBacking.currentTime = 0;
                total_listened = 0;
                play();

            } else { //same button pressed again
                console.log('hi mom');
                play();
            }

        })
    })

    playButtonsFavs.forEach(function(button) {
        const submissionUrl = button.getAttribute('data-audio-url');
        const favItem = button.parentElement;
        var x = favItem.querySelector(".x")
        x.addEventListener('click', function(){
            removeFavourite(x)
        })
        button.addEventListener('click', function() {
            if (nowPlayingButton !== this) {
                changeButtonText(nowPlayingButton, 'play');
                nowPlayingButton = button;
                audioSubmission.src = submissionUrl;
                playing = false;
                playing_unlistened = false;
                audioBacking.currentTime = 0;
                play();
            } else {
                play()
            }
        
        });
    });



    let lastUpdated;
    let listened_POST = false;
    audioBacking.addEventListener('timeupdate', updateProgress);
    function updateProgress(e) {
        
        const {duration, currentTime} = e.srcElement;
        // const progress = (currentTime / duration);
        const progress = (currentTime / duration) || 0; //this shit was making the prog bar jump in the middle oh my god
        // progSlider.value = progress;
        // updateSlider(progSlider);

        // const percentValue = progress * 100;
        // currentPlayingButton.querySelector('div').style.width = `${percentValue}%`


        // const secNow = Math.floor(currentTime % 60);
        
        // if (secNow !== lastUpdated){
        //     lastUpdated = secNow
        //     const minNow = Math.floor(currentTime / 60);
        //     const formattedSec = secNow < 10 ? '0' + secNow : secNow;
        //     currTime.textContent = `${minNow}:${formattedSec}`;
        // }

        if (progress >= 0.35 && listened_POST == false && playing_unlistened == true){
            //loading in add to fav button
            listened_POST = true;
            mark_listened(nowPlayingButton, nowPlayingItem)
        }
    }




    // gui functions

  
function createXfav(){
    var x = document.createElement('button');
x.className = 'absolute';
x.style.top = '-5px';
x.style.right = '-1px';
x.classList.add("x")
x.innerText = 'X';
return x;
}


// function initPlayer(){
//     if (playButtonsUnlistened) {
//         nowPlayingButton = playButtonsUnlistened[0];
//     } else if (playButtonsListened) {
//         nowPlayingButton = playButtonsListened[0];
//     }
//     console.log(playButtonsUnlistened)
//     console.log(nowPlayingButton)
//     nowPlayingItem = nowPlayingButton.parentNode
//     const submissionUrl = nowPlayingButton.getAttribute('data-audio-url');
//     audioSubmission.url = submissionUrl;
// }
// initPlayer();

function gui_transport_play(x){
    if (x == 0){
        playBtnMain.textContent = "PLAY"
    } else if (x == 1) {
        playBtnMain.textContent = "STOP"
    }
}


    playBtnMain.addEventListener('click', play);
    


function favEmptyActivate(node) {
    
    node.innerHTML = "Loading";

}

let testBtn = document.getElementById("test-btn")




// ANIMATION FUNCTIONS BY Maurici Abad https://codepen.io/MauriciAbad/pen/yLbrpey
function getFlexItemsInfo(container) {
    return Array.from(container.children).map((item) => {
      const rect = item.getBoundingClientRect();
      return {
        element: item,
        x: rect.left,
        y: rect.top,
        width: rect.right - rect.left,
        height: rect.bottom - rect.top,
      };
    });
  }

  function animateFlexItems(oldFlexItemsInfo, newFlexItemsInfo) {
    for (const newFlexItemInfo of newFlexItemsInfo) {
      const oldFlexItemInfo = oldFlexItemsInfo.find(
        (itemInfo) => itemInfo.element === newFlexItemInfo.element
      );
  
      const translateX = oldFlexItemInfo.x - newFlexItemInfo.x;
      const translateY = oldFlexItemInfo.y - newFlexItemInfo.y;
      const scaleX = oldFlexItemInfo.width / newFlexItemInfo.width;
      const scaleY = oldFlexItemInfo.height / newFlexItemInfo.height;
  
      newFlexItemInfo.element.animate(
        [
          {
            transform: `translate(${translateX}px, ${translateY}px) scale(${scaleX}, ${scaleY})`,
          },
          { transform: 'none' },
        ],
        {
          duration: 250,
          easing: 'ease-out',
        }
      );
    }
  }
});
