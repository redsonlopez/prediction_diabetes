import joblib
import pandas as pd
from pathlib import Path

from prediction_diabetes.config import MODEL_PATH, FEATURE_COLUMNS

BASE_DIR = Path(__file__).resolve().parents[3]
MODEL_FULL_PATH = BASE_DIR / MODEL_PATH


class DiabetesPredictor:
    def __init__(self):
        self.model = joblib.load(MODEL_FULL_PATH)

    def predict(self, data: dict):
        df = pd.DataFrame([data])
        df = df[FEATURE_COLUMNS]

        prob = self.model.predict_proba(df)[0][1]
        pred = int(prob >= 0.5)

        return {
            "prediction": pred,
            "probability": float(prob)
        }

