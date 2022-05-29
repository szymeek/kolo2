import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# wykres kolumnowy na podstawie slownika

dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Belhi', 'Brasilia', 'Warszawa'],
        'Populacja': [11190826, 1303171035, 207847528, 38675467],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa']}

df = pd.DataFrame(dane)
print(df)
# grupuje nam wartosci na danym kontynencie
grupa = df.groupby('Kontynent')

# tworzy liste unikalnych etykiet
etykiety = list(grupa.groups.keys())

# sumuje populacje w danej grupie
wartosci = list(grupa.agg('Populacja').sum())

# to samo co up tylk szybciej
sum = df.groupby(['Kontynent'])['Populacja'].sum()

plt.bar(x=etykiety, height=wartosci, color=['red', 'green', 'blue'])
plt.xlabel('Kontynenty')
plt.ylabel('Populacja na kontynentach')
plt.show()
