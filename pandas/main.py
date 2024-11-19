import pandas as pd

df = pd.read_csv('GoogleApps.csv')
# df.info()
#1.1
# print(df['App']) # Photo Editor & Candy Camera & Grid & ScrapBook
# print(df) #LIFESTYLE
# print(df) #12 rows & 
# print(df.describe()) # mean(size) = 22.769578, max(price) = 400.000000, mean(installs) = 8.662313e+06
# print(df['Size'].median) # median(size) = 19.000000
# print(df['Installs'].median) # median(Installs) = 10000.0
# a = round(df['Installs'].median(), 0)
# print(a)
# print(df['Size'].mean())
#2.1
# print(df[(df['Type'] == 'Paid')]['Price'].min())
# print(df [ df['Reviews'] & df['Type'] == 'Paid' ].max())
# a = df['Reviews']
# b = df['Type'] == 'Paid'
# print(a)

# print(df.groupby(by = 'Type')['Reviews'].max())

# a = 44893888 - 190086
# print(a)

# print(df [ df['Content Rating'] ])
# a = round(df.groupby(by = 'Content Rating')['Size'].min(), 3)
# print(a)


# a = df['Reviews'].max()
# new_df = df [df['Reviews'] == a]
# b = new_df['App']
# print(new_df)

# new_df = df [df['Price'] >= 20]
# new_df = df [df['Installs'] >= 10000]
# print(new_df)
# print(round(new_df['Rating'].mean(), 2))
new_dfs = df [(df['Price'] >= 20) & (df['Installs'] >= 10000)]
print(new_dfs['Rating'].mean())











# print(df.describe())
# print(df)
# print(df['App'])
# print(df['App'].head(10)) #tail end
# print(df['Price'].max) # mean, median, min, max

# print(df['Rating'] >= 4)
# print(df [ df['Rating'] >= 4 ])
# print(df [ df['Category'] == 'FAMILY' ])
# n_df = print(df [ df['Type'] == 'Paid' & 'Free'])
# print(n_df)
# print(df [ df['Type'] == 'Paid'])

