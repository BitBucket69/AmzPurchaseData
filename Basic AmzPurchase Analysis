import pandas as pd 
df = pd.read_csv('amz_data.csv')
df.shape
df.fillna(0)
df.head() 

print('Total Amnt Spent On Amz:')
print(df["Order Net Total"])
print()

print('Mean Amnt Spent On Amz:')
print(df["Order Net Total"].mean())
print()

print('Median Amnt Spent On Amz:')
print(df["Order Net Total"].median())
print()

print('Total Tax and Shipping Amnt Spent On Amz:')
print(df["Item & Shipping Tax"].sum())
print()

print('Percent of Tax Paid on Amz wrt Bill:')
print(df["Item & Shipping Tax"].sum()/df["Order Net Total"].sum()*100)
print()

df['Order Date'] = pd.to_datetime(df['Order Date'])
df.head()

df.plot.bar(x='Order Date', y='Order Net Total', rot=90, figsize=(20,10))

daily_orders = df.groupby("Order Date").sum()["Order Net Total"]
df.head()
