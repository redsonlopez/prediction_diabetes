from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression


def create_pipeline():
    return Pipeline(steps=[
        ("interactions", PolynomialFeatures(
            degree=2,
            interaction_only=True,
            include_bias=False
        )),
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(
            C=0.01,
            l1_ratio=1,
            solver="saga",
            max_iter=2000
        ))
    ])

