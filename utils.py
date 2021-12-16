import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import ParameterGrid
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

corpus_oil_price_resampled=pd.read_csv("data/corpus_oil_price_resampled2.csv", index_col=0)
corpus_alternative_energies_resampled=pd.read_csv("data/corpus_alternative_energies_resampled2.csv", index_col=0)

oil_price=pd.read_csv("data/oil_prices.csv", index_col=0)
corpus_oil_price_resampled2 = corpus_oil_price_resampled.merge(oil_price, on="date_published")
corpus_oil_price_resampled2.drop(columns=['baseline_sentiment'])

corpus_oil_price_resampled2.drop(corpus_oil_price_resampled2.tail(3).index,inplace=True)
corpus_oil_price_resampled2['Brent-1'] = corpus_oil_price_resampled2['Brent'].shift(1)
corpus_oil_price_resampled2['vader_sentiment-1'] = corpus_oil_price_resampled2['vader_sentiment'].shift(1)
corpus_oil_price_resampled2.drop(index='2009-11-01')

corpus_oil_price_resampled2.dropna(inplace=True)
X = corpus_oil_price_resampled2[['vader_sentiment-1', 'interaction_term']]
y = corpus_oil_price_resampled2['Brent']

train_size = int(0.85 * y.shape[0])
X_train = X[:train_size]
y_train = y[:train_size]
X_test = X[train_size:]
y_test = y[train_size:]

parameters = {'n_estimators': [50, 100, 200], 'max_depth': [2, 10, 15, 50,100]}
random_forest = RandomForestRegressor(random_state= 42) 
cv = GridSearchCV(random_forest, param_grid = parameters, verbose=10)
rf_model = cv.fit(X_train, y_train)   

size = int(0.85 * corpus_oil_price_resampled2.shape[0])
corpus_oil_price_resampled2_2 = corpus_oil_price_resampled2[size:]
corpus_oil_price_resampled2_2['date'] = corpus_oil_price_resampled2_2.index
y_pred = rf_model.predict(X_test)
corpus_oil_price_resampled2_2['y_pred'] = y_pred















