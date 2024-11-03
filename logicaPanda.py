import pandas as pd

dados = {"nome":['marcos',"pedro","marcio", "michele",'michel','augusto'],
         "iidade": [23,43,12,54,15,43]}

df = pd.DataFrame(dados)

print(df)