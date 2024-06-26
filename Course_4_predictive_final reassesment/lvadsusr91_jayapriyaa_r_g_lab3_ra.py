# -*- coding: utf-8 -*-
"""LVADSUSR91_JAYAPRIYAA_R_G_lab3_ra.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gT16eJzNohbYoZqiT5dj9HpVPi2uo34A
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix, recall_score, f1_score, precision_score,silhouette_score, davies_bouldin_score, calinski_harabasz_score,mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore")
from sklearn.impute import SimpleImputer

"""Read Data"""

df=pd.read_csv('/content/customer_segmentation.csv')
print(df)

"""Data Processing"""

#Handling null values and duplicates
n=df.isnull().sum()
print('Null values in the dataset:\n',n)
dd=df[df.duplicated()]
print('Duplicate rows in the datset:\n',dd)

#Handling outliers
plt.figure(figsize=(20,15))
sns.boxplot(df)
plt.show()

#Label Encoding

label_encoder = LabelEncoder()
categorical_columns = ['Education', 'Marital_Status', 'Dt_Customer']
for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

imputer = SimpleImputer(strategy='median')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

#Remove Outliers
# Use Isolation Forest to identify outliers
outlier_detector = IsolationForest(contamination=0.05, random_state=42)
outliers = outlier_detector.fit_predict(df_imputed)

# Remove outliers
df_cleaned = df_imputed[outliers == 1]

"""EDA"""

#Describing Data
print('Head of the dataset:\n',df_cleaned.head())
print('Tail of the dataset:\n',df_cleaned.tail())
print('Description of the dataset:\n',df_cleaned.describe())
print('Columns of the dataset:\n',df_cleaned.columns)
print('Shape of the data:\n',df_cleaned.shape)
print('Correleation of features:\n',df_cleaned.corr())

#Viz

sns.heatmap(df.corr())
plt.show()

from matplotlib import pyplot as plt
_df_4.plot(kind='scatter', x='ID', y='Year_Birth', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Education']
  ys = series['Marital_Status']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = _df_10.sort_values('Education', ascending=True)
_plot_series(df_sorted, '')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Education')
_ = plt.ylabel('Marital_Status')

"""Elbow Method"""

l=[]
pca=PCA(n_components=2)
df_pca_scaled=pca.fit_transform(df_cleaned)
scaler=MinMaxScaler()
df_scaled=scaler.fit_transform(df_pca_scaled)
print(df_scaled)
for i in range(1,11):
  ml=KMeans(n_clusters=i)
  op=ml.fit_predict(df_scaled)
  inertia_score=ml.inertia_
  l.append(inertia_score)
plt.plot(range(1,11),l,marker='o')

"""Model Training"""

ml=KMeans(n_clusters=3)
op=ml.fit_predict(df_scaled)
labels=ml.labels_
centroids=ml.cluster_centers_
plt.scatter(df_scaled[:,0],df_scaled[:,1],c=labels)
plt.scatter(centroids[:,0],centroids[:,1],marker='X',color='r')
plt.title('Clusters Formation')

"""Model Evaluation"""

s=silhouette_score(df_scaled,op)
d=davies_bouldin_score(df_scaled,op)
c=calinski_harabasz_score(df_scaled,op)

print('Silhouette Score:',s)
print('\nDavies Bouldin Score:',d)
print('\ncalinski_harabasz_score:',c)