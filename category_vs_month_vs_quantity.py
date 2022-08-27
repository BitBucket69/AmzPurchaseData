import pandas as pd 
df = pd.read_csv('amz_data.csv')
df.shape
df.fillna(0)
df.head()

(df.pivot_table(index='Month', columns='Amazon-Internal Product Category', 
               values='Order Net Total', aggfunc='sum', fill_value=0)
 .plot.bar(stacked=True, figsize=(20,10)))

