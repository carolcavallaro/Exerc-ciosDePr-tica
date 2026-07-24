"""
--- EXERCÍCIO DE PRÁTICA: DESAFIO PROCESSADOR DE E-MAILS E USUÁRIOS ---

Crie um script Python chamado processador_email.py que faça o seguinte:
1. Receba do usuário uma string contendo um e-mail completo (exemplo: usuario@gmail.com).
2. Extraia o nome do usuário (tudo o que vem antes do @).
3. Extraia o domínio (tudo o que vem depois do @).
4. Verifique e exiba se o e-mail termina com .com ou .br utilizando índice negativo ([-4:] ou [-3:]).
5. Imprima o nome do usuário invertido e em letras maiúsculas.
"""

email = input("Digite o seu e-mail completo: ")
nomeUsuario = email.split('@')[0] # .split('@') para dividir a frase a partir do @ | e [0] para dar nome ao usuário do começo ao fim dessa divisão. Como o usuário vem antes do @, não precisa mais nada antes.
dominioEmail = email.split('@')[1] # [-1] também funciona
fimEmail = dominioEmail.split('.')[-1]
invertido = nomeUsuario.upper()[::-1] # .upper() para letras maiúsculas
print(f"Seu usuário é: {nomeUsuario} \nSeu domínio é: @{dominioEmail} \nSeu e-mail termina com: .{fimEmail} \nSeu nome de usuário invertido fica: {invertido}")

# --- FIM DO ALGORITMO ---