import pandas as pd
from pathlib import Path

def load_raw_data(filepath: str) -> pd.DataFrame:
    """Load raw fruit dataset from file."""
    return pd.read_csv(filepath, sep='\t')