# Fruit Classifier Project

## Overview
This project implements a **fruit classification system** using **Dagster** for data pipeline orchestration and **FastAPI** for serving the trained model. The pipeline includes data extraction, preprocessing, model training, and evaluation.

## Project Structure
```
fruit_classifier/
│── src/
│   ├── data/
│   │   ├── load_data.py
│   │   ├── preprocess.py
│   ├── models/
│   │   ├── train_model.py
│   │   ├── evaluate_model.py
│   │   ├── predict.py
│   ├── assets.py
│   ├── main.py
│── dagster.yaml
│── requirements.txt
│── README.md
```

## Components
- **Dagster**: Manages the data pipeline for training the fruit classifier model.
- **FastAPI**: Provides an API for making predictions using the trained model.

## Installation
Ensure you have Python installed, then install the required dependencies:

```sh
pip install -r requirements.txt
```

## Running the Project

### 1. Start Dagster
Dagster runs the data pipeline and provides a UI for monitoring jobs.

```sh
dagster dev --port 3002
```

### 2. Run the Dagster Job (Pipeline Execution)
You can execute the Dagster job directly using:

```sh
python main.py
```

This script will:
- Start Dagster's development environment (Dagit UI at `http://localhost:3002`)
- Execute the `fruit_classifier_job` to train and evaluate the model
- Launch the FastAPI server to serve predictions

### 3. Access FastAPI
Once FastAPI is running, access the API documentation at:

```
http://localhost:8000
```

### 4. Making Predictions
Use FastAPI to send a POST request for predictions:

## Dagster Assets
The `assets.py` file defines the pipeline using **Dagster Assets**:
- `extract_data()`: Loads the dataset
- `preprocess_raw_data()`: Cleans and preprocesses data
- `model_train()`: Trains the model
- `eval_model()`: Evaluates the model


