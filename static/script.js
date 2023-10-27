const chatForm = document.querySelector('#chat-form');
const chatInput = document.querySelector('#userQuery');

chatForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const userMessage = chatInput.value;
    chatInput.value = '';
    addChatUser(userMessage)

    $.ajax({
        type: "POST",
        url: "/",
        data: { userQuery: userMessage },
        dataType: "json",
        success: function (data) {
            addChatBot(data.answer);
        },
        error: function (xhr, textStatus, errorThrown) {
            console.error("AJAX Request failed -> ", textStatus, " -> ", errorThrown);
        }
    });
});


const chatArea = document.querySelector(".card-body")
function addChatUser(message) {
    html = `<div class="msg-send-div">
                <div class="msg-send col-md-6 col-sm-10">
                    <p>${message}</p>
                </div> 
            </div>`;

    chatArea.innerHTML += html;
}

function addChatBot(message) {
    html = `<div class="msg-recive-div">
                <img class="profile-photo-small rounded-circle" src="{{ url_for('static', filename='logo.jpg') }}" alt="">
                <div class="msg-recive col-md-6 col-sm-10">
                    <p>${message}</p>
                </div>
            </div>`

    chatArea.innerHTML += html;
}

