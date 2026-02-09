from pathlib import Path
import pandas as pd
import logging

from prediction_diabetes.config import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
)

SMOKING_MAP = {
    "No Info": 0,
    "never": 1,
    "not current": 2,
    "former": 3,
    "ever": 3,
    "current": 4,
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def load_raw_data(path: str) -> pd.DataFrame:
    logging.info("Loading raw data")
    return pd.read_csv(path)


def map_smoking_history(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Mapping smoking_history")

    df = df.copy()
    df["smoking_history"] = df["smoking_history"].map(SMOKING_MAP)

    if df["smoking_history"].isna().any():
        raise ValueError("UNEXPECTED VALUES IN smoking_history")

    df.rename(
        columns={"smoking_history": "smoking_history_mapped"},
        inplace=True,
    )
    return df


def encode_gender(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Applying one-hot encoding to gender")

    return pd.get_dummies(
        df,
        columns=["gender"],
        drop_first=True,
        dtype=int,
    )


def select_features_and_target(
    df: pd.DataFrame,
    features: list[str],
    target: str,
) -> pd.DataFrame:
    logging.info("Selecting features and target")

    required = set(features + [target])
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"Missing columns in dataset: {missing}")

    return df[features + [target]]


def save_processed_data(df: pd.DataFrame, path: str) -> None:
    logging.info("Saving processed data")

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def build_dataset() -> None:
    logging.info("Starting dataset build")

    df = load_raw_data(RAW_DATA_PATH)
    df = map_smoking_history(df)
    df = encode_gender(df)

    df = select_features_and_target(
        df,
        features=FEATURE_COLUMNS,
        target=TARGET_COLUMN,
    )

    save_processed_data(df, PROCESSED_DATA_PATH)

    logging.info("Dataset build completed successfully")


if __name__ == "__main__":
    build_dataset()

