import joblib
import pandas as pd
from prediction_diabetes.features.build_features import create_pipeline

def train():
    df = pd.read_csv("data/processed/features_diabetes.csv")
    X = df.drop("diabetes", axis=1)
    y = df["diabetes"]

    pipeline = create_pipeline()
    pipeline.fit(X, y)

    joblib.dump(pipeline, "models/logistic_diabetes.pkl")

if __name__ == "__main__":
    train()

