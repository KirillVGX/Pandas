import pandas as pd

df = pd.read_csv('GoogleApps.csv')
# df.info()

# print(df.groupby(by = 'Type')['Reviews'].max())

# print(df['Category'].value_counts())

# print(df['Content Rating'].value_counts())
# print(round(868 / 318, 2))

# print(df.groupby(by = 'Type')['Rating'].mean())

# print(df [ df['Category'] == 'COMICS' ].max())
# print(df [ df['Category'] == 'COMICS' ].min())

# a = df['Rating'] == 4.5
# a = df [ (df['Category'] == 'FINANCE')]
# b = a [ a['Rating'] == 4.5 ]
# print(b ['Rating'].value_counts())
a = df [ df ['Category'] == 'FINANCE']

print((a['Rating'] >= 4.5).value_counts())