from pydantic import BaseModel

class DiabetesInput(BaseModel):
    bmi: float
    age: int
    hypertension: int
    # ... todas as features
