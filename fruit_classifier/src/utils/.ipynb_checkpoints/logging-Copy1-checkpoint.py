data:
  raw_data_path: "data/raw/fruit_data_with_colors.txt"
  processed_data_path: "data/processed/processed_fruits.csv"
  external_data_path: "data/external/"
  interim_data_path: "data/interim/"

model:
  random_state: 42
  test_size: 0.2
  cross_validation_folds: 5
  
paths:
  model_save_path: "models/fruit_classifier.joblib"
  log_path: "logs/training.log"
  performance_path: "reports/performance/"

features:
  numerical:
    - mass
    - width
    - height
    - color_score
    - area
    - density
    - aspect_ratio