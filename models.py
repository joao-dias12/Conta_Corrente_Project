import time


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
        self._nome = nome  # Underline antes dos atributos não publicos, ou seja que só podem ser alterados por
        # métodos da classe , se eu utilizasse dois underlines, eu nao conseguiria acessar fora da classe
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

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
            print(f'{self._nome} sacou {valor} e o seu saldo ficou {self._saldo}')
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
        self._transacoes.append(transacao.copy())   # Criando o registro de transferencia enviada

        destinatario._saldo += valor
        transacao_destino = {
            'Tipo': 'Transferência',
            'Valor': -valor,
            'Data e Hora': ContaCorrente._data_hora(),
            'Origem': self
        }
        destinatario._transacoes.append(transacao_destino.copy())

        return f'{self._nome} fez a transferência no valor de {valor} para {destinatario._nome}'


class CartaoCredito:
    """
    Esse classe são os objetos cartão de crédito dos nossos clientes
    """

    def __init__(self, titular, conta_corrente):
        self.numero = None
        self.titular = titular
        self.validade = None
        self.cod_seguranca = None
        self.limite = None
        self.conta_corrente = conta_corrente
