#4
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
#que cada estado teve dentro do valor total mensal da distribuidora. 


#Importando as bibliotecas
import json
import pandas as pd 

#Definindo o valor de faturamento
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

#Importando o JSON
with open("dados.json") as meu_json:
    dados = json.load(meu_json)

#Criando df
df_dados = pd.DataFrame(dados)

#Visualizando df
print(df_dados)

#Guardando a soma total dos valores de vendas na variável total
df_dados['valor'].sum()
total = df_dados['valor'].sum()

#Calculando o porcentual por estado
percentual_sp = (sp / total)*100
percentual_rj = (rj / total)*100
percentual_mg = (mg / total)*100
percentual_es = (es / total)*100
percentual_outros = (outros / total)*100

#Imprimindo o resultado
print('Respectivos estados e sua representação de vendas % em relação ao total do mês vigente')
print('São Paulo: {0:.2f}%'.format(percentual_sp))
print('Rio de Janeiro: {0:.2f}%'.format(percentual_rj))
print('Minas Gerais: {0:.2f}%'.format(percentual_mg))
print('Espirito Santo: {0:.2f}%'.format(percentual_es))
print('Outros estados: {0:.2f}%'.format(percentual_outros))

#Respectivos estados e sua representação de vendas % em relação ao total do mês vigente
#São Paulo: 15.48%
#Rio de Janeiro: 8.37%
#Minas Gerais: 6.67%
#Espirito Santo: 6.20%
#Outros estados: 4.53%
