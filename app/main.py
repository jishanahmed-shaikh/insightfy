from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import fitz
from app.nlp_utils import summarize_text, analyze_sentiment, list_unique_words

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/main.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

async def extract_text_from_pdf(file):

    pdf_bytes = await file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.post("/process")
async def process_input(
    action: str = Form(...),
    textInput: str = Form(None),
    fileInput: UploadFile = File(None)
):
    content = textInput
    if fileInput:
        if fileInput.content_type == 'application/pdf':
            content = await extract_text_from_pdf(fileInput) 
        else:
            content = await fileInput.read()
            content = content.decode('utf-8')  

    result = ""
    if action == 'summarize':
        result = summarize_text(content)
    elif action == 'sentiment':
        result = analyze_sentiment(content)
    elif action == 'unique-words':
        result = list_unique_words(content)

    print(f"Action: {action}, Result: {result}") 

    return JSONResponse(content={"result": result})

@app.post("/clear")
async def clear_inputs():
    return JSONResponse(content={"result": "Inputs cleared"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)