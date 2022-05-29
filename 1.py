import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('automobile.csv', delimiter=';', header=None)
df = pd.read_csv('automobile.csv', delimiter=';')
# print(df)
# nowa ramka
df1 = df[df['Price'] >= 10000]
grupa = df1.groupby(['Car model'])['Car model'].count()
# print(grupa)

# labels = df1['Car model'].unique()
# unikalne wartosci

plt.pie(grupa.values, labels=grupa.index, autopct='%.2f%%')
# plt.savefig('wykreszad1.png', format='png')
plt.show()
