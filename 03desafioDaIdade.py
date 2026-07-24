"""
EXECÍCIO DE PRÁTICA: DESAFIO DA IDADE
1. PERGUNTE O NOME DA PESSOA.
2. PERGUNTE O ANO DE NASCIMENTO DELA.
3. CALCULE A IDADE ATUAL (CONSIDERE O ANO VIGENTE).
4. EXIBA UMA MENSAGEM USANDO F-STRING E QUEBRA DE LINHA (\n) DIZENDO:
"Olá, [nome]!
Em 2026, você tem ou completará [X] anos de idade."
"""
nome = input("Olá! Qual o seu nome? ")
nascimento = int(input("E qual seu ano de nascimento? "))
resultado = 2026 - nascimento
print(f"Bem vinda, {nome}!\nEm 2026, você tem ou completará {resultado} anos de idade.")