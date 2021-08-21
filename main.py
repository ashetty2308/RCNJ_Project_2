import pandas as pd
import numpy as np
from scipy import stats


medals_csv = pd.read_csv('medals.csv')
print(medals_csv)


# 1



# 2

# 3

df = pd.DataFrame(np.random.rand(500, 5), columns =['A', 'B', 'C','D','E'])
df['A'] = np.random.randint(1,1000, size=len(df))
df['B'] = np.random.randint(1,1000, size=len(df))
df['C'] = np.random.randint(1,1000, size=len(df))
df['D'] = np.random.randint(1,1000, size=len(df))
df['E'] = np.random.randint(1,1000, size=len(df))

df.to_csv('dataframe_csv_export.csv')

# Summary Statistics
# print(df.describe())

print('Standard deviation: ', df.stack().std())

new_df = df[df>(df.stack().std()*3)]
new_df_csv = new_df.to_csv('new_df_csv2.csv')

new_df = new_df.fillna(0.0)
print(new_df)
