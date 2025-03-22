"""
Utility functions for the Mental Health Prediction project.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_data(filepath):
    """
    Load and perform initial data checks.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    df = pd.read_csv(filepath)
    print(f"Dataset shape: {df.shape}")
    print("\nMissing values:")
    print(df.isnull().sum())
    return df

def preprocess_data(df, categorical_columns):
    """
    Preprocess the data including one-hot encoding.
    
    Args:
        df (pd.DataFrame): Input dataset
        categorical_columns (list): List of categorical column names
        
    Returns:
        tuple: (X, y) where X is features and y is target variables
    """
    # Create a copy of the dataframe
    X = df.copy()
    
    # Perform one-hot encoding
    X_encoded = pd.get_dummies(X, columns=categorical_columns, prefix=categorical_columns)
    X = X_encoded
    
    # Define target variables
    y = df[['Depression_Score', 'Anxiety_Score']]
    
    # Remove target variables from features
    X = X.drop(['Depression_Score', 'Anxiety_Score'], axis=1)
    
    return X, y

def prepare_data(X, y, test_size=0.2, random_state=42):
    """
    Prepare data for modeling including train-test split and scaling.
    
    Args:
        X (pd.DataFrame): Features
        y (pd.DataFrame): Target variables
        test_size (float): Proportion of data to use for testing
        random_state (int): Random seed for reproducibility
        
    Returns:
        tuple: (X_train_scaled, X_test_scaled, y_train, y_test)
    """
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test 