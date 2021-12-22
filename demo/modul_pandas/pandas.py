# I will be using Jupyter for this
# pip install pandas
# pip install jupyterlab
# start jupyter by running "jupyter notebook"

import pandas as pd

# wir lesen ein csv in einen dataframe
df = pd.read_csv('personen.csv')

# Dataframe ausgeben
print(df)

# Anzahl der Zeilen und Spalten
df.shape

# Ausgabe der Spalten
df.columns

# Nur die Ausgabe einer Spalte
df.FirstName
# oder
df['FirstName']

# Ausgabe mehrerer Spalten
df[['FirstName','LastName']]

# die ersten 10 Zeilen
df.head(10)

# die letzten 10 Zeilen
df.tail(10)


# Dataframes indizieren sich selbst:
# Ausgabe Column 1 Zeile 1 mit iloc
df.iloc[0][0]

# der Spalte Firstname mit loc
df.loc[0]['FirstName']

# value_counts()
# ein wenig wie group by
df['EmailPromotion'].value_counts()

# einen neuen DataFrame aus einem bestehenden
my_new_df = df[['FirstName','LastName']]

# Speichern - das Geheimnis liegt im Schlüsselwort "to_"
my_new_df.to

my_new_df.to_csv(r'mycsv.csv', index=False, header=True)