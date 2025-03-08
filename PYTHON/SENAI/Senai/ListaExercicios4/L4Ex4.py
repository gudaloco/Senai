"""
4. Faça um programa que leia calcule o frete com base no peso informado pelo usuário.
Obs. A empresa de entregas cobra frete de acordo com o peso da mercadoria. Se o peso for até
5 kg, o frete é R$ 20,00. Se o peso for acima de 5 kg e até 10 kg, o frete é R$ 40,00. Para pesos
acima de 10 kg, o frete é R$ 60,00.
Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""

peso = float(input("Digite o peso da mercadoria: "))

if peso <= 5.0:
    print("Frete: 20.00")
elif peso > 5.0 and peso <=10.0:
    print("Frete: 40.00")
else:
    print("Frete: 60.00")
