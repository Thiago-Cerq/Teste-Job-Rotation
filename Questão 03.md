## 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

## IMPORTANTE:

a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da méd

## Solução:

```
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

```
