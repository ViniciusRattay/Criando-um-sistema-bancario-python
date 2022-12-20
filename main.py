# Criar um sistema bancário com as opções: depositar, sacar e ver extrato
# Os depósitos devem ser números inteiros positivos, e todos depósitos devem ser armazenados em uma
# variável para ser exibido na operação de exibir extrato
# Existe o limite de 3 saques diários com limite de R$ 500 por saque, se não houver saldo suficiente
# exibir mensagem de saldo insuficiente, saques também devem ser armazenados em uma variável
# Exibe depósitos e saques realizados e o saldo atual, se o extrato estiver em branco mostrar
#"não foram realizadas movimentações"

menu = """ 
------------------ BEM VINDO AO R BANK ------------------

Selecione a operação desejada:

[D] Para depositar
[S] Para Sacar
[E] Para Extrato
[Q] Para sair

=> """
# menu construído com docstring para manter toda formatação de espaços
saldo = 0  # variáveis globais para funcionamento do programa
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3  # constante contendo limite diário de saques

while True:  # loop infinito para manter o programa em execução

    opcao = input(menu).upper()  # com o menu feito em uma variável fica mais
    # simples de invocá-lo, assim automatiza o input
    if opcao == 'D':            # do usuário e já converte para upper para evitar erros

        # condicional para cada operação
        valor = float(input('Informe o valor do depósito: R$ '))

        if valor > 0:  # condicional que valida o valor digitado pelo usuário
            saldo += valor  # sendo um valor válido adiciona ao saldo
            # adiciona uma string ao extrato gerando um
            extrato += f"Depósito R$ {valor:.2f}\n"
        else:                                       # registro da operação
            print('Operação Falhou. Valor Inválido.')

    elif opcao == 'S':

        # novas variáveis locais para
        valor = float(input('Informe o valor do Saque: R$ '))
        # validar regras de negócio
        excedeu_saldo = valor > saldo
        # garantindo que nenhuma operação
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES       # indevida ocorra

        if excedeu_saldo:
            # condicionais da operação
            print('Operação Falhou. Saldo insuficiente.')
        elif excedeu_limite:
            print('Operação Falhou. Excedeu limite de Saque.')
        elif excedeu_saques:
            print('Operação Falhou. Excedeu limite diário de Saques.')
        elif valor > 0:  # condicional que valida o valor inserido caso o mesmo seja inválido
            saldo -= valor
            extrato += f'Saque R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Operação Falhou. Valor Inválido.')

    elif opcao == 'E':
        print('\n------------------ EXIBIR EXTRATO ------------------\n')
        # if ternário para strings
        print('Não foram realizadas operações.' if not extrato else extrato)
        print(f'\nSALDO R$ {saldo:.2f}')
        print('----------------------------------------------------')

    elif opcao == 'Q':
        print('Operação Finalizada')
        break  # fim do programa
    else:
        print('Operação Falhou. Selecione opção desejada')
