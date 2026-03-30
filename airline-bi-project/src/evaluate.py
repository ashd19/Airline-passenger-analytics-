import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import json
import os

def evaluate_models(X_test, y_test, models, output_dir='outputs'):
    """Evaluate models and save metrics."""
    if not os.path.exists(f'{output_dir}/plots'):
        os.makedirs(f'{output_dir}/plots')
        
    metrics = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        
        metrics[name] = {
            'accuracy': float(accuracy_score(y_test, y_pred)),
            'precision': float(precision_score(y_test, y_pred)),
            'recall': float(recall_score(y_test, y_pred)),
            'f1': float(f1_score(y_test, y_pred))
        }
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f'Confusion Matrix: {name}')
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.savefig(f'{output_dir}/plots/cm_{name}.png')
        plt.close()
        
        # Feature Importance for Random Forest
        if name == 'RandomForest':
            importances = model.feature_importances_
            feature_names = X_test.columns
            feature_importance_df = pd.DataFrame({'feature': feature_names, 'importance': importances})
            feature_importance_df = feature_importance_df.sort_values(by='importance', ascending=False)
            
            plt.figure(figsize=(10, 8))
            sns.barplot(x='importance', y='feature', data=feature_importance_df.head(15))
            plt.title('Top 15 Feature Importances (Random Forest)')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/plots/feature_importance.png')
            plt.close()
            
            # Save feature importance to csv
            feature_importance_df.to_csv(f'{output_dir}/feature_importance.csv', index=False)
            
    # Save metrics to JSON
    with open(f'{output_dir}/metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)
        
    print(f"Evaluation complete. Metrics and plots saved to {output_dir}")
    return metrics

if __name__ == "__main__":
    X_test = pd.read_csv('airline-bi-project/data/processed/X_test.csv')
    y_test = pd.read_csv('airline-bi-project/data/processed/y_test.csv')
    
    models = {
        'LogisticRegression': joblib.load('airline-bi-project/models/LogisticRegression.joblib'),
        'DecisionTree': joblib.load('airline-bi-project/models/DecisionTree.joblib'),
        'RandomForest': joblib.load('airline-bi-project/models/RandomForest.joblib')
    }
    
    evaluate_models(X_test, y_test, models, 'airline-bi-project/outputs')
