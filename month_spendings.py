import pandas as pd 
df = pd.read_csv('amz_data.csv')
df.shape
df.fillna(0)
df.head()

date_val = pd.DatetimeIndex(df['Order Date']) #used to extract month from 'Order Date'

df['Month'] = date_val.month 
df['Year'] = date_val.year 
df['Day'] = date_val.day 

print(date_val.month)
DataAsList = [8,  8,  8,  8,  8,  8,  6,  6,  6,  5,  5,  5,  5,  4,  4,  4,  4,
             4,  4,  4,  3,  3,  3,  3,  2,  2,  2,  2,  1,  1, 12, 12, 12, 12,
            12, 11, 11, 11, 11, 10, 10, 10, 10,  9,  9,  9,  9,  9,  9,  9,  9,
             8,  8,  6,  5,  1, 12, 12, 12, 12, 12,  9,  9,  9,  9,  1,  1,  1,
             1,  1,  1,  1,  1,  1, 11, 10, 10, 10,  8,  8,  7,  6,  5,  5,  4,
             4,  4,  3,  3,  3,  3,  2,  2, 12, 12, 12, 12, 12]

df = df.append({"MONTH": DataAsList}, ignore_index=True)
df.to_csv("amz_data.csv", index=False)

month=df.groupby("Month").sum()["Order Net Total"]
month.plot.bar(figsize=(20,20))





