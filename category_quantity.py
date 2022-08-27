import pandas as pd 
df = pd.read_csv('amz_data.csv')
df.shape
df.fillna(0)
df.head()

date_val = pd.DatetimeIndex(df['Order Date'])

df['Month'] = date_val.month 
df['Year'] = date_val.year 
df['Day'] = date_val.day 

df['Month'] = pd.to_datetime(df['Month'])
month=df.groupby(["Amazon-Internal Product Category", "Month"]).count()
print(month)
month.plot.bar(figsize=(10,10))








