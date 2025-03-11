import pandas as pd
from pathlib import Path

# Get the absolute path to the Project directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Moves up to src/

# Adjust the file path relative to diabetesProj
filepath = BASE_DIR.parent / "data/raw/fruit_data_with_colors.txt"

def load_raw_data() -> pd.DataFrame:
    """Load raw fruit dataset from file."""
    print(f"Loading file from: {filepath}")  # Debugging
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return pd.read_csv(filepath, sep='\t')
