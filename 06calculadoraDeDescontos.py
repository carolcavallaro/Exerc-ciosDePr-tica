"""
Exercício Prático: "Calculadora de Desconto da Loja"
Você vai criar um programa para aplicar cupons de desconto em uma loja online. O programa deve calcular o valor com desconto e checar se o usuário tem direito a frete grátis.

Requisitos do Exercício:
Criar uma função chamada calcularDesconto(preco, porcentagem) que retorna o novo preço.
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

def calcularDesconto (preco, porcetagem): # adicionando biblioteca para facilitar
    return preco - (preco * (porcetagem / 100)) # devolve o resultado

valorCompra = float(input('Bem vinda (o) a Loja de Descontos Python!\nInsira o valor da sua compra: R$ '))

valorTotal = valorCompra # defini as variáveis antes para corrigir o erro quando caía no else de não ter desconto
cupom = "" # deixando vazia para calcular o frete grátis no final 

while True: # para retornar ao início caso a resposta inicial (sim/não) seja inválida
    simNao = input('Você possui um cupom de descontos? (Sim/não) ').strip().lower() # .strip() para remover os espaços e .lower() para colocar tudo em letra minúscula e facilitar no código.

    if simNao == 'sim':
        cupom = input('Digite o nome do cupom: ').strip().upper() # agora, o .upper() vai deixar tudo em letras maiúsculas e sem espaço (.strip())

        if cupom == 'DEV10' and valorCompra > 100:
            valorTotal = calcularDesconto(valorCompra, 10)
            cupom = 'DEV10' # variável pra conferir o frete
            print('Cupom DEV10 aplicado com sucesso!')
            break # para sair do laço

        elif cupom == 'DEV5':
            valorTotal = calcularDesconto(valorCompra, 5)
            cupom = 'DEV5'
            print('Cupom DEV5 aplicado com sucesso!')
            break
        
        else:
            print('Cupom inválido! Nenhum cupom aplicado.')
            break

    elif simNao == 'não':
        print('Nenhum desconto aplicado.')
        break

    elif simNao in ['nao', 'não']:  # Trata tanto 'nao' quanto 'não'
        print('Nenhum desconto aplicado.')
        break  # Sai do loop e segue o código! -> sugestão de correção da IA para aplicar em testes de QA.

else:
    print('Não foi possível identificar uma resposta.')

freteGratis = valorTotal >= 150 or cupom == 'DEV10'

print('\n' + '-' * 10 + '\n') # +'-'*10 = multiplica o - 10 vezes pra deixar a estética bonitinha (IA que me ensinou rs)
print(f'Valor da compra: R$ {valorCompra:.2f}\nCupom aplicado: {cupom}\nValor da compra: R$ {valorTotal:.2f}')

if freteGratis:
    print('Você tem frete grátis! 🎉')
else:
    print(f'Frete: R$ 15,00\nValor total a pagar: R$ {valorTotal + 15 :.2f}')
print('\n' + '-' * 10)

# --- FIM DO ALGORITMO ---