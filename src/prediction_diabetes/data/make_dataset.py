from pathlib import Path
import pandas as pd
import logging

from sklearn.model_selection import train_test_split
from prediction_diabetes.config import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    RAW_DATA_PATH,
    TRAIN_DATA_PATH,
    TEST_DATA_PATH,
    TEST_SIZE,
    RANDOM_STATE,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def load_raw_data(path: str) -> pd.DataFrame:
    logging.info("Loading raw data")
    return pd.read_csv(path)


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

    return df[features + [target]].copy()


def split_data(df: pd.DataFrame):
    logging.info("Splitting data into train and test")

    X = df.drop(TARGET_COLUMN, axis=1)
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    train_df = pd.concat([X_train, y_train], axis=1)
    test_df = pd.concat([X_test, y_test], axis=1)

    return train_df, test_df


def save_dataframe(df: pd.DataFrame, path: str) -> None:
    logging.info(f"Saving data to {path}")

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def build_dataset() -> None:
    logging.info("Starting dataset build")

    df = load_raw_data(RAW_DATA_PATH)

    df = select_features_and_target(
        df,
        features=FEATURE_COLUMNS,
        target=TARGET_COLUMN,
    )

    train_df, test_df = split_data(df)
    logging.info(f"Train shape: {train_df.shape}")
    logging.info(f"Test shape: {test_df.shape}")

    save_dataframe(train_df, TRAIN_DATA_PATH)
    save_dataframe(test_df, TEST_DATA_PATH)

    logging.info("Dataset build completed successfully")


if __name__ == "__main__":
    build_dataset()

