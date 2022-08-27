import pandas as pd 
df = pd.read_csv('amz_data.csv')
df.shape
df.fillna(0)
df.head()

(df.pivot_table(index='Year', columns='Amazon-Internal Product Category', 
               values='Order Quantity', aggfunc='sum', fill_value=0)
 .plot.bar(stacked=True, figsize=(20,10)))

