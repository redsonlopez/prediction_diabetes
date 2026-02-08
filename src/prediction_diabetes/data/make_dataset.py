from pathlib import Path
import pandas as pd
import logging

# ==========================
# Configuração
# ==========================

RAW_DATA_PATH = Path("data/raw/diabetes.csv")
PROCESSED_DATA_PATH = Path("data/processed/features_diabetes.csv")

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
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ==========================
# Etapas de limpeza
# ==========================

def load_raw_data(path: Path) -> pd.DataFrame:
    logging.info("Carregando dados brutos")
    return pd.read_csv(path)


def map_smoking_history(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Mapeando smoking_history")

    df = df.copy()
    df["smoking_history"] = df["smoking_history"].map(SMOKING_MAP)

    if df["smoking_history"].isna().any():
        raise ValueError("Valores inesperados em smoking_history")

    df.rename(columns={"smoking_history": "smoking_history_mapped"}, inplace=True)
    return df


def encode_gender(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Aplicando one-hot encoding em gender")

    return pd.get_dummies(
        df,
        columns=["gender"],
        drop_first=True,
        dtype=int
    )


def save_processed_data(df: pd.DataFrame, path: Path) -> None:
    logging.info("Salvando dados processados")

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


# ==========================
# Pipeline offline
# ==========================

def build_dataset() -> None:
    df = load_raw_data(RAW_DATA_PATH)
    df = map_smoking_history(df)
    df = encode_gender(df)
    save_processed_data(df, PROCESSED_DATA_PATH)


if __name__ == "__main__":
    build_dataset()

