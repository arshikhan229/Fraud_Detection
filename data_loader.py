import pandas as pd
import os

def load_data():
    if not os.path.exists('transaction_data.csv'):
        # Add code to download and unzip data from Kaggle
        pass
    df = pd.read_csv('transaction_data.csv')
    return df
