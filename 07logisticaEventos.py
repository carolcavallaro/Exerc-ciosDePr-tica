"""
Cenário: Você está desenvolvendo o módulo de agendamento e logística para uma empresa de eventos corporativos. O sistema precisa gerenciar as datas disponíveis na agenda e calcular o orçamento de transporte das conferências.

Desafios Propostos:
1. Gestão da Lista de Datas (Conteúdo Novo de Listas):
- Crie uma lista inicial com algumas datas disponíveis para eventos (ex: ["10/10", "15/10", "20/10", "25/10"]).
- Inclusão: O cliente solicitou uma nova data de emergência. Use o método .append() para adicionar a data "12/10" ao final da lista.
- Inserção Prioritária: Use o método .insert() para colocar a data "05/10" na primeira posição da lista (índice 0).
Remoção de Data Reservada: Uma das datas foi confirmada e fechada. Use o método .pop() para remover a última data da lista (ou remove() para remover uma data específica) e exiba na tela qual data foi confirmada.
- Exiba a lista final de datas atualizadas.
2. Cálculo de Logística e Ordenação (Arredondamento + Listas):
- Cada van de transporte comporta 12 pessoas.
- Solicite ao usuário o número de participantes para 3 salas/palestras diferentes.
- Para cada sala, calcule quantas vans serão necessárias (lembre-se: se houver sobra de passageiros, uma van a mais deve ser contratada usando math.ceil() ou a lógica do resto %).
- Sabendo que cada van custa R$ 350,00, calcule o custo de transporte de cada uma das 3 salas e guarde esses 3 valores em uma lista de orçamentos.
- Ordene essa lista de custos em ordem crescente usando o método .sort() (ou a função sorted()) e exiba os valores ordenados na tela.

"""

import math

print('Olá! Bem vindo (a) ao agendamento de Vans Python!')

datasDisponiveis = ["10/10", "15/10", "20/10", "25/10"]
datasDisponiveis.append("12/10") # como solicitado no exercício
datasDisponiveis.insert(0, "05/10") # como solicitado no exercício

print(f'Datas disponíveis para agendamento: {datasDisponiveis}')
dataEscolhida = input('Que data você quer reservar para a conferência? ').strip()

if dataEscolhida in datasDisponiveis:
    datasDisponiveis.remove(dataEscolhida) # remove a data escolhida da lista de datas disponíveis
    dataConfirmada = dataEscolhida
else:
    dataConfirmada = datasDisponiveis.pop() # conforme solicitado no exercício

print(f'Data {dataConfirmada} confirmada com sucesso!\nDatas disponíveis: ', datasDisponiveis)

print('=' * 20)

sala1 = int(input('Quantos participantes irão para a Sala 1? '))
sala2 = int(input('E quantos serão os participantes da sala 2? '))
sala3 = int(input('Por fim, os participantes na sala 3: '))
qtdePessoas = sala1 + sala2 + sala3

vanSala1 = math.ceil(sala1 / 12) # conforme solicitado no exercício
vanSala2 = math.ceil(sala2 / 12)
vanSala3 = math.ceil(sala3 / 12)
qtdeVans = vanSala1 + vanSala2 + vanSala3

orcamento = [vanSala1 * 350, vanSala2 * 350, vanSala3 * 350]
orcamento.sort() # para ordenar os custos conforme solicitado no exercício
print(f'Orçamentos ordenados: {orcamento}')

valorTotal = sum(orcamento)

print('=' * 20)
print(f'RESUMO DO AGENDAMENTO PARA O DIA {dataConfirmada}:')
print(f'- Total de pessoas: {qtdePessoas}')
print(f'- Total de vans reservadas: {qtdeVans}')
print(f'- Valor total para esse evento: R$ {valorTotal:.2f}')
print('=' * 20)