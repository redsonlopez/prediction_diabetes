import json
import joblib
import pandas as pd
import logging

from pathlib import Path

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from prediction_diabetes.config import (
    TEST_DATA_PATH,
    MODEL_LATEST_PATH,
    METRICS_PATH,
    TARGET_COLUMN,
    DECISION_THRESHOLD
)

logging.basicConfig(level=logging.INFO)


def load_data():
    logging.info("Loading test data")
    df = pd.read_csv(TEST_DATA_PATH)

    X = df.drop(TARGET_COLUMN, axis=1)
    y = df[TARGET_COLUMN]

    return X, y


def evaluate():
    logging.info("Loading model")
    model = joblib.load(MODEL_LATEST_PATH)

    X, y = load_data()

    logging.info("Generating probabilities")
    y_proba = model.predict_proba(X)[:, 1]

    logging.info(f"Applying threshold: {DECISION_THRESHOLD}")
    y_pred = (y_proba >= DECISION_THRESHOLD).astype(int)

    logging.info("Calculating metrics")
    metrics = {
        "threshold": DECISION_THRESHOLD,
        "accuracy": accuracy_score(y, y_pred),
        "precision": precision_score(y, y_pred, zero_division=0),
        "recall": recall_score(y, y_pred, zero_division=0),
        "f1_score": f1_score(y, y_pred, zero_division=0),
        "confusion_matrix": confusion_matrix(y, y_pred).tolist()
    }

    for k, v in metrics.items():
        logging.info(f"{k}: {v}")

    logging.info("Saving metrics")

    Path(METRICS_PATH).parent.mkdir(parents=True, exist_ok=True)

    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)

    logging.info("Evaluation completed successfully")


if __name__ == "__main__":
    evaluate()
