from pydantic import BaseModel, Field

from prediction_diabetes.config import FEATURE_COLUMNS


class DiabetesInput(BaseModel):
    age: int = Field(..., example=48)
    physical_activity_minutes_per_week: int = Field(..., example=143)
    diet_score: float = Field(..., example=6.7)
    screen_time_hours_per_day: float = Field(..., example=8.7)
    bmi: float = Field(..., example=23.1)

