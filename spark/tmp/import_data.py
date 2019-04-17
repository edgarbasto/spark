import pandas as pd

df = pd.read_excel('../files/base.xlsx', index_col=None, header=None, dtype={'period':str, 'consumption':int, 'price':float})
year = df[1][1]
df.dropna(axis=0, thresh=1, inplace=True)

df[1]
sleep(10)