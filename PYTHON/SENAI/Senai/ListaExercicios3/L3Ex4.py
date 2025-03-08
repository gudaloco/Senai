"""
4. Escreva um programa que solicite ao usuário dois números e exiba a soma, subtração,
multiplicação e divisão entre eles. Utilize o tipo de dados double.
Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multipicacao = num1 * num2
divisao = num1 / num2

print("soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicação: ", multipicacao)
print(f"Divisão: {divisao:.3}")