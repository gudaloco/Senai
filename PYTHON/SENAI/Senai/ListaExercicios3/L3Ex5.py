"""
5. Escreva um programa que calcule a média geométrica entre três números informados pelo
usuário. Utilize o tipo de dados double.
Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""

num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
num3 = float(input("digite o terceiro número: "))

#media = (num1*num2*num3) ** (1/3)
media = pow(num1*num2*num3, 1/3)

print("Média geométrica: ", media)