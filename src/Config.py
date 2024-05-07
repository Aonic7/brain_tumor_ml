import os
import torch

class Config:
    # Different modes
    DATA_MODES = ['train', 'val', 'test']
    RESCALE_SIZE = 224
    BATCH_SIZE = 16
    
    # Cuda mode
    DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    
    # MEANS
    MEANS = None
    
    # define folders for input
    PROJECT_DIR = r"D:\Thesis\Project_Brain Tumor\brain_tumor_ml"
    RAW_DIR = os.path.join(PROJECT_DIR, 'data', 'raw')
    BASE_DIR = os.path.join(PROJECT_DIR, 'data', 'processed')
    
    TRAINING_FOLDER = os.path.join(BASE_DIR, 'Training')
    TESTING_FOLDER = os.path.join(BASE_DIR, 'Testing')
    VAL_FOLDER = os.path.join(BASE_DIR, 'Validation')
    
    # define classes in the training folder
    CLASSES = ['glioma', 'meningioma', 'notumor', 'pituitary']
    
    #define path for output
    BASE_DIR_OUT = os.path.join(PROJECT_DIR, 'src')
    MODEL_FOLDER = os.path.join(BASE_DIR_OUT, 'models')
    
    # Test size
    TEST_SIZE = 0.25
    RANDOM_STATE = 42
