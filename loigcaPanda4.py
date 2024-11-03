import pandas as pd

# Função para calcular o fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Criando um DataFrame com números de 0 a 10
numeros = pd.DataFrame({'Numero': range(11)})

# Aplicando a função fatorial
numeros['Fatorial'] = numeros['Numero'].apply(fatorial)

print(numeros)
