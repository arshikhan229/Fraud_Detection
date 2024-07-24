# Fraud Detection

This project aims to detect fraudulent transactions using various machine learning techniques. It includes data downloading, preprocessing, model training, and evaluation.

## Project Structure

The project is divided into several modules for better organization and maintainability:

- `data_loader.py`: Handles data downloading and loading.
- `preprocessing.py`: Manages data preprocessing tasks such as handling missing values and scaling.
- `models.py`: Contains functions for defining and training machine learning models.
- `evaluation.py`: Includes functions for evaluating the models and generating reports.
- `main.py`: Orchestrates the workflow of the entire project.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd fraud_detection
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. (Optional) Set up Kaggle API credentials for downloading the dataset:
    ```sh
    mkdir ~/.kaggle
    cp kaggle.json ~/.kaggle/
    chmod 600 ~/.kaggle/kaggle.json
    ```

## Usage

1. Run the `main.py` script to execute the entire fraud detection pipeline:
    ```sh
    python main.py
    ```

## License

This project is licensed under the MIT License.
