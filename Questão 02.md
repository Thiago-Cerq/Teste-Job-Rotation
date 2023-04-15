## 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

## Solução:


```
#Solução esta em Python.

numero = int(input("Digite um numero: ")) #valor de entrada
sequencia = [0,1] # iniciando o array com os 2 primeiros elementos da sequenciua de fibonnaci

while sequencia[-1] < numero: #Enquanto o ultimo numero da sequencia for menor que a entrada faça:
    sequencia.append(sequencia[-1] + sequencia[-2]) #Soma os 2 ultimos numeros da sequencia enquanto a antrada for menor que o ultimo numero

if numero in sequencia: #Se a sequencia entiver no meu array ele pertence a sequencia
    print(f"0 numero {numero} pertence à sequência de Fibonacci!")
else: #Se não, ele não pertence
    print(f" O numero {numero} não pertence à sequência de Fibonacci!")

```
