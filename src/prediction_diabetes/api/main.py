from fastapi import FastAPI
from prediction_diabetes.models.predictor import DiabetesPredictor
from prediction_diabetes.api.schemas import DiabetesInput

app = FastAPI(title="Diabetes Prediction API")

predictor = DiabetesPredictor()

@app.post("/predict")
def predict(data: DiabetesInput):
    return predictor.predict(data.dict())
