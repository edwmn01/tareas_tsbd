import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from prophet import Prophet

from datetime import datetime


def modelo_kmeans(df):
    imputer = SimpleImputer(strategy='mean')
    X = imputer.fit_transform(df[['total', 'contracts']])
    
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)
    
    return df


def modelo_prophet(df):
    df['ds'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str) + '-01')
    df['y'] = df['total']
    
    model = Prophet()
    model.fit(df[['ds', 'y']])
    
    future = model.make_future_dataframe(periods=12)
    forecast = model.predict(future)
    
    return model, forecast


def modelo_regresion_logistica(df):
    X = df[['total', 'contracts']]
    
    if df['year'].nunique() > 1:
        df['year_binary'] = np.where(df['year'] < df['year'].median(), 0, 1)
        y = df['year_binary']
    else:
        return None
    
    imputer = SimpleImputer(strategy='mean')
    model = Pipeline([('imputer', imputer), ('logistic', LogisticRegression())])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy


def modelo_PCA(df):
    imputer = SimpleImputer(strategy='mean')
    X = imputer.fit_transform(df[['total', 'contracts']])
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(X)
    return pca_result



def modelo_isolation_forest(df):
    model = IsolationForest(contamination=0.01, random_state=42)
    df['anomaly'] = model.fit_predict(df[['total', 'contracts']])

    return df