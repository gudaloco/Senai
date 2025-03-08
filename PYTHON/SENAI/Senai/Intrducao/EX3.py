"""
EX3 - Crie um programa que calcule a potência de um número
Criado por: Gustavo Galdino
Data: 08/02/25
"""

num = int(input("Digite o primeiro numero: "))

sinal = input("Sinal aritmetico: ")

potencia = int(input("Digite o segundo numero:"))

if sinal == "+" : resultadom = num + potencia
if sinal == "-" : resultadom = num - potencia
if sinal == "/" : resultadom = num / potencia
if sinal == "//" : resultadom = num // potencia
if sinal == "X" : resultadom = num * potencia
if sinal == "**" : resultadom = num ** potencia
else: print("aoba")

resultado = num ** potencia

print(num,sinal,potencia,"= ", resultadom)
exit()