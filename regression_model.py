import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def train_regression_model(df):
    X = df[['open', 'high', 'low', 'close', 'volume']]  
    y = df['close'].shift(-1)  # prédire la clôture du jour suivant
    df = df.dropna()
    X = X[:-1]
    y = y[:-1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"📉 MSE (régression) : {mean_squared_error(y_test, y_pred)}")

if __name__ == "__main__":
    df = pd.read_csv('data/AAPL_preprocessed.csv')
    train_regression_model(df)

