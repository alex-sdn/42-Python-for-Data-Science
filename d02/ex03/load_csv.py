import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads a .csv, prints the dimensions and returns a pandas DataFrame"""
    try:
        data = pd.read_csv(path)

        print(f"Loading dataset of dimensions {data.shape}")

        return data
    except Exception as e:
        print(str(e))
        return None
