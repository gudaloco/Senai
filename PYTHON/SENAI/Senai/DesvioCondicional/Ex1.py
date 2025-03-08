"""
    DESVIO CONDICIONAL SIMPLES
Apresenta a mensagem se o número inteiro digitado for maior que 1000
Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""

# ENTRADA
num = int(input("Digite um número inteiro: "))

# Se o número for maior que 1000 faça
if num > 1000:
    print("O número digitado é maior que 1000") #Mensagem de verdadeiro
    print("Fim.")

# Apresenta a mensagem independente do if, porque está no mesmo nível do if
print(f"O numero: {num} É menor que 1000")
print("Fim.")

"""
SINTAXE DA FUNÇÃO SIMPLES

if teste_lógico:
    linha_instrução_se_verdadeiro
"""