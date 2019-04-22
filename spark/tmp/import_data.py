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
        #meses.index(getattr(row, 'Descritivo'))
        mes = meses.index(getattr(row, 'Descritivo')) + 1
        print('Mês: {}'.format(mes))
    except ValueError:
        if mes >= 1 and mes <= 12:
            try:
                #periodo.index(getattr(row, 'Descritivo'))
                if (periodo.index(getattr(row, 'Descritivo')) is not None):
                    print('Para o {} mes, periodo: {}, consumo: {}, preço: {}'.format(mes, getattr(row, 'Descritivo'), getattr(row, 'Consumo'), getattr(row, 'Preco')))
                    type(getattr(row, 'Consumo'))
                    type(getattr(row, 'Preco'))
            except ValueError:
                print('')
        #False        
    #print('Para o {} mes, periodo: {}, consumo: {}, preço: {}'.format(mes, getattr(row, 'Descritivo'), getattr(row, 'Consumo'), getattr(row, 'Preco')))



   

df[1]