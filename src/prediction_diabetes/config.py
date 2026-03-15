FEATURE_COLUMNS = [
    "age",
    "physical_activity_minutes_per_week",
    "diet_score",
    "screen_time_hours_per_day",
    "bmi"
]

TARGET_COLUMN = "diagnosed_diabetes"

DECISION_THRESHOLD = 0.30

RAW_DATA_PATH = "data/raw/diabetes_health_indicators.csv"
PROCESSED_DATA_PATH = "data/processed/features_diabetes.csv"
MODEL_PATH = "artifacts/logistic_diabetes.pkl"

