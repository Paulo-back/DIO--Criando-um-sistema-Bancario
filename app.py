import time as time
from datetime import datetime,timedelta,timezone
import pytz



def menu():
    separador = '-----------------------------'
    operacoes = f'MENU:\n\n[1]DEPÓSITO\n{separador}\n\n[2]SAQUE\n\n{separador}\n[3]EXTRATO\n\n{separador}\n[4]CRIAR USUÁRIO\n\n{separador}\n[5]CRIAR CONTA CORRENTE\n\n{separador}\n[6]EXIBIR CONTAS\n\n{separador}\n[7]SAIR\n\n{separador}\nDigite aqui: '
    return operacoes

def saque(*,cliente_saldo,valor,CLIENTE_LIMITE_TRANSACOES,cliente_transacoes,cliente_limite,movimentacoes_saida):
    
    if len(cliente_transacoes) < CLIENTE_LIMITE_TRANSACOES:
            horario_saque = datetime.now(pytz.timezone('America/Sao_Paulo'))
            horario_saque = datetime.strftime(horario_saque, "%d/%m/%Y %H:%M:%S")
            saques = {}

            if valor<=cliente_saldo and valor<=cliente_limite:
                print('Transação em andamento...')
                time.sleep(2)
                print('Saque feito com Sucesso!')
                cliente_saldo-=valor
                saques['Valor']=valor
                saques['Horário']=horario_saque
                movimentacoes_saida.append(saques)
                cliente_transacoes.append(horario_saque)
            else:
                print('Erro ao tentar sacar por favor veja seu limite e quantidade de saques')
                time.sleep(2)
    else:
        print('\nOperação falhou! O número máximo de saques excedido.')


    return cliente_saldo

def deposito_cliente(valor,cliente_saldo,movimentacoes_entrada,cliente_transacoes,/):
    deposito = {}
    if valor <= 0:
        print('\nErro ao receber depósito\nImpossivel receber valores negativos!!!\n')
        print('Operações disponiveis\n')
    else:
        horario_deposito = datetime.now(pytz.timezone('America/Sao_Paulo'))
        horario_deposito = datetime.strftime(horario_deposito, "%d/%m/%Y %H:%M:%S")
        cliente_saldo+=valor
        deposito['Valor']=valor
        deposito['Horário']=horario_deposito
        movimentacoes_entrada.append(deposito)
        cliente_transacoes.append(horario_deposito)

        print('Depositando...')
        time.sleep(2)
        print('Depósito concluído com sucesso!')

        return cliente_saldo


def extrato(*,cliente_saldo,CLIENTE_LIMITE_TRANSACOES,cliente_transacoes,movimentacoes_entrada,movimentacoes_saida):
    print('\nExtrato')
    # print(f'NOME: {nome}\nCPF: {cpf}')
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

def criar_usuario(usuarios):
    cpf = input('Informe seu CPF (SOMENTE NÚMEROS)')
    novo_usuario = filtro_usuario(cpf,usuarios)
    if novo_usuario:
        print('Usuário com este CPF já existente !!!')
        return
    nome = input('Digite seu nome completo: ')
    dt_nascimento = input('Digite sua data de nascimento neste formato (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço neste formato (logradouro,nro - bairro - cidade/sigla - estado): ')
    usuarios.append({"nome": nome, "data_nascimento": dt_nascimento, "cpf": cpf, "endereco": endereco})
    print("Parabéns -_-\nUsuário Cadastrado com Sucesso!")
    print('Redirecinando ao menu...\n')
    time.sleep(2)

def filtro_usuario(cpf,usuarios):
     usuarios_filtro = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
     return usuarios_filtro[0] if usuarios_filtro else None

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Por favor informe seu CPF de usuário: ")
    usuario = filtro_usuario(cpf,usuarios)
    if usuario:
         print('\nSua conta foi criada com Sucesso !')
         print('Retornando ao menu...')
         time.sleep(2)
         
         return {
            "agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    time.sleep(2)
    print('\nUsuário não encontrado,crie um usuário ou reveja os dados') 

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def transacoes_diarias(cliente_transacoes):
     hoje = datetime.now(pytz.timezone('America/Sao_Paulo')).date()
     transacoes_hoje = sum(
        1 for i in cliente_transacoes 
        if datetime.strptime(i, "%d/%m/%Y %H:%M:%S").date() == hoje)
     return transacoes_hoje

def main():
    AGENCIA = "0001"
    movimentacoes_entrada = []
    movimentacoes_saida = []
    cliente_saldo = 0
    cliente_limite = 500
    cliente_transacoes = []
    CLIENTE_LIMITE_TRANSACOES = 10
    contas = []
    usuarios =  []


    while True:
        opcao = int(input(menu()))
        if opcao in [1,2]:
             if transacoes_diarias(cliente_transacoes)>=CLIENTE_LIMITE_TRANSACOES:
                print(f"\nVocê atingiu o limite de {CLIENTE_LIMITE_TRANSACOES} transações diárias!\n")
                continue
             
        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))
            cliente_saldo = deposito_cliente(valor,cliente_saldo,movimentacoes_entrada,cliente_transacoes)

        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            cliente_saldo = saque(valor=valor,cliente_saldo=cliente_saldo,cliente_transacoes=cliente_transacoes,cliente_limite=cliente_limite,movimentacoes_saida=movimentacoes_saida,CLIENTE_LIMITE_TRANSACOES=CLIENTE_LIMITE_TRANSACOES)

        elif opcao == 3:
             extrato(cliente_saldo=cliente_saldo,CLIENTE_LIMITE_TRANSACOES=CLIENTE_LIMITE_TRANSACOES,cliente_transacoes=cliente_transacoes,movimentacoes_entrada=movimentacoes_entrada,movimentacoes_saida=movimentacoes_saida)
             time.sleep(5)
             
        elif opcao == 4:
             criar_usuario(usuarios)

        elif opcao == 5:
             numero_conta = len(contas)+1
             conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

             if conta:
                  contas.append(conta)
        elif opcao == 6:
             listar_contas(contas)

        elif opcao == 7:
             print('Saindo .....')
             time.sleep(2)
             break
        else:
             print('Operação invalida!!!\nPor favor selecione novamente a operação desejada do menu')
        


             


main()