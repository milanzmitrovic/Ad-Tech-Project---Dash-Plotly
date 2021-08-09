import pandas as pd

df = pd.read_csv('data/AD-Tech.csv')

df['date'] = pd.to_datetime(df['date'])

df.set_index(df['date'], inplace=True)

df.sort_index(inplace=True)

df['total_revenue'].astype(int)

# df['total_revenue'] = pd.to_numeric(df['total_revenue'], downcast='int')


