from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import joblib


filepath = "models/scaler.joblib"

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess raw data with scaling and cleaning."""
    scaler = StandardScaler()
    numerical_features = ['mass', 'width', 'height', 'color_score']
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    joblib.dump(scaler, filepath)
    return df