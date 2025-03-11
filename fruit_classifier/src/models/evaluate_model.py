from sklearn.metrics import classification_report, confusion_matrix
import json
from pathlib import Path

# Get the absolute path to the Project directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Moves up to src/

# Adjust the file path relative to diabetesProj
filepath = BASE_DIR.parent / "reports/metrics.json"

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance and save metrics."""
    predictions = model.predict(X_test)
    
    metrics = {
        'classification_report': classification_report(y_test, predictions, output_dict=True),
        'confusion_matrix': confusion_matrix(y_test, predictions).tolist()
    }
    
    with open(filepath, "w") as f:
        json.dump(metrics, f, indent=4)
    
    print(metrics) 

    return metrics