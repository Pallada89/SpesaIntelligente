from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
import pytesseract, os, json

app = FastAPI(title="RisparmioSmart Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HERE = os.path.dirname(__file__)
OFFERS_FILE = os.path.join(HERE, "offers.json")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/offers")
def offers():
    if os.path.exists(OFFERS_FILE):
        with open(OFFERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []
    return {"offers": data}

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    try:
        img = Image.open(BytesIO(await file.read()))
        text = pytesseract.image_to_string(img, lang="ita")
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
