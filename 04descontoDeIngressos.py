"""
--- EXERCÍCIO DE PRÁTICA: DESAFIO DA CALCULADORA DE DESCONTO DE INGRESSOS ---
1. O valor base do ingresso é R$ 100,00.
2. O programa deve pedir o nome do cliente e a idade (convertida para int).
3. O sistema deve aplicar as seguintes regras de desconto:
    - Crianças até 12 anos: Desconto de 50% (Paga R$ 50,00).
    - Idosos (60 anos ou mais): Desconto de 40% (Paga R$ 60,00).
    - Pessoas entre 13 e 59 anos: Pagam o valor integral (R$ 100,00).
4. Bônus de Verificação Par/Ímpar: Além disso, o programa deve verificar se a idade digitada é um número par ou ímpar usando o operador de resto da divisão (%).

OBJETIVO:
Praticar Operadores Matemáticos e Estruturas de condicionais.
"""

nome = input("Bem vindo (a) ao Parque Python. \nDigite o seu nome: ")
idade = int(input("Digite a sua idade: ")) # precisa ser número inteiro para usar a divisão inteira

# 1) Verificar se a idade é par ou ímpar e guardar o texto dentro de uma variável
if idade % 2 == 0:
    par_impar = "par"
else:
    par_impar = "ímpar"

# 2) Calcular o desconto e guardar dentro de uma nova variável
# a- Definir o valor base
valor_base = 100.0
# b- Calcular o desconto de acordo com a idade
if idade <= 12:
    desconto_txt = "50%"
    valor_final = valor_base * 0.50 # 50% de desconto
    # valor_final para a impressão do valor à ser pago
elif idade >= 60:
    desconto_txt = "40%"
    valor_final = valor_base * 0.60 # 40% de desconto (paga 60% do valor)
else:
    desconto_txt = "0%"
    valor_final = valor_base # paga o valor integral

# 3) Imprimir o texto com as informações solicitadas
print(f"Olá, {nome}! \nSua idade ({idade}) é um número {par_impar}. \nPor ter {idade} anos, você tem direito a {desconto_txt} de desconto! \nO valor final do seu ingresso é: R$ {valor_final:.2f}") # :.2f para colocar .00 no valor de moeda

"""Entendendo a sintaxe :.2f:
: avisa o Python que vem uma formatação para aquela variável.
.2 especifica que você quer exatamente 2 casas decimais após o ponto.
f indica o tipo float (número decimal)."""

# --- FIM DO ALGORITMO ---