from datetime import datetime
import pytz
import time
from random import randint


class ContaCorrente:
    """
    Cria um objeto conta corrente pra gerenciar as contas dos clientes

    Atributos
        nome(str): Nome do Cliente
        cpf(str): CPF do Cliente
        Agencia(str): Agencia do Cliente
        saldo(int): Valor do saldo na conta
        transações(list): Lista de transações realizadas  ...
    """

    @staticmethod
    def _data_hora():
        """
        Função interna para calcular a hora
        :return: hora daquele momento
        """
        hora = time.strftime("%d/%m/%Y %H:%M:%S")
        return hora

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome  # Underline antes dos atributos não publicos, ou seja que só podem ser alterados por
        # métodos da classe , se eu utilizasse dois underlines, eu nao conseguiria acessar fora da classe
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        """
        Esse método retorna o saldo
        :return:
        """
        return f'R${self._saldo:,.2f}'

    def depositar(self, valor):
        """
        Esse método deposita um valor em uma conta
        :param valor:  valor a ser depositado
        :return: retorna o saldo e o valor depositado de forma bruta e formatada
        """
        transacao = {'Tipo': 'Depósito', 'Valor': valor, 'Data e Hora': ContaCorrente._data_hora()}
        self._transacoes.append(transacao.copy())
        self._saldo += valor
        print(f'Como você depositou R${valor:,.2f} , o seu saldo é R${self._saldo:,.2f}')
        return self._saldo, valor, f'R${self._saldo:,.2f}', f'R${valor:,.2f}'

    def _limite_conta(self):  # por ter um underline, se forna um método privado
        """
        Defini o limite inferior do valor de uma conta
        :return: limite
        """
        self._limite = -1000
        return self._limite

    def sacar(self, valor):
        """
        Realiza o saque de um valor de uma conta
        :param valor: valor a ser sacado
        :return: valor sacado e saldo após o saque
        """
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente')
        else:
            self._saldo -= valor
            print(f'{self.nome} sacou {valor} e o seu saldo ficou {self._saldo}')
            transacao = {'Tipo': 'Saque', 'Valor': -valor, 'Data e Hora': ContaCorrente._data_hora()}
            self._transacoes.append(transacao.copy())
        return self._saldo, valor, f'R${self._saldo:,.2f}', f'R${valor:,.2f}'

    def consutar_limite_chequeespecial(self):
        """
        Consulta o valor do limete de cheque especial
        :return: Frase dizendo o valor do limite de cheque especial
        """
        return f'Seu lime no cheque especial é {self._limite_conta()}'

    def transferir(self, valor, destinatario):
        """
        Realiza transferência de um objeto (conta corrente) para outro objeto(conta corrente)
        :param valor: Valor a ser transferido
        :param destinatario: Objeto que ira receber a transferência
        :return:
        """
        self._saldo -= valor
        transacao = {
            'Tipo': 'Transferência',
            'Valor': -valor,
            'Data e Hora': ContaCorrente._data_hora(),
            'Destinatario': destinatario
        }
        self._transacoes.append(transacao.copy())  # Criando o registro de transferencia enviada

        destinatario._saldo += valor
        transacao_destino = {
            'Tipo': 'Transferência',
            'Valor': -valor,
            'Data e Hora': ContaCorrente._data_hora(),
            'Origem': self
        }
        destinatario._transacoes.append(transacao_destino.copy())

        return f'{self.nome} fez a transferência no valor de {valor} para {destinatario.nome}'


class CartaoCredito:
    """
    Esse classe são os objetos cartão de crédito dos nossos clientes
    Atributos:
        Numero: Numero do cartão
        titular: Pesssoa Titular da conta
        validade: Data de Validade
        cod_segurança: Código de segurança do cartão
        limite: Limite do cartão de crédito
        Conta corrente: Conta ao qual o cartão é vinculado, relação de ManyToOne

    """

    @staticmethod
    def _data_hora():
        """
        Função interna para calcular a hora
        :return: hora daquele momento
        """
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)

        return horario_br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)  # criando numero de cartão com 16 digitos
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0, 9)} {randint(0, 9)} {randint(0, 9)}'
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append({'Cartão': self, 'Tipo': 'Crédito'})

    @property  # Quando o atributo tem que passar por algum tipo de validação, é necessario criar um metodo get e
    # método set, no caso , usando @property , temos um método "GET"
    def senha(self):
        """
        Criação de Senha com obrigatóriamente 4 digitos
        :return: senha
        """
        return self._senha

    @senha.setter  # estamos a criar a validação de "settar" a senha, ou seja, definir a senha que deve ter 4 digitos
    # e ser numero. Nesse caso , temos um método 'SET"
    def senha(self, nova_senha):
        if len(nova_senha) == nova_senha.isnumeric():
            self._senha = nova_senha
        else:
            print('Nova senha invalida')
