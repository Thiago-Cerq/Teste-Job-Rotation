#Solução esta em Python.

numero = int(input("Digite um numero: ")) #valor de entrada
sequencia = [0,1] # iniciando o array com os 2 primeiros elementos da sequenciua de fibonnaci

while sequencia[-1] < numero: #Enquanto o ultimo numero da sequencia for menor que a entrada faça:
    sequencia.append(sequencia[-1] + sequencia[-2]) #Soma os 2 ultimos numeros da sequencia enquanto a antrada for menor que o ultimo numero

if numero in sequencia: #Se a sequencia entiver no meu array ele pertence a sequencia
    print(f"0 numero {numero} pertence à sequência de Fibonacci!")
else: #Se não, ele não pertence
    print(f" O numero {numero} não pertence à sequência de Fibonacci!")
