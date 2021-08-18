import pandas as pd
import numpy as np

medals_csv = pd.read_csv('medals.csv')
print(medals_csv)


#1

#2

#3

df = pd.DataFrame(np.random.rand(500, 5), columns =['A', 'B', 'C','D','E'])
df['A'] = np.random.randint(1,1000, size=len(df))
df['B'] = np.random.randint(1,1000, size=len(df))
df['C'] = np.random.randint(1,1000, size=len(df))
df['D'] = np.random.randint(1,1000, size=len(df))
df['E'] = np.random.randint(1,1000, size=len(df))

df.to_csv('dataframe_csv_export.csv')

print(df)

