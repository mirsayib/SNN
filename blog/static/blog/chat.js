var message_tab = document.getElementById('msg-tab')
var chat_log = document.getElementById("chat-log")
var msgInput = document.getElementById("chat-message-input")
var msgSubmit = document.getElementById("chat-message-submit")


if (message_tab){
    message_tab.scrollTop = message_tab.scrollHeight

    var groupName = document.getElementById("group-name")
    var currentUser = document.getElementById("current_user")

    if(!groupName){
        var group_Name = 'lobby'
        var current_User = JSON.parse(document.getElementById("current_user_lobby").textContent)
    }
    else{
        var group_Name = JSON.parse(groupName.textContent)
        var current_User = JSON.parse(currentUser.textContent)
    }

    var ws = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/ac/'
        + group_Name
        + '/'
    )


    msgSubmit.onclick = (event) => {
        const message = msgInput.value
        if (message) {
            ws.send(JSON.stringify({
                'msg': message,
                'sender': current_User
            }))

            msgInput.value = ""
        }
    }

    ws.onopen = () => {
        console.log('Websocket connection open...');
    }

    ws.onmessage = (event) => {
        console.log('Message received from Server...', event.data);
        const data = JSON.parse(event.data)

        msg = document.createElement('div')
        msg.class = "chat-message-left pb-4"


        msg.innerHTML = `<div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3 mb-3">
									<div class="font-weight-bold mb-1">${data.sender}</div>
									${data.msg}
								</div>`
        message_tab.appendChild(msg)

        message_tab.scrollTop = message_tab.scrollHeight

    }

    ws.onerror = (event) => {
        console.log('Error Encountered...', event);
    }

    ws.onclose = (event) => {
        console.log('Websocket Connection Closed...', event);
    }


}


