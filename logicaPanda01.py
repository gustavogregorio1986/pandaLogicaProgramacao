import pandas as pd

dados = {'nome': ['luiz', 'paulo', 'marcos', 'pedro', 'laio', 'ana', 'bia'],
         'idade': [23, 43, 11, 65, 12, 10, 32]}

df = pd.DataFrame(dados)

df_maiores_de_18 = df[df['idade'] > 18]

df_menores_de_18 = df[df['idade'] < 18]

print(df_maiores_de_18)

print(df_menores_de_18)
