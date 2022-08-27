import pandas as pd 
df = pd.read_csv('amz_data.csv')
df.shape
df.fillna(0)
df.head()

category = df.groupby("Amazon-Internal Product Category").sum()["Order Net Total"]


category.drop_duplicates()
print(category)
category.plot.bar(figsize=(20,10))














