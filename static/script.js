document.getElementById('text-input').addEventListener('input', toggleButtons);
document.getElementById('file-input').addEventListener('change', toggleButtons);

function toggleButtons() {
    const textInput = document.getElementById('text-input').value.trim();
    const fileInput = document.getElementById('file-input').files.length > 0;
    const enable = textInput || fileInput;
    document.getElementById('summarize-btn').disabled = !enable;
    document.getElementById('sentiment-btn').disabled = !enable;
    document.getElementById('unique-words-btn').disabled = !enable;
}

function processInput(action) {
    const textInput = document.getElementById('text-input').value;
    const fileInput = document.getElementById('file-input').files[0];
    const formData = new FormData();
    formData.append('action', action);
    if (textInput) {
        formData.append('textInput', textInput);
    }
    if (fileInput) {
        formData.append('fileInput', fileInput);
    }
    console.log('Sending data:', action, textInput, fileInput);

    fetch('http://localhost:8000/process', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Response data:', data);
        if (data.error) {
            document.getElementById('output').innerText = `Error: ${data.error}`;
        } else {
            if (action === 'sentiment') {
                const sentimentEmoji = getSentimentEmoji(data.result);
                document.getElementById('output').innerHTML = `${sentimentEmoji} <br>Sentiment: ${data.result}`;
            } else if (Array.isArray(data.result)) {
                document.getElementById('output').innerHTML = `<ul>${data.result.map(item => `<li>${item}</li>`).join('')}</ul>`;
            } else {
                document.getElementById('output').innerText = data.result;
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('output').innerText = `Error: ${error.message}`;
    });
}

function getSentimentEmoji(sentiment) {
    switch (sentiment.toLowerCase()) {
        case 'positive':
            return '😄';
        case 'negative':
            return '😞';
        case 'neutral':
            return '😐';
        default:
            return '';
    }
}

function clearInputs() {
    document.getElementById('text-input').value = '';
    document.getElementById('file-input').value = '';
    document.getElementById('output').innerText = '';
    toggleButtons();
    fetch('http://localhost:8000/clear', {
        method: 'POST'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Clear response:', data);
    })
    .catch(error => {
        console.error('Error clearing inputs:', error);
    });
}

document.getElementById('summarize-btn').addEventListener('click', () => processInput('summarize'));
document.getElementById('sentiment-btn').addEventListener('click', () => processInput('sentiment'));
document.getElementById('unique-words-btn').addEventListener('click', () => processInput('unique-words'));
