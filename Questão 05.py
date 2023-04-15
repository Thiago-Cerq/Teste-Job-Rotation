##Solução esta em Python.

palavra = input('Digite uma palavra: ')  # entre com a plavra que quiser

palavraInvertida = '' #Iniciando a var da palavra ivertida

for i in range(len(palavra) - 1, -1, -1): #Criado um loop invers, i vai começar com o tamanho da palavra -1 ate o valor -1 
  palavraInvertida += palavra[i] #Adicionando cada letra começando da ultima para a primeira

print(f'String original: {palavra}')
print(f'String invertida: {palavraInvertida}')
