# -*- coding: utf-8 -*-
"""EDA

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1slTyfT8HYbsGEAyiEVZ3Avb4GeFUJKLF
"""

import numpy as np
import pandas as pd
import seaborn as sp

mydf=pd.read_csv('/content/application_record.csv')

mydf.shape

mydf.info()

mydf.isnull()

mydf.describe()

import matplotlib.pyplot as plt

sp.boxplot(data=mydf)

df=mydf.dropna()
print(df)

mydf.info()

df.info()

correlation=df.corr()

sp.heatmap(correlation,annot=True)

sp.boxplot(data=df)

sp.pairplot(df.corr())

