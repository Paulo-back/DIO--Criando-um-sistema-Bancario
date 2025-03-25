#DESAFIO -DIO
#Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja 
#Modernizar suas operações e para isso escolheu a linguagem Python.
#Para implementar apenas 3 operações:
#Depósito
#Saque
#Extrato

import time as time
import re

import re



NOME = 'Breno Da Costa'
CPF_PONTUADO = '502.902.833-27'
CPF = '50290283327'
movimentacoes_entrada = []
movimentacoes_saida = []
cliente_saldo = 0
cliente_limite = 500
cliente_numero_saques = 0
CLIENTE_LIMITE_SAQUES = 3
contador_entradas = 0
contador_saidas = 0

def apresentacao():
    cpf_incompleto = CPF[10:11] + '-' + CPF[12:14]
    estrutura = (f'Ola SR.{NOME}, agradeçemos por estar iniciando sua sessão!\nPor favor insira seu CPF de final: xxx.xxx.xx{cpf_incompleto}')
    return print(estrutura)

def menu():
    separador = '-----------------------------'
    operacoes = f'DEPÓSITO ---> 1\n{separador}\n\nSAQUE ---> 2\n\n{separador}\nEXTRATO --->3\n\n{separador}\nSAIR --> 4\n\n{separador}\n\nDigite aqui: '
    
    
    return operacoes


apresentacao()
validacao = input('Digite aqui: ')

if(validacao == CPF or validacao ==CPF_PONTUADO):
    print("\n\nSessão Iniciada!\n\n")
    while True:
        opcao = int(input(menu()))
        if opcao == 1:
            valor_deposito = float(input('\nDigite o valor do depósito: '))
            if valor_deposito <=0:
                print('\nErro ao receber depósito\nImpossivel receber valores negativos!!!\n')
                print('Operações disponiveis\n')
            else:
                cliente_saldo+=valor_deposito
                movimentacoes_entrada.append(valor_deposito)
                print('Depositando...')
                time.sleep(2)
                print('Depósito concluído com sucesso!')
                contador_entradas +=1
                #####
                x = int(input('\nDeseja mais alguma coisa?\n(1) Sim   (2)Não\nDigite aqui:'))
                if x == 2:
                    break
                elif x== 1:
                    continue

                else:
                    print('Nao entendi sua resposta,confirme com (1) Sim e (2)Não')
                    x = int(input())
                    if x == 2:
                        break
            
        elif opcao == 2:
            print('Saque')
            valor_saque = float(input('Digite o valor do saque: '))
            if cliente_numero_saques < CLIENTE_LIMITE_SAQUES:

                if valor_saque<=cliente_saldo and valor_saque<=cliente_limite:
                    print('Transação em andamento...')
                    time.sleep(2)
                    print('Saque feito com Sucesso!')
                    cliente_saldo-=valor_saque
                    cliente_numero_saques +=1
                    movimentacoes_saida.append(valor_saque)
                    contador_saidas +=1
                else:
                    print('Erro ao tentar sacar por favor veja seu limite e quantidade de saques')

                x = int(input('\nDeseja mais alguma coisa?\n(1) Sim   (2)Não\nDigite aqui:'))
                if x == 2:
                    break
                elif x== 1:
                    continue

                else:
                    print('Nao entendi sua resposta,confirme com (1) Sim e (2)Não')
                    x = int(input())
                    if x == 2:
            
                        break
            else:
                print('\nVoce ja alcançou seu limite de saldo diário!\n')   



        elif opcao == 3:
            print('\nExtrato')
            print(f'NOME: {NOME}\nCPF: {CPF}')
            print(f'SALDO: R$ {cliente_saldo} \nLIMITE DE SAQUES(D): {CLIENTE_LIMITE_SAQUES}\nNUMERO DE SAQUES(D): {cliente_numero_saques}\n')
            print('MOVIMENTAÇÕES\n')
            print(f'DEPÓSITOS:')
            for i in range(contador_entradas):
                print(f'R$ {movimentacoes_entrada[i]}')
            print('\nSAQUES:')
            for i in range(contador_saidas):
                print(f'R$ {movimentacoes_saida[i]}')
                
            
            x = int(input('\nDeseja mais alguma coisa?\n(1) Sim   (2)Não\nDigite aqui:'))
            if x == 2:
                break
            elif x== 1:
                continue

            else:
                print('Nao entendi sua resposta,confirme com (1) Sim e (2)Não')
                x = int(input())
                if x == 2:
                    break
        elif opcao == 4:
            print('Saindo .....')

            break
        else:
            print('Operação invalida!!!\nPor favor selecione novamente a operação desejada do menu')
else:
    print('Dados incorretos!')
    print('\nDESCONECTANDO...')
    time.sleep(2)
    




