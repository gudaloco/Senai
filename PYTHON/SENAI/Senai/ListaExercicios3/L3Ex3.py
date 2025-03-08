"""
3. Escreva um programa que csolicite ao usúario o valor do raio de uma esfera e calcule o seu volume
Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""
import math

raio = float(input("Digite o raio da esfera: "))

volume = (4.0/3.0) * math.pi * (raio**3.0)

print(f"Volume= {volume:.6}")
