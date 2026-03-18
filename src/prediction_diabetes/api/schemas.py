from pydantic import BaseModel, Field

from prediction_diabetes.config import FEATURE_COLUMNS


class DiabetesInput(BaseModel):
    age: int = Field(..., example=23)
    physical_activity_minutes_per_week: int = Field(..., example=360)
    diet_score: float = Field(..., example=9.0)
    screen_time_hours_per_day: float = Field(..., example=1.0)
    bmi: float = Field(..., example=21.5)

