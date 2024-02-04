document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault();
    sendMessage();
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.textContent = userInput;

    document.querySelector('.chat').appendChild(userMessage);

    document.getElementById('user-input').value = '';

    // Envoyez la question au serveur et mettez à jour la réponse du bot
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'user_input=' + encodeURIComponent(userInput),
    })
    .then(response => response.text())
    .then(botResponse => {
        const botMessage = document.createElement('div');
        botMessage.className = 'bot-message';
        botMessage.textContent = botResponse;

        document.querySelector('.chat').appendChild(botMessage);
    });
}
