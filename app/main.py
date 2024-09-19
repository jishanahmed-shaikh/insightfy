from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from .nlp_utils import summarize_text, analyze_sentiment, list_unique_words

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/main.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/process")
async def process_input(
    action: str = Form(...),
    textInput: str = Form(None),
    fileInput: UploadFile = File(None)
):
    content = textInput
    if fileInput:
        content = await fileInput.read()
        content = content.decode('utf-8') 

    result = ""
    if action == 'summarize':
        result = summarize_text(content)
    elif action == 'sentiment':
        result = analyze_sentiment(content)
    elif action == 'unique-words':
        result = list_unique_words(content)

    return JSONResponse(content={"result": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)