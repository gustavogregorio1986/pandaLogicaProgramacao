import pandas as pd

dados = {"nome":['marcos',"pedro","marcio", "michele",'michel','augusto'],
         "idade": [23,43,12,54,15,43],
         "cpf":['1234567890','0987654321','7890654123','09874561234','9807612345','0978651234']}

df = pd.DataFrame(dados)

print(df)