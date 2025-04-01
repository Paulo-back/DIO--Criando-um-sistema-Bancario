#DESAFIO -DIO
#Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja 
#Modernizar suas operações e para isso escolheu a linguagem Python.
#Para implementar apenas 3 operações:
#Depósito
#Saque
#Extrato

import time as time
from datetime import datetime,timedelta,timezone
import re
import pytz


NOME = 'Breno Da Costa'
CPF_PONTUADO = '502.902.833-27'
CPF = '50290283327'
movimentacoes_entrada = []
movimentacoes_saida = []
cliente_saldo = 0
cliente_limite = 500
cliente_transacoes = []
CLIENTE_LIMITE_TRANSACOES = 10

def apresentacao():
    cpf_incompleto = CPF_PONTUADO[10:11] + '-' + CPF_PONTUADO[12:14]
    estrutura = (f'Ola SR.{NOME}, agradeçemos por estar iniciando sua sessão!\nPor favor insira seu CPF de final: xxx.xxx.xx{cpf_incompleto}')
    return print(estrutura)

def menu():
    separador = '-----------------------------'
    operacoes = f'DEPÓSITO ---> 1\n{separador}\n\nSAQUE ---> 2\n\n{separador}\nEXTRATO ---> 3\n\n{separador}\nSAIR --> 4\n\n{separador}\n\nDigite aqui: '
    
    
    return operacoes
def transacoes_diarias():
    hoje = datetime.now(pytz.timezone('America/Sao_Paulo')).date()
    transacoes_hoje = sum(1 for i in cliente_transacoes if i.date() == hoje)
    return transacoes_hoje

apresentacao()
validacao = input('Digite aqui: ')

if(validacao == CPF or validacao ==CPF_PONTUADO): 
    print("\n\nSessão Iniciada!\n\n")
    while True:
        deposito = {}
        saques = {}
        opcao = int(input(menu()))
        

        if opcao in [1,2]:
            if transacoes_diarias()>=CLIENTE_LIMITE_TRANSACOES:
                print(f"\nVocê atingiu o limite de {CLIENTE_LIMITE_TRANSACOES} transações diárias!\n")
                continue

            horario_atual = datetime.now(pytz.timezone('America/Sao_Paulo'))

        if opcao == 1:
            valor_deposito = float(input('\nDigite o valor do depósito: '))
            horario_deposito = datetime.now(pytz.timezone('America/Sao_Paulo'))
            horario_deposito = datetime.strftime(horario_deposito, "%d/%m/%Y %H:%M:%S")

            if valor_deposito <=0:
                print('\nErro ao receber depósito\nImpossivel receber valores negativos!!!\n')
                print('Operações disponiveis\n')
            else:
                cliente_saldo+=valor_deposito
                deposito['Valor']=valor_deposito
                deposito['Horário']=horario_deposito
                movimentacoes_entrada.append(deposito)
                cliente_transacoes.append(horario_atual)
                

                print('Depositando...')
                time.sleep(2)
                print('Depósito concluído com sucesso!')
                
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
            horario_saque = datetime.now(pytz.timezone('America/Sao_Paulo'))
            horario_saque = datetime.strftime(horario_saque, "%d/%m/%Y %H:%M:%S")

            if len(cliente_transacoes) < CLIENTE_LIMITE_TRANSACOES:

                if valor_saque<=cliente_saldo and valor_saque<=cliente_limite:
                    print('Transação em andamento...')
                    time.sleep(2)
                    print('Saque feito com Sucesso!')
                    cliente_saldo-=valor_saque
                    saques['Valor']=valor_saque
                    saques['Horário']=horario_saque
                    movimentacoes_saida.append(saques)
                    cliente_transacoes.append(horario_atual)
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
            print(f'SALDO: R$ {cliente_saldo} \nLIMITE DE TRANSFERÊNCIAS(D): {CLIENTE_LIMITE_TRANSACOES}\nNUMERO DE TRANSFERÊNCIAS(D): {len(cliente_transacoes)}\n')
            print('MOVIMENTAÇÕES\n')
            print(f'DEPÓSITOS:')
            for i,deposito in enumerate(movimentacoes_entrada,1):
                for chave,valor in deposito.items():
                    if chave =='Valor':
                        print(f"{chave}: R$ {valor}") 
                    else: 
                        print(f"{chave}: {valor}\n")  
                
            print('\nSAQUES:')
            for i,saques in enumerate(movimentacoes_saida,1):
                for chave,valor in saques.items():
                    if chave =='Valor':
                        print(f"{chave}: R$ {valor}")
                    else:
                        print(f"{chave}: {valor}\n")  
            
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
    




