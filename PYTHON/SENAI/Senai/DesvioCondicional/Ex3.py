"""
    DESVIO CONDICIONAL ALINHADO (ENCADEADO)
Verifique se o número digitado é positivo, negativo ou igual a zero.

Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""
from selectors import SelectSelector

num = int(input("Digite um número: "))

if num > 0:
    print("Número positivo!")
else:
    if num < 0 :
        print("Número negativo!")
    else:
        print("Número igual a zero!")

"""
    SINTAXE DO DESVIO CONDICIONAL ANINHADO
if testes_lógico1:
    instrução_se_verdadeira1
else:
    if teste_lógica2:
        instrução_se_verdadeira2
    else:
        instrução_se_falsa2

"""