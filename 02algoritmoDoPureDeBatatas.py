#ALGORTIMO DO PURÊ DE BATATAS (EXERCÍCIO DE PRÁTICA)
nome = (input("Olá, qual o seu nome? "))
print(f"Bem vinda, {nome}. Vamos fazer um purê de batatas?")
print("--- Algotitmo do Purê de Batatas ---")
batatasNaGeladeira = int(input("Quantas batatas tem na geladeira? "))
batatasNecessarias = 20 #valor fixo
batatasAComprar = batatasNecessarias - batatasNaGeladeira
if batatasAComprar > 0:
    print(f"Você precisa comprar {batatasAComprar} batatas. Vá ao mercado.")
else:
    print("Você já tem batatas suficientes para fazer o purê.")
print("\n----------------------------\n")
print("--- Teste de soma (sem concatenação). ---")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
resultado = num1 + num2
print(f"A soma de {num1} e {num2} é igual a: {resultado}")
print("\n----------------------------\n")