#!/bin/bash
set -e

echo "[INFO] Setting up virtual environment for Reproducible Training Pipeline..."
python3 -m venv venv
source venv/bin/activate

echo "[INFO] Installing dependencies..."
pip install --upgrade pip
pip install mlflow scikit-learn dvc pandas numpy

echo "[INFO] Executing training script and logging metrics to MLflow..."
python train.py

echo "[SUCCESS] Training pipeline execution complete!"
