document.getElementById("send-btn").onclick = function() {
    let userMessage = document.getElementById("user-input").value.trim();

    if (userMessage === "") {
        return;
    }

    // Display user message
    let chatLog = document.getElementById("chat-log");
    let userPara = document.createElement("p");
    userPara.classList.add("user-message");
    userPara.innerHTML = userMessage;
    chatLog.appendChild(userPara);

    // Clear input
    document.getElementById("user-input").value = "";

    // Scroll to the bottom
    chatLog.scrollTop = chatLog.scrollHeight;

    // Send message to the server
    fetch("/chat", {
        method: "POST",
        body: new URLSearchParams("message=" + userMessage),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        let botPara = document.createElement("p");
        botPara.classList.add("bot-message");
        botPara.innerHTML = data.response;
        chatLog.appendChild(botPara);

        // Scroll to the bottom
        chatLog.scrollTop = chatLog.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });
};

// Allow pressing Enter to send message
document.getElementById("user-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        document.getElementById("send-btn").click();
    }
});
