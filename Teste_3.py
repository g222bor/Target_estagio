#3
# O menor valor de faturamento ocorrido em um dia do mês; 
# O maior valor de faturamento ocorrido em um dia do mês; 
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 


#Importando a biblioteca json e pandas
import json
import pandas as pd 
menor_valor = 0
maior_valor = 0
dias_faturamento = 0

#Chamando o arquivo "dados.json" que foi disponibilzado
with open("dados.json") as meu_json:
    dados = json.load(meu_json)

#Criando um dataframe no pandas com o JSON
df_dados = pd.DataFrame(dados)

#Visualização do dataframe
#print(df_dados)

#Verificando o dataframe, não há valores nulos, somente valores 0
#df_dados.info()

#Localizando os valores 0 na coluna "valor"
df_dados.loc[df_dados['valor'] == 0]

#Criando um novo dataframe com os dias em que o "valor" é 0
df_remover_zeros = df_dados.loc[df_dados['valor'] == 0]

#Resulta em um dataframe em que foi retirado todos os valores 0
df_final = df_dados.drop(df_remover_zeros.index)

#Média dos valores
df_final['valor'].mean()

#Valor mínimo
df_final['valor'].min()
menor_valor = df_final['valor'].min()

#Valor máximo
df_final['valor'].max()
maior_valor = df_final['valor'].max()

#Localizando no dataframe os valores em que "valor" é maior que a média mensal
df_dados.loc[df_dados['valor'] > df_final['valor'].mean()]

#Guardando em um novo dataframe
df_dados_faturamento_diario_mensal = df_dados.loc[df_dados['valor'] > df_final['valor'].mean()]

#Contagem
df_dados_faturamento_diario_mensal.shape[0]
dias_faturamento = df_dados_faturamento_diario_mensal.shape[0]

#Formatacao do valor final
def formatar(valor):
    return f"R${valor:,.2f}". format(valor)


print(f"O menor valor de faturamento diário, no mês vigente, foi de: {formatar(menor_valor)}")
print(f"O maior valor de faturamento diário, no mês vigente, foi de: {formatar(maior_valor)}")
print(f"A quantidade de dias em que o faturamento diário ultrapassou a média mensal: {dias_faturamento} dias")


#O menor valor de faturamento diário, no mês vigente, foi de: R$373.78
#O maior valor de faturamento diário, no mês vigente, foi de: R$48,924.24
#A quantidade de dias em que o faturamento diário ultrapassou a média mensal: 10 dias

