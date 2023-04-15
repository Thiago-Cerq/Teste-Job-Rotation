## 5) Escreva um programa que inverta os caracteres de um string.

##IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

# Resolução:

```
##Solução esta em Python.

palavra = input('Digite uma palavra: ')  # entre com a plavra que quiser

palavraInvertida = '' #Iniciando a var da palavra ivertida

for i in range(len(palavra) - 1, -1, -1): #Criado um loop invers, i vai começar com o tamanho da palavra -1 ate o valor -1 
  palavraInvertida += palavra[i] #Adicionando cada letra começando da ultima para a primeira

print(f'String original: {palavra}')
print(f'String invertida: {palavraInvertida}')

```
