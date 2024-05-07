
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
from src.Config import Config as cfg
from src.data import Utils 

def preprocess_data(raw_data_path):
    """
    Preprocesses raw data and returns the processed data.
    
    Args:
        raw_data_path (str): Path to the raw data file.
        
    Returns:
        pd.DataFrame: Processed data.
    """
    # Load raw data
    
    
    
    
    # Perform preprocessing steps (e.g., handle missing values, encode categorical variables)
    # For demonstration, let's assume we're dropping missing values and scaling numerical features
    processed_data = raw_data.dropna()
    numerical_features = processed_data.select_dtypes(include=['int', 'float']).columns
    scaler = StandardScaler()
    processed_data[numerical_features] = scaler.fit_transform(processed_data[numerical_features])
    
    return processed_data

def extract_features(processed_data):
    """
    Extracts features from processed data.
    
    Args:
        processed_data (pd.DataFrame): Processed data.
        
    Returns:
        pd.DataFrame: Data with extracted features.
    """
    # Perform feature extraction (e.g., create new features, transform existing ones)
    # For demonstration, let's assume we're creating dummy variables for categorical features
    features = pd.get_dummies(processed_data)
    
    return features

def save_features(features, output_path):
    """
    Saves extracted features to a file.
    
    Args:
        features (pd.DataFrame): Data with extracted features.
        output_path (str): Path to save the features file.
    """
    features.to_csv(output_path, index=False)

def main():
    """
    Main function to preprocess raw data, extract features, and save them to a file.
    
    Args:
        raw_data_path (str): Path to the raw data file.
        output_path (str): Path to save the features file.
    """
    # Preprocess raw data
    processed_data = preprocess_data(raw_data_path)
    
    # Extract features
    features = extract_features(processed_data)
    
    # Save features to a file
    save_features(features, output_path)

if __name__ == "__main__":
    main()

 
 
 
"""
 # We have to collect all files paths into one array according to folders, train and test
        train_val_files = Utils.get_files_and_labels(cfg.TRAINING_FOLDER)
        test_files = Utils.get_files_and_labels(cfg.TESTING_FOLDER)
        
        # Now we need to split train images into validation and train parts
        # Train and Validation data
        train_val_labels = [path.parent.name for path in train_val_files]
        train_files, val_files = train_test_split(train_val_files, test_size=cfg.TEST_SIZE, random_state=cfg.RANDOM_STATE, \
                                                stratify=train_val_labels)
                                                """