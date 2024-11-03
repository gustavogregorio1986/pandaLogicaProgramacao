import pandas as pd

# Criando a tabuada do 1 ao 10
numeros = range(1, 11)

# Função para gerar a tabuada
def gerar_tabuada(n):
    return [n * i for i in numeros]

# Criando um DataFrame para armazenar as tabuadas
dados = {str(n): gerar_tabuada(n) for n in numeros}
df = pd.DataFrame(dados, index=numeros)

print(df)
