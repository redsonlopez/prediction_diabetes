from pydantic import BaseModel, Field

from prediction_diabetes.config import FEATURE_COLUMNS


class DiabetesInput(BaseModel):
    HbA1c_level: float = Field(..., example=6.5)
    blood_glucose_level: float = Field(..., example=140)
    age: int = Field(..., example=45)
    bmi: float = Field(..., example=27.3)
    hypertension: int = Field(..., example=0)
    smoking_history_mapped: int = Field(..., example=2)

