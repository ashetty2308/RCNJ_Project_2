import pandas as pd
import numpy as np

# 1

medals_df = pd.read_csv('medals.csv')
# print(medals_df)

# Dimension: 2311 rows x 8 columns

norway = medals_df.loc[(medals_df['NOC'] == 'NOR')]
# print(norway)
# norway.to_csv('norway.csv')

olympic_years = norway['Year'].unique()
# print(sorted(olympic_years))


# Get number of medals Norway earned at each Olympic Games
print((norway['Year'].value_counts()))

'''
1994    26
2002    25
1998    25
1992    20
2006    19
1924    17
1952    16
1964    15
1928    15
1936    15
1968    14
1972    12
1980    10
1948    10
1932    10
1984     9
1976     7
1960     6
1988     5
1956     4
'''

# Norway obtained the highest amount of medals at the 1994 Olympic Games


# 2

print("")
print("********************************************************************")
print("")
inputDf = [['white', 'pen', 5.56, 4.75], ['red', 'pencil', 4.24, 4.12], ['green', 'pencil', 2.50, 1.60],
           ['red', 'ashtray', 0.56, 0.75], ['green', 'pen', 2.83, 5.15], ['white', 'ashtray', 6.44, 4.00]]

my_df = pd.DataFrame(inputDf, columns=['Color', 'Object', 'Price 1', 'Price 2'])

total_col2_sum = my_df['Price 2'].sum()
mean_col1 = my_df['Price 1'].mean()
range_col1 = my_df['Price 1'].max() - my_df['Price 1'].min()

print(my_df)
print("")
print('Price 2 Sum:', total_col2_sum)
print('Price 1 Mean:', mean_col1)
print('Price 1 Range:', range_col1)

# 3

print("")
print("********************************************************************")
print("")
df = pd.DataFrame(np.random.rand(500, 5), columns=['A', 'B', 'C', 'D', 'E'])
df['A'] = np.random.randint(1, 1000, size=len(df))
df['B'] = np.random.randint(1, 1000, size=len(df))
df['C'] = np.random.randint(1, 1000, size=len(df))
df['D'] = np.random.randint(1, 1000, size=len(df))
df['E'] = np.random.randint(1, 1000, size=len(df))

df.to_csv('dataframe_csv_export.csv')

# Summary Statistics
print(df.describe())
print("")
print('Standard deviation: ', df.stack().std())
print("")
new_df = df[df > (df.stack().std() * 3)]
new_df_csv = new_df.to_csv('new_df_csv2.csv')
new_df = new_df.fillna(0.0)
print(new_df)

