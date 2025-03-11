from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from typing import Tuple
import numpy as np
from pathlib import Path

# Get the absolute path to the Project directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Moves up to src/

# Adjust the file path relative to diabetesProj
filepath = BASE_DIR.parent / "models/model.joblib"


def train_model(df) -> Tuple[RandomForestClassifier, dict]:
    """Train the fruit classification model."""
    X = df[["mass","width","height","color_score"]]
    y = df[['fruit_label']]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, stratify=y, random_state=42)
    
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight='balanced'
    )

    model.fit(X_train, y_train)
    joblib.dump(model, filepath)
    return model, {'X_train': X_train, 'X_test': X_test, 
                  'y_train': y_train, 'y_test': y_test}