import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('automobile.csv', delimiter=';')
# nowa ramka
df1 = df[df['Horsepower'] >= 100]
grupa = df1.groupby(['Car model'])['Car model'].count()

xlabels = grupa.index
# x_len = len(xlabels)
ylabels = grupa.values

plt.figure(figsize=(20, 5))
plt.bar(xlabels, ylabels)
plt.xlabel('marka samochodu')
plt.ylabel('ilosc samochodow')
plt.tight_layout()

plt.show()
