import joblib
import pandas as pd

MODEL_PATH = "models/logistic_diabetes.pkl"

class DiabetesPredictor:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, data: dict):
        df = pd.DataFrame([data])
        prob = self.model.predict_proba(df)[0][1]
        pred = int(prob >= 0.5)

        return {
            "prediction": pred,
            "probability": prob
        }

