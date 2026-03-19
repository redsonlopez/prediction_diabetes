import pandas as pd

timestamp = pd.Timestamp.now().date()

FEATURE_COLUMNS = [
    "age",
    "physical_activity_minutes_per_week",
    "diet_score",
    "screen_time_hours_per_day",
    "bmi"
]
TARGET_COLUMN = "diagnosed_diabetes"

RAW_DATA_PATH = "data/raw/diabetes_health_indicators.csv"
TRAIN_DATA_PATH = "data/processed/train.csv"
TEST_DATA_PATH = "data/processed/test.csv"
MODEL_LATEST_PATH = "artifacts/model.pkl"
MODEL_VERSIONED_PATH = f"artifacts/models/model_{timestamp}.pkl"
METRICS_PATH = f"artifacts/metrics_{timestamp}.json"

DECISION_THRESHOLD = 0.3
TEST_SIZE = 0.2
RANDOM_STATE = 42

