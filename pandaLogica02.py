import pandas as pd 

numeros = pd.DataFrame({'Valores': [3]})

def zero_ou_negativo_positivo(num):
    if num > 0:
        return 'positivo'
    elif num < 0:
        return 'Negativo'
    else:
        return 'zero'


numeros['categoria'] = numeros['Valores'].apply(zero_ou_negativo_positivo)

print(numeros)