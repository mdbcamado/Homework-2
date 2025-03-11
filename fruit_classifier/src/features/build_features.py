import pandas as pd
import numpy as np

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create engineered features for the fruit dataset."""
    df['area'] = df['width'] * df['height']
    df['density'] = df['mass'] / df['area']
    df['aspect_ratio'] = df['height'] / df['width']
    return df