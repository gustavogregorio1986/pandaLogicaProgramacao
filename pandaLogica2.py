import pandas as pd

numeros = []

for i in range(41):
    numeros.append(i)

df = pd.DataFrame(numeros, columns=['numero'])

# Função para verificar par ou ímpar
def par_ou_impar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

df['paridade'] = df['numero'].apply(par_ou_impar)

print(df)