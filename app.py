from abc import ABC, abstractmethod
from datetime import datetime
import pytz
import time


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.horario = datetime.now(pytz.timezone('America/Sao_Paulo'))

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.horario = datetime.now(pytz.timezone('America/Sao_Paulo'))

    def registrar(self, conta):
        conta.sacar(self.valor)


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Conta:
    def __init__(self, cliente, numero, agencia='0001'):
        self._cliente = cliente
        self._numero = numero
        self._agencia = agencia
        self._saldo = 0
        self._historico = Historico()

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print('Saque realizado com sucesso.')
            self.historico.adicionar_transacao(Saque(valor))
        else:
            print('Erro: saldo insuficiente ou valor inválido.')

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Depósito realizado com sucesso.')
            self.historico.adicionar_transacao(Deposito(valor))
        else:
            print('Erro: valor inválido para depósito.')

    @property
    def cliente(self):
        return self._cliente

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return self._saldo

    @property
    def historico(self):
        return self._historico


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia='0001', limite=500, limite_saques=3):
        super().__init__(cliente, numero, agencia)
        self._limite = limite
        self._limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= self._limite_saques:
            print("Limite de saques diários excedido.")
            return
        if valor <= self._limite and valor <= self._saldo:
            super().sacar(valor)
            self.saques_realizados += 1
        else:
            print("Erro: valor excede limite ou saldo insuficiente.")


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    @property
    def contas(self):
        return self._contas


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

# Menu
def menu():
    menu = """
=========== MENU ===========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova conta
[5] Listar contas
[6] Novo usuário
[7] Dicas
[0] Sair
=> """
    return input(menu)

def filtrar_cliente(cpf, usuarios):
    for cliente in usuarios:
        if cliente.cpf == cpf:
            return cliente
    return None

# Main
def main():
    usuarios = []
    contas = []
    print("Bem vindo ao Banco GTP")
    while True:
        opcao = menu()

        if opcao == "1":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, usuarios)

            if not cliente:
                print("Cliente não encontrado.")
                continue
            if not cliente._contas:
                print("Este cliente ainda não possui conta. Crie sua conta antes de fazer transacões.")
                continue

            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            cliente.realizar_transacao(cliente.contas[0], transacao)

        elif opcao == "2":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, usuarios)

            if not cliente:
                print("Cliente não encontrado.")
                continue

            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            cliente.realizar_transacao(cliente.contas[0], transacao)

        elif opcao == "3":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, usuarios)

            if not cliente:
                print("Cliente não encontrado.")
                continue

            conta = cliente.contas[0]
            print("\n=========== EXTRATO ===========")
            if not conta.historico.transacoes:
                print("Nenhuma transação realizada.")
            else:
                for transacao in conta.historico.transacoes:
                    tipo = transacao.__class__.__name__
                    valor = transacao.valor
                    horario = transacao.horario.strftime("%d/%m/%Y %H:%M:%S")
                    print(f"{tipo} de R$ {valor:.2f} em {horario}")
            print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
            print("===============================")

        elif opcao == "4":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, usuarios)

            if not cliente:
                print("Cliente não encontrado. Cadastre-o primeiro.")
                continue

            numero = len(contas) + 1
            nova_conta = ContaCorrente(cliente, numero)
            cliente.adicionar_conta(nova_conta)
            contas.append(nova_conta)
            print("Conta criada com sucesso!")

        elif opcao == "5":
            for conta in contas:
                print("=" * 30)
                print(f"Agência: {conta.agencia}")
                print(f"Número: {conta.numero}")
                print(f"Titular: {conta.cliente.nome}")
                print("=" * 30)

        elif opcao == "6":
            cpf = input("Informe o CPF (somente números): ")
            cliente = filtrar_cliente(cpf, usuarios)

            if cliente:
                print("Usuário já cadastrado!")
                continue

            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

            novo_cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
            usuarios.append(novo_cliente)
            print("Usuário criado com sucesso!")
        elif opcao == "7":
            print("Antes de fazer transferências siga esse passo a passo:\nCrie um usuário em: [6] Novo usuário\nDepois crie uma conta em: [4] Nova Conta\nApós isso voce estará apto a fazer transferências!")
            time.sleep(3)

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

# Chamada do main
if __name__ == "__main__":
    main()
