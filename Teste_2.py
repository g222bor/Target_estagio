#2
#Escreva um programa na linguagem que desejar onde, informado um número
#ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

#Definindo o método
numero = 0
a, b = 0

def sequencia_fibonacci(numero):
  a, b = 0, 1
  while b < numero:
    a, b = b, a + b
  if b == numero:
    return True
  else:
    return False

#Imprimindo
numero = int(input("Digite um numero para saber se o mesmo se encontra na sequencia de Fibonacci "))
if sequencia_fibonacci(numero):
  print(f"{numero} pertence a sequencia de Fibonacci.")
else:
  print(f"{numero} nao pertence a sequencia de Fibonacci.")