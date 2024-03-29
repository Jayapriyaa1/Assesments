# -*- coding: utf-8 -*-
"""LVADSUSR91-Jayapriyaa-IA2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AjUjl9BqEjPc7IZiCw3WSAeNCm1bMCz7
"""

import numpy as np
import pandas as pd

#1

import numpy as np

rgb_image = np.array([[[255,0,0],[0,255,0],[0,0,255]],[[255,255,0],[255,0,255],[0,0,255]],[[127,127,127],[200,200,200],[50,50,50]]])

for i in range(rgb_image.shape[0]):
    for j in range(rgb_image.shape[1]):
        r, g, b = rgb_image[i, j]
        rgb_image[i, j] = [int(0.2989 * r), int(0.5870 * g), int(0.1140 * b)]

print(rgb_image)

#2
health_arr=np.array

import numpy as np

def normalize_data(data):
    means = np.mean(data, axis=0)
    stds = np.std(data, axis=0)

    normalized_data = (data - means) / stds

    return normalized_data


health_data = np.array([[170, 70, 30],
                        [160, 65, 35],
                        [180, 80, 25]])


normalized_health_data = normalize_data(health_data)

print("Original data:")
print(health_data)
print("\nNormalized data:")
print(normalized_health_data)

#3
arr=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(arr)
print('flatten',arr.flatten())
print('two-d',arr.reshape(2,1,6))

#4
arr=np.array([[[1,5,6],[2,6,8],[3,4,5]],[[4,5,6],[5,7,8],[6,7,8]]])

#5

#6

#7

data={
    'NAME':['Alice','Bob','Charlie','David','Eve','Frank','Grace'],
    'AGE':[25,30,35,40,45,50,55],
    'CITY':['New york','Los Angeles','Chicago','Houston','Phoenix','Miami','Boston'],
    'DEPARTMENT':['HR','IT','FINANCE','MARKETING','SALES','IT','HR']

}
df=pd.DataFrame(data)
df1=df[(df['AGE']<45) & (df['DEPARTMENT'] =='HR')][['NAME','CITY']]
print(df1)

#8
data = {
    'Product':['Apples','Bananas','Cherries','Dates','Elderberries','Flour','Grapes'],
    'Category':['Fruit','Fruit','Fruit','Fruit','Fruit','Bakery','Fruit'],
    'Price':[1.20,0.50,3.00,2.50,4.00,1.50,2.00],
    'Promotion':[True,False,True,True,False,True,False]
}

df=pd.DataFrame(data)
avg=df['Price'].mean()
#print(avg)
#print(df)
df1=df[(df['Price']>avg) & (df['Category']=='Fruit') & (df['Promotion']==False)]
print(df1)

#9

#10
data={
    'Department':['Electronics','Electronics','Clothing','Clothing','Homegoods'],
    'Salesperson':['Alice','Bob','Charlie','David','Eve'],
    'Sales':[70000,50000,30000,40000,60000]
}
df=pd.DataFrame(data)
avg_sales_per_dept = df.groupby(['Department', 'Salesperson'])['Sales'].mean().reset_index()
avg_sales_per_dept['Rank'] = avg_sales_per_dept['Sales'].rank(ascending=False).astype(int)
avg_sales_per_dept = avg_sales_per_dept.sort_values(by='Rank')
print(avg_sales_per_dept)