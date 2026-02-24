document.addEventListener('DOMContentLoaded', () => {
    const chatWindow = document.getElementById('chat-window');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const personaSelect = document.getElementById('persona-select');

    let chatHistory = [];

    const addMessage = (text, sender) => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(sender === 'user' ? 'user-message' : 'ai-message');
        messageDiv.textContent = text;
        chatWindow.appendChild(messageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    };

    const sendMessage = async () => {
        const message = userInput.value.trim();
        const persona = personaSelect.value;

        if (!message) return;

        addMessage(message, 'user');
        userInput.value = '';
        
        // Add loading state
        const loadingDiv = document.createElement('div');
        loadingDiv.classList.add('message', 'ai-message');
        loadingDiv.textContent = '...';
        chatWindow.appendChild(loadingDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    persona: persona,
                    history: chatHistory
                }),
            });

            const data = await response.json();
            
            chatWindow.removeChild(loadingDiv);

            if (data.response) {
                addMessage(data.response, 'ai');
                chatHistory.push({ role: 'user', parts: [message] });
                chatHistory.push({ role: 'model', parts: [data.response] });
            } else {
                addMessage('죄송해요, 대화 중에 오류가 발생했어요.', 'ai');
            }
        } catch (error) {
            chatWindow.removeChild(loadingDiv);
            console.error('Error:', error);
            addMessage('서버에 연결할 수 없어요.', 'ai');
        }
    };

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    personaSelect.addEventListener('change', () => {
        chatHistory = []; // Reset history when persona changes
        chatWindow.innerHTML = `<div class="message ai-message">안녕! 나는 이제부터 ${personaSelect.value}야. 무엇이든 물어봐!</div>`;
    });
});
