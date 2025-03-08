"""
Cálculo da área do círculo
Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""
import math

# ENTRADA - Solicita o valor do raio do círculo
raio = float(input("Digite o valor do raio: "))

#PROCESSAMENTO - Cálculo da área do círculo
area = math.pow(raio, 2.0) * math.pi
#area = raio**2 * math.pi

#SAÍDA - Exibe o resultado
print(F"A área do círculo é {area:.4}")
