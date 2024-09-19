document.getElementById('send-button').addEventListener('click', async function() {
    const userInput = document.getElementById('user-input').value;
    const chatOutput = document.getElementById('chat-output');

    // Отображение пользовательского сообщения
    chatOutput.innerHTML += `<p><strong>Вы:</strong> ${userInput}</p>`;

    // Запрос к AI (например, к OpenAI API)
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ВАШ_API_КЛЮЧ`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{ role: "user", content: userInput }]
        })
    });
    
    const data = await response.json();
    const botReply = data.choices[0].message.content;

    // Отображение ответа бота
    chatOutput.innerHTML += `<p><strong>AI:</strong> ${botReply}</p>`;
    
    // Очистка поля ввода
    document.getElementById('user-input').value = '';
});
