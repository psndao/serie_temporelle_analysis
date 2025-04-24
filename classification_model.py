import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def train_classification_model(df):
    X = df[['open', 'high', 'low', 'close', 'volume']]
    y = df['Target']  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"Accuracy (classification) : {accuracy_score(y_test, y_pred)}")

if __name__ == "__main__":
    df = pd.read_csv('data/AAPL_preprocessed.csv')
    train_classification_model(df)

