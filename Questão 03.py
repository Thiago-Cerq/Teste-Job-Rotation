#Solução esta em Python.

import json

with open('faturamento_mensal.json', 'r') as f: #Carregando os dados para meu array
    dados = json.load(f)


faturamentoDiario = dados['faturamento_diario'] #Pegando o faturamento diario


mediaMensal = sum(faturamentoDiario) / len(faturamentoDiario) # Calculando a media valo total/quantidade de dias


menorValor = faturamentoDiario[0] #Inicializa as variáveis para o menor valor
maiorValor = faturamentoDiario[0] #Inicializa as variáveis para o maior valor


diasAcimaDaMedia = 0 #Inicializa a variável para os dias com faturamento acima da média


for valor in faturamentoDiario: #Percorrendo o Array e verificando qual o menor valor obtido
    if valor < menorValor:
        menorValor = valor
    if valor > maiorValor: #Percorrendo o Array e verificando qual o maior valor obtido
        maiorValor = valor
    if valor > mediaMensal: #Percorrendo o Array e verificando quais dias ficaram acima da media
        diasAcimaDaMedia += 1


print('Maior valor de faturamento:', maiorValor)
print('Menor valor de faturamento:', menorValor)
print('Número de dias em que o faturamento ficou acima da media:', diasAcimaDaMedia)
