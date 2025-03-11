import os
from dagster import AssetOut, asset, multi_asset
import pandas as pd
from src.data.load_data import load_raw_data
from src.data.preprocess import preprocess_data
from src.models.train_model import train_model
from src.models.evaluate_model import evaluate_model

asset_group_name = "fruit_classifier"

@asset(group_name=asset_group_name, compute_kind="pandas")
def extract_data():
    """Calls the function from load_data.py"""
    return load_raw_data()

@asset(group_name=asset_group_name, compute_kind="scikit-learn")
def preprocess_raw_data(extract_data):
    """Calls the function from preprocess_data.py"""
    return preprocess_data(extract_data)

@multi_asset(group_name=asset_group_name, compute_kind="scikit-learn",
             outs={"training_data": AssetOut(), "test_data": AssetOut(), "model": AssetOut()}
             )
def model_train(preprocess_raw_data):
    """Calls the function from train_model.py"""
    model, data_splits = train_model(preprocess_raw_data)

    return (data_splits["X_train"], data_splits["y_train"]), (data_splits["X_test"], data_splits["y_test"]), model

@multi_asset(
    group_name=asset_group_name,
    compute_kind="scikit-learn",
    outs={"metrics": AssetOut()} 
)
def eval_model(test_data, model):
    """Calls the function from evaluate_model.py"""

    X_test, y_test = test_data

    metrics = evaluate_model(model, X_test, y_test)

    return metrics

