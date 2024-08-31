import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

def barchart(df, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(df[xlabel], df[ylabel])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f"{xlabel} against {ylabel}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


df = pd.read_csv('train.csv')

# barchart(df, 'Survived', 'Fare')  # This shows that there is a correlation between fare and survival rate.

df['Embarked'] = df['Embarked'].replace({
    'C': 1,
    'Q': 2,
    'S': 3
})

print(df.head())
# plt.figure(figsize=(12, 6))
# sb.heatmap(df.corr() > 0.7, annot=True, cbar=False)  # shows a heatmap, displaying values where there is correlation
# plt.show()