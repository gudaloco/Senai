"""
    DESVIO CONDICIONAL ALINHADO (ENCADEADO) - IF-ELIF_ELSE
Verifique se o número digitado é positivo, negativo ou igual a zero.

Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""

num = int(input("Digite um número: "))

if num > 0:
    print("Onúmero é positivo!")
elif num <0:
    print("O número é negativo!")
else:
    print("O número é igual a zero!")

"""
    SINTAXE IF-ELIF-SELSE
if teste_lógico1:
       instrução_se_verdadeira1
elif  teste_lógico2:
    instrução_se_verdadeira2
else:
    instrução_se_falsa
"""