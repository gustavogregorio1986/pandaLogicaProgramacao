import pandas as pd

dados = {'nome':['pedro','marcos','laio','marcelo', 'ligia'],
         'idade':[32,12,22,17,23],
         'sexo':['m','m','m','m','f']}

df = pd.DataFrame(dados)

df_maiores_de_18_masculino = df[(df['idade'] > 18) & (df['sexo'] == 'm')]

print(df_maiores_de_18_masculino)