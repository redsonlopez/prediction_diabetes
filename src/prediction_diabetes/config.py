FEATURE_COLUMNS = [
    "HbA1c_level",
    "blood_glucose_level",
    "age",
    "bmi",
    "hypertension",
    "smoking_history_mapped",
]

TARGET_COLUMN = "diabetes"

RAW_DATA_PATH = "data/raw/diabetes.csv"
PROCESSED_DATA_PATH = "data/processed/features_diabetes.csv"
MODEL_PATH = "models/logistic_diabetes.pkl"

