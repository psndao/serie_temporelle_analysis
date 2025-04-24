import pandas as pd

def preprocess_data(filepath):
    df = pd.read_csv(filepath)
    # Vérification des colonnes
    print("Colonnes du fichier :", df.columns.tolist())
    
    # Création de la colonne Target : 1 si le prix monte demain, 0 sinon
    df['Target'] = (df['close'].shift(-1) > df['close']).astype(int)
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    df = preprocess_data('data/AAPL.csv')
    df.to_csv('data/AAPL_preprocessed.csv', index=False)
    print("Données prétraitées et sauvegardées dans data/AAPL_preprocessed.csv")
