import pandas as pd
import numpy
import openpyxl
import plotly.express as px

# Passo 1: Importar a base de dados
tabela = pd.read_csv("telecom_users.csv")

# Informação que não te ajuda te atrapalha

# Passo 2: Visualizar a base de dados
#   Entender as informações que você tem disponível
#       Descobrir as cagadas da base de dados

# excluir coluna inútil
# axis = 0 -> eixo da linha
# axis = 1 -> eixo da coluna

tabela = tabela.drop("Unnamed: 0", axis=1)
# print(tabela)

# Passo 3: Tratamento de dados
# informação do tipo incorreto - ajustar o TotalGasto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Informações vazias

#   axis = 0 -> eixo da linha
#   axis = 1 -> eixo da coluna

# colunas completamente vazias -> excluir
tabela = tabela.dropna(how="all", axis=1)

# linhas que tem alguma informação vazia
tabela = tabela.dropna(how="any", axis=0)

# informações do tipo das colunas
print(tabela.info())

# Passo 4: Análise inicial dos dados
# Como estão os cancelamentos? 26%
print(tabela["Churn"].value_counts())

# percentual
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Descobrir os motivos do cancelamento

# coluna = "Aposentado"

for coluna in tabela.columns:

    # etapa 1: criar o gráfico
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)

    # etapa 2: exibe o gráfico
    grafico.show()

""" Anlise dos gráficos

- Clientes que estão há pouco tempo estão cancelando muito
     - Pode tá fazendo alguma promoção que tá dando o ! mês de graça
     - O início do serviço pro cliente tá sendo muito confuso
     - A 1 experiencia do cliente tá ruim
     - Podemos criar incentivos nos primeiros meses

- Boleto eletrônico tem muito mais cancelmaneto do que as outras formas de pagamento
    - Oferecer desconto em outras formas de pagamento
    
- Clientes com contrato mensal tem muito mais chance de cancelar
    - Dá desconto para pagar anuidade

- Quantos mais serviços o cliente tem, menor a chance dele cancelar
    - Pode oferecer serviços extras quase de graça
    
- Cliente com mais linhas com família mairo tem menos chance de cancelar
    - 2 Linha de graça ou com desconto
"""