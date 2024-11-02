import pandas as pd

numeros = []

for i in range(41):
    numeros.append(i)

df = pd.DataFrame(numeros, columns=['numero'])
print(df)