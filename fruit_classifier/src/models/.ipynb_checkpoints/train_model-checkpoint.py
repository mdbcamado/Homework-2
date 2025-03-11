from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import logging
from typing import Tuple
import numpy as np

def train_model(X: np.ndarray, y: np.ndarray, config: dict) -> Tuple[RandomForestClassifier, dict]:
    """Train the fruit classification model."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config['model']['test_size'], stratify=y, random_state=config['model']['random_state'])
    
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=config['model']['random_state'],
        class_weight='balanced'
    )
    
    model.fit(X_train, y_train)
    return model, {'X_train': X_train, 'X_test': X_test, 
                  'y_train': y_train, 'y_test': y_test}