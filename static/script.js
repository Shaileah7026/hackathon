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
                <div class="message msg-send col-auto">
                    <p class="p-0 m-0">${message}</p>
                </div> 
            </div>`;

    chatArea.innerHTML += html;
}

function addChatBot(message) {
    const botChatBubble = document.createElement('div');
    botChatBubble.className = 'msg-recive-div';

    // Process newline characters and create separate paragraphs
    const paragraphs = message.split('\n').map(paragraph => {
        return `<p class="p-0 m-0">${paragraph}</p>`;
    });

    botChatBubble.innerHTML = `
        <div class="msg-recive col-auto">
            ${paragraphs.join('<br>')}
        </div>
    `;

    chatArea.appendChild(botChatBubble);
}


