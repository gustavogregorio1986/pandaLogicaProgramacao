import pandas as pd

dados = { 'produto:': ['A','B', 'C', 'D'],
          'quantidade': [10,5,0, 10],
           'preco': [100, 200, 150, 120] }

df = pd.DataFrame(dados)

def categorizar_produto(row):
    if row['quantidade'] == 0:
        return 'Esgotado'
    elif row['quantidade'] < 10:
        return 'Baixo estoque'
    else:
        return 'Em estoque'

df['categoria'] = df.apply(categorizar_produto, axis=1)
print(df)