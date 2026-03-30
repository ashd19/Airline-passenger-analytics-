import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
import os

def load_data(file_path):
    """Load the airline passenger satisfaction dataset."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Handle missing values and basic cleaning."""
    # Fill missing Arrival Delay with median
    df['Arrival Delay'] = df['Arrival Delay'].fillna(df['Arrival Delay'].median())
    
    # Drop ID as it's not a feature
    if 'ID' in df.columns:
        df = df.drop(columns=['ID'])
        
    return df

def encode_features(df):
    """Encode categorical features and target."""
    le = LabelEncoder()
    
    # Categorical columns to encode
    cat_cols = ['Gender', 'Customer Type', 'Type of Travel', 'Class']
    
    encoders = {}
    for col in cat_cols:
        encoders[col] = LabelEncoder()
        df[col] = encoders[col].fit_transform(df[col])
        
    # Encode target
    df['Satisfaction'] = le.fit_transform(df['Satisfaction'])
    encoders['Satisfaction'] = le
    
    return df, encoders

def preprocess_pipeline(file_path, output_dir='data/processed'):
    """Complete preprocessing pipeline."""
    df = load_data(file_path)
    df = clean_data(df)
    df, encoders = encode_features(df)
    
    X = df.drop(columns=['Satisfaction'])
    y = df['Satisfaction']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Convert back to DataFrame to keep column names for feature importance later
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=X.columns)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=X.columns)
    
    # Save artifacts
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    X_train_scaled.to_csv(f'{output_dir}/X_train.csv', index=False)
    X_test_scaled.to_csv(f'{output_dir}/X_test.csv', index=False)
    y_train.to_csv(f'{output_dir}/y_train.csv', index=False)
    y_test.to_csv(f'{output_dir}/y_test.csv', index=False)
    
    joblib.dump(scaler, f'{output_dir}/scaler.joblib')
    joblib.dump(encoders, f'{output_dir}/encoders.joblib')
    
    print(f"Preprocessing complete. Files saved to {output_dir}")
    return X_train_scaled, X_test_scaled, y_train, y_test

if __name__ == "__main__":
    preprocess_pipeline('airline-bi-project/data/airline_passenger_satisfaction.csv', 'airline-bi-project/data/processed')
