import mlflow
import pandas as pd
from fastapi import FastAPI
from src.api.pydantic_models import PredictionRequest, PredictionResponse

app = FastAPI()

MODEL_NAME = "CreditRiskModel"
MODEL_STAGE = "Production"

model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{MODEL_NAME}/{MODEL_STAGE}"
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    df = pd.DataFrame([request.features])
    prob = model.predict(df)[0]
    return PredictionResponse(risk_probability=float(prob))
