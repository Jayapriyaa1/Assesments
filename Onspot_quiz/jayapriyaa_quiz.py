# -*- coding: utf-8 -*-
"""Jayapriyaa_quiz

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18vdz-zf0xgFia0kT7-y5TsH7zYkB8ATD
"""

import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, precision_score, f1_score, recall_score
import time

mark = pd.read_csv('/content/DSAI-LVA-DATASET for Quiz.csv')
print(mark.head())

for i, rows in mark.iterrows():
    if rows['Pass'] == 'Yes' and rows['PreviousTestScore'] >= 75:
        mark.loc[i, 'Result'] = 'High'
    elif rows['Pass'] == 'Yes' and rows['PreviousTestScore'] < 75:
        mark.loc[i, 'Result'] = 'Low'
    elif rows['Pass'] == 'No':
        mark.loc[i, 'Result'] = 'Fail'
mark = mark.drop('Pass', axis=1)

print(mark.head())

parent_edu = ['Masters', 'Bachelor''s', 'College', 'High School', 'Not Educated']
mark['Parent_Education'] = np.random.choice(parent_edu, size = len(mark['StudyTime']))

mark = mark.drop('ParentEducation', axis=1)
print(mark.head())

mark_shuffled = mark.sample(frac=1, random_state=42).reset_index(drop=True)

train_size = int(0.7 * len(mark_shuffled))

train_set = mark_shuffled.iloc[:train_size]
test_set = mark_shuffled.iloc[train_size:]

train_set.to_csv('train.csv', index=False)
test_set.to_csv('test.csv', index=False)

test_df=pd.read_csv('/content/test.csv')
train_df=pd.read_csv('/content/train.csv')

lbl = LabelEncoder()
train_df['Parent_Education'] = lbl.fit_transform(train_df['Parent_Education'])

X_train = train_df.drop('Result', axis=1)
X_test = test_df.drop('Result', axis=1)
y_train = train_df['Result']
y_test = test_df['Result']

model_name = [
    ('Decision Tree Classifier', DecisionTreeClassifier()),
    ('K Nearest Neighbors', KNeighborsClassifier(n_neighbors=2)),
    ('SVM', SVC()),
    ('XGB Classifier', XGBClassifier(learning_rate=0.01, gamma=3))
]

results = {}
for name, model in model_name:
    start_time = time.time()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    time_taken = round((time.time() - start_time), 2)
    accuracy = accuracy_score(y_pred, y_test)
    results[name] = accuracy
    print(f'{name} \nAccuracy : {accuracy*100:.2f}% \nTime Taken: {time_taken} sec\n ')

# Plotting the results
model_plot = pd.DataFrame(results.values(), index=results.keys(), columns=['Accuracy'])
model_plot.plot(kind='barh')
plt.xlabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.show()