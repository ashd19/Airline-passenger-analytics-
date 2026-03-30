import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import json

def train_models(X_train, y_train, output_dir='models'):
    """Train multiple models and return them."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    models = {
        'LogisticRegression': LogisticRegression(max_iter=1000),
        'DecisionTree': DecisionTreeClassifier(),
        'RandomForest': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    }
    
    trained_models = {}
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train.values.ravel())
        joblib.dump(model, f'{output_dir}/{name}.joblib')
        trained_models[name] = model
        
    return trained_models

if __name__ == "__main__":
    X_train = pd.read_csv('airline-bi-project/data/processed/X_train.csv')
    y_train = pd.read_csv('airline-bi-project/data/processed/y_train.csv')
    train_models(X_train, y_train, 'airline-bi-project/models')
