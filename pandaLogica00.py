import pandas as pd

dados = {'nome': ['Alice','Bruno', 'Carla', 'Daniel','Eva'],
         'idade':[17, 25, 30, 16, 19]}

df = pd.DataFrame(dados)

df_maiores_de_18 = df[df['idade'] > 18]

print(df_maiores_de_18)