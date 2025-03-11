from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi import Request
import numpy as np
import pandas as pd  
import joblib

# Load the trained model and the scaler
MODEL_PATH = "models/model.joblib"
SCALER_PATH = "models/scaler.joblib"
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

app = FastAPI()

# Setup Jinja2 templates
templates = Jinja2Templates(directory="src/templates")

# Define input model
class PredictionInput(BaseModel):
    mass: float
    width: float
    height: float
    color_score: float

@app.get("/")
def read_root(request: Request):
    """Serve the prediction form as a separate page."""
    return templates.TemplateResponse("prediction_form.html", {"request": request})

@app.post("/predict/")
def predict(request: Request, mass: float = Form(...), width: float = Form(...), height: float = Form(...), color_score: float = Form(...)):
    """Receives structured input and returns a prediction."""
    
    # Create the features DataFrame
    features = pd.DataFrame(
        [[mass, width, height, color_score]],
        columns=['mass', 'width', 'height', 'color_score']
    )  # Using DataFrame to retain feature names
    
    # Scale the features using the loaded scaler
    features_scaled = scaler.transform(features)

    # Make the prediction
    prediction = model.predict(features_scaled)
    probabilities = model.predict_proba(features_scaled)

    # Label map for fruit classes
    label_map = {1: "apple", 2: "mandarin", 3: "orange", 4: "lemon"}

    # Return the result on a separate page
    return templates.TemplateResponse("prediction_result.html", {
        "request": request, 
        "prediction": label_map[prediction[0]],
        "probabilities": probabilities.tolist()
    })
