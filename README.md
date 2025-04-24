# Prédiction de la Variation Quotidienne du Cours de l'Action AAPL



## Objectif

Ce projet a pour but de prédire la variation quotidienne du cours de l’action **Apple Inc. (AAPL)** à partir de données historiques.  
Deux approches sont utilisées :  
- **Régression** : prédiction du prix de clôture du jour suivant.
- **Classification** : prédiction de la tendance (hausse ou baisse) du prix de clôture du lendemain.

---

## Technologies utilisées

- Python 3.12
- `pandas`, `numpy`
- `scikit-learn`
- `requests` (pour récupération via API Alpha Vantage)
- API Alpha Vantage (clé gratuite)

---

## Structure du projet
## Resultats
### Modèle de régression (LR)
MSE : 3.36

Le modèle de régression prédit le prix de clôture du lendemain à partir des valeurs du jour actuel.
Une MSE de 3.36 indique une erreur encore significative. Cette performance pourrait être améliorée par l’ajout d’indicateurs techniques (comme RSI, MACD, moyennes mobiles) ou par la création de variables laggées (fenêtres temporelles).

### Modèle de classification (RandomForestClassifier)
Accuracy : 52.96 %

Le modèle de classification prédit si le prix va monter ou baisser le lendemain.
Une accuracy de 52.96 % montre que le modèle dépasse légèrement le hasard (50 %), mais reste trop faible pour être fiable dans un contexte réel de trading. On pourrait améliorer les resultats par l'utilisation de modèles plus complexes comme XGBoost, SVM, ou LSTM.



## Installation

Clonez le projet :
```bash
git clone https://github.com/psndao/serie_temporelle_analysis.git
cd serie_temporelle_analysis

