"""
1. Faça um programa que pergunte a idade do usuário e informe se ele pode ou não se aposentar.
Obs. Uma pessoa só pode se aposentar quando atingir 60 anos (idade mínima).
Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""

idade = int(input("Digite a sua idade: "))

if idade >= 60:
    print("Você pode se aposentar")
else: print("Infelizmente, você ainda não pode se aposentar.")