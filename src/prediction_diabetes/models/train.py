import joblib
import pandas as pd

from prediction_diabetes.features.build_features import create_pipeline
from prediction_diabetes.config import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    PROCESSED_DATA_PATH,
    MODEL_PATH,
)


def train() -> None:
    df = pd.read_csv(PROCESSED_DATA_PATH)

    required = set(FEATURE_COLUMNS + [TARGET_COLUMN])
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in training data: {missing}")

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    pipeline = create_pipeline()
    pipeline.fit(X, y)

    joblib.dump(pipeline, MODEL_PATH)


if __name__ == "__main__":
    train()

