import pandas as pd

# 1. Carregar dados de vendas
df = pd.read_csv("vendas.csv")

# 2. Limpeza de dados
# Remover linhas com valores nulos
df.dropna(inplace=True)

# Corrigir qualquer erro de tipo na coluna 'quantidade' e 'preco_unitario'
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce')
df['preco_unitario'] = pd.to_numeric(df['preco_unitario'], errors='coerce')

# Remover linhas onde a quantidade ou o preço seja nulo ou zero
df.dropna(subset=['quantidade', 'preco_unitario'], inplace=True)
df = df[(df['quantidade'] > 0) & (df['preco_unitario'] > 0)]

# 3. Transformação de dados
# Calcular o total de venda para cada linha
df['total_venda'] = df['quantidade'] * df['preco_unitario']

# Extrair o mês e ano da coluna 'data' para agrupar
df['data'] = pd.to_datetime(df['data'])
df['mes'] = df['data'].dt.month
df['ano'] = df['data'].dt.year

# 4. Análise de dados
# Agrupar as vendas por 'produto', 'ano' e 'mes' para obter o total de vendas por mês
resumo_mensal = df.groupby(['produto', 'ano', 'mes'])['total_venda'].sum().reset_index()

# 5. Exportar o resumo para um novo CSV
resumo_mensal.to_csv("resumo_vendas_mensal.csv", index=False)

print("Automação concluída! Resumo de vendas mensal exportado para 'resumo_vendas_mensal.csv'.")
