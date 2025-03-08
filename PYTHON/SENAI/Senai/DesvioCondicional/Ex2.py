"""
    DESVIO CONDICIONAL COMPOSTO
Se a idade for maior ou igual a 18, apresentar a mensagem
"Você é maior de idade"
Caso contrário, apresentar a mensagem "Você é menor de idade"
Data: 15/02/2025
Criado por: Gustavo Galdino Alexandre Cavalcante
Professora: Luciana
"""

idade = int(input("Digite a idade: "))

# Se a idade for maior ou igual a 18 faça
if idade >= 18:
    # Se o teste lógico for verdadeiro, apresenta a linha abaixo
    print("Você é maior de idade")
else: #Senão
    #Se o teste lógico for falso, apresenta a linha abaixo
    print("Você é menor de idade")

"""
    SINTAXE DO IF-ELSE
if teste_lógico:
    intrução_se_verdadeira
else:
    instrução_se_falsa
"""