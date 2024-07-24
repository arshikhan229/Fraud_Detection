from data_loader import load_data
from preprocessing import preprocess_data
from models import train_model
from evaluation import evaluate_model

def main():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == '__main__':
    main()
