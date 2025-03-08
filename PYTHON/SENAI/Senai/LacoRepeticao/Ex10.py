"""
 Escreva um programa que exiba os números pares de 0 a 50.
Data: 22/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""

contador = 1

while contador <= 50:
    contador += 1
    if contador % 2 == 0:
        print("numero:", contador)

# Agora exiba os números ímpares de 51 a 99.
while contador < 100:
    contador += 1
    if contador % 2 == 1:
        print("numero:", contador)

#Solução 2

cont = 0
print("Números pares de 0 a 50")
while cont <= 50:
    if cont % 2 == 0:
        print(cont)
    cont += 1

print("\nNúmeros pares de 51 a 99")
while cont <= 99:
    if cont % 2 == 1:
        print(cont)
    cont += 1