from fastapi import FastAPI

from prediction_diabetes.inference.predictor import DiabetesPredictor
from prediction_diabetes.api.schemas import DiabetesInput

app = FastAPI(title="Diabetes Prediction API")

predictor = DiabetesPredictor()

@app.post("/predict")
def predict(data: DiabetesInput):
    return predictor.predict(data.dict())


@app.get("/")
def health_check():
    return {"status": "ok", "model": "logistic_diabetes"}

