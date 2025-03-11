from sklearn.metrics import classification_report, confusion_matrix
import json
import logging

def evaluate_model(model, X_test, y_test, save_path: str = None):
    """Evaluate model performance and save metrics."""
    predictions = model.predict(X_test)
    
    metrics = {
        'classification_report': classification_report(y_test, predictions, output_dict=True),
        'confusion_matrix': confusion_matrix(y_test, predictions).tolist()
    }
    
    if save_path:
        with open(save_path, 'w') as f:
            json.dump(metrics, f, indent=4)
    
    return metrics