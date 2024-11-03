import pandas as pd

# Criando um DataFrame com uma coluna de números
numeros = pd.DataFrame({'Valores': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

# Contando números pares e ímpares
contagem = {
    'Pares': (numeros['Valores'] % 2 == 0).sum(),
    'Ímpares': (numeros['Valores'] % 2 != 0).sum()
}

# Exibindo os resultados
print(contagem)


