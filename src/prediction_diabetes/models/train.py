import joblib
import pandas as pd

from prediction_diabetes.models.model_pipeline import create_pipeline
from prediction_diabetes.config import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    TRAIN_DATA_PATH,
    MODEL_LATEST_PATH,
    MODEL_VERSIONED_PATH
)


def train() -> None:
    df = pd.read_csv(TRAIN_DATA_PATH)

    required = set(FEATURE_COLUMNS + [TARGET_COLUMN])
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in training data: {missing}")

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    pipeline = create_pipeline()
    pipeline.fit(X, y)

    joblib.dump(pipeline, MODEL_LATEST_PATH)
    joblib.dump(pipeline, MODEL_VERSIONED_PATH)


if __name__ == "__main__":
    train()

