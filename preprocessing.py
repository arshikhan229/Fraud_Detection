import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler

def preprocess_data(df):
    # Handle missing values, scaling, and splitting
    df['Class'] = df['Class'].astype('category')
    X = df.drop('Class', axis=1)
    y = df['Class'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = RobustScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test
