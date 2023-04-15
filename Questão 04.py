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
