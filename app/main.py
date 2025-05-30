from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Load model, tokenizer, label encoder
model = load_model("app/text_rnn_model.h5")  
with open("app/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)
with open("app/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

max_len = 5616  

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(request: Request, text: str = Form(...)):
    # Preprocess input text
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len)
    
    # Predict
    pred_probs = model.predict(padded)
    pred_class_idx = pred_probs.argmax(axis=1)[0]
    pred_label = label_encoder.inverse_transform([pred_class_idx])[0]
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "input_text": text,
        "predicted_label": pred_label
    })
