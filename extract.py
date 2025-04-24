import requests
import pandas as pd

API_KEY = 'ZKYQJPZ7IYLA4CCC'  
SYMBOL = 'AAPL'
FUNCTION = 'TIME_SERIES_DAILY'  
OUTPUTSIZE = 'full'

url = (
    f"https://www.alphavantage.co/query?function={FUNCTION}"
    f"&symbol={SYMBOL}&outputsize={OUTPUTSIZE}&apikey={API_KEY}&datatype=csv"
)

response = requests.get(url)

if response.status_code == 200:
    with open('data/AAPL.csv', 'wb') as f:
        f.write(response.content)
    print("Données téléchargées avec succès dans data/AAPL.csv")
else:
    print("Erreur de téléchargement :", response.status_code)
