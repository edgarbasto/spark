import pandas as pd

df = pd.read_excel('../files/base.xlsx', index_col=None, header=None, dtype={'period':str, 'consumption':int, 'price':float})
year = df[1][1]
df.columns = ['Descritivo', 'Consumo', 'Preco', 'Total']
df.dropna(axis=0, thresh=1, inplace=True)

mes=0

for row in df.itertuples(index=True, name='Teste'):
    meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
    periodo = ['Ponta', 'Cheio', 'Vazio', 'Super Vazio']
    try:
        meses.index(getattr(row, 'Descritivo'))
        mes = meses.index(getattr(row, 'Descritivo')) + 1
        #print('{} and {}'.format(mes, getattr(row+1, 'Descritivo')))
    except ValueError:
        False
         

    print('{} and {}'.format(getattr(row, 'Descritivo'), getattr(row, 'Consumo')))



df[1]