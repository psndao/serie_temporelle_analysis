📄 README.md : Prédiction de la Variation du Cours d’une Action (Apple - AAPL)
📌 Objectif :
Ce projet a pour but de prédire la variation quotidienne du cours d’une action (Apple Inc. - AAPL) à partir de données historiques récupérées via l’API Alpha Vantage.
Deux approches sont comparées :

Régression : prédire le prix de clôture du lendemain.

Classification : prédire si le prix va monter ou baisser le lendemain.

🛠️ Technologies utilisées :
Python 3.12

pandas

numpy

scikit-learn

requests

yfinance

API Alpha Vantage (clé gratuite)

🗂️ Structure du projet :

serie_temporelle_analysis/
│
├── data/                    # Contient AAPL.csv et AAPL_preprocessed.csv
├── extract.py               # Téléchargement automatique via Alpha Vantage 
├── preprocess.py           # Préparation des données (Target = hausse ou baisse)
├── regression_model.py     # Modèle de régression (Linear Regression)
├── classification_model.py # Modèle de classification (RandomForestClassifier)
├── main.py                  # Pipeline complet
├── requirements.txt         # Librairies nécessaires
└── README.md                # Ce fichier de documentation
