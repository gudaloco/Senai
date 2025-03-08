"""
Calcular o perímetro do círculo
Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""

#Importando a biblioteca matemática
import math

# ENTRADA - Solicita ao usuário do diâmetro do círculo
diametro = float(input("Digite o valor do diâmetro: "))

# PROCESSAMENTO - Cálculo do perímetro = PI * diâmetro
perimetro = math.pi * diametro
#perimetro = 3.14 * diametro

# SAÍDA - Exibe o resultado do perímetro
print(f"O perímetro cco círculo é {perimetro:.4}")
