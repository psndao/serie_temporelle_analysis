from extract import download_data
from preprocess import preprocess_data
from regression_model import train_regression_model
from classification_model import train_classification_model
import pandas as pd

def main():
    ticker = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2024-12-31'
    
    print("Téléchargement des données...")
    df_raw = download_data(ticker, start_date, end_date)
    df_raw.to_csv('data/AAPL.csv', index=False)
    
    print("Préparation des données...")
    df_preprocessed = preprocess_data('data/AAPL.csv')
    df_preprocessed.to_csv('data/AAPL_preprocessed.csv', index=False)

    print("Entraînement du modèle de régression...")
    train_regression_model(df_preprocessed)
    
    print("Entraînement du modèle de classification...")
    train_classification_model(df_preprocessed)

if __name__ == "__main__":
    main()
