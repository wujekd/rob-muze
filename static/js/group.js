document.addEventListener("DOMContentLoaded", ()=> {

    const createInvitationButton = document.querySelector('.invitations button');
    const invitationsDiv = document.querySelector('.invitations');



  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// const csrftoken = getCookie('csrftoken');

document.getElementById('joinGroupButton').addEventListener('click', function() {
    axios.post(joinGroupUrl, {}, {
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(function(response) {
        document.getElementById('responseMessage').innerText = response.data.message;
    })
    .catch(function(error) {
        console.error(error);
        document.getElementById('responseMessage').innerText = 'An error occurred.';
    });
});



createInvitationButton.addEventListener('click', function() {
    axios.post(createInvitationUrl, {}, {
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(function(response) {
        console.log('Full response:', response); // Log the full response for debugging
    
        if (response.data.token) {
            const invitationLink = document.createElement('p');
            invitationLink.textContent = `Invitation Link: ${response.data.token}`;
            invitationsDiv.appendChild(invitationLink);
        } else {
            console.error(response.data.message);
        }
    })
    .catch(function(error) {
        console.error('An error occurred:', error);
    });
});


})