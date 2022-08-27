import pandas as pd 
df = pd.read_csv('amz_data.csv')
df.shape
df.fillna(0)
df.head()

date_val = pd.DatetimeIndex(df['Order Date'])

df['Month'] = date_val.month 
df['Year'] = date_val.year 
df['Day'] = date_val.day 

month=df.groupby("Month").sum()["Order Quantity"]
month.plot.bar(figsize=(30,10))