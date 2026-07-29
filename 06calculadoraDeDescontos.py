"""
Exercício Prático: "Calculadora de Desconto da Loja"
Você vai criar um programa para aplicar cupons de desconto em uma loja online. O programa deve calcular o valor com desconto e checar se o usuário tem direito a frete grátis.

Requisitos do Exercício:
Criar uma função chamada calcular_desconto(preco, porcentagem) que retorna o novo preço.
1. Solicitar dados ao usuário: o valor da compra (número decimal).
2. Perguntar se o usuário possui cupom de desconto. É aqui que entra a resposta "sim" ou "nao" usando .lower()!
3. Lógica do Cupom (if/elif/else):
    - Se responder "sim", pergunte o nome do cupom.
    - Se o cupom for "DEV10" and o valor da compra for maior que 100, aplique 10% de desconto.
    - Se o cupom for "DEV5", aplique 5% de desconto.
    - Se for qualquer outro cupom, avise que o cupom é inválido e não aplique desconto.
    - Se responder "nao", informe que nenhum desconto será aplicado.
    - Else: Trate o caso em que o usuário digita algo diferente de "sim" ou "nao".
4. Frete Grátis (Operadores Booleanos): O frete é grátis se o valor final da compra for maior ou igual a R$ 150,00 or se o cupom utilizado for "DEV10".
5. Exibir o resumo final formatado.
"""

# --- CALCULADORA DE DESCONTOS ---

