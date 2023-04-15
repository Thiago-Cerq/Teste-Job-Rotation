## 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43

RJ – R$36.678,66

MG – R$29.229,88

ES – R$27.165,48

Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

# Solução:

```
#Solução esta em Python.

#Criando um dicionario como a Região e o valor arrecadado
faturamento_mensal = { 
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_mensal.values())  #Ultilizando o sum para somar todos os valores arrecadados

print("O faturamento em porcentagem:")

for estado, faturamento in faturamento_mensal.items(): #Iterando meu dict
    percentual = faturamento / faturamento_total * 100 #Calculando a porcentagem do faturamento
    print(f'{estado}: {percentual:.2f}%') #Mostrando o faturamento em porcentagem com seu devido mes
```
