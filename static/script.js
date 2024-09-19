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

    fetch('http://localhost:8000/process', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = data.result;
    })
    .catch(error => console.error('Error:', error));
}
