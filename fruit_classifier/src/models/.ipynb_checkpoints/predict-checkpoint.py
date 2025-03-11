import numpy as np
from typing import List, Dict

def predict_fruit(model, features: np.ndarray) -> List[str]:
    """Make fruit predictions with probability scores."""
    predictions = model.predict(features)
    probabilities = model.predict_proba(features)
    
    label_map = {1: 'apple', 2: 'mandarin', 3: 'orange', 4: 'lemon'}
    return [label_map[pred] for pred in predictions]