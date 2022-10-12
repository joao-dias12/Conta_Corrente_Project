import random
from datetime import datetime
import pytz


class Agencia:
    """

    Essa classe representa todos os objetos "agencia do banco
    Atributos:
        telefone(str): Numero de telefone da agência
        cnpj(str): registo de cnpj da agência
        numero(str): número correspondente à agência
        cliente(lista): lista de clientes da agencia
        caixa(int): valor monetário de caixa na agência
        emprestimos(list): Lista de emprestimos feitos pela agência

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

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificacao_de_caixa(self):
        if self.caixa < 1 * 10 ** 6:
            print(f'Caixa abaixo do nivel recomendado, Caixa Atual: R${self.caixa:,.2f}')
        else:
            print(f'Caixa Aprovado - Caixa Atual: R${self.caixa:,.2f}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        emprestimo = {'Valor': valor, 'CPF': cpf, 'Juros': juros, 'Data': self._data_hora()}
        if self.caixa > valor:
            self.emprestimos.append(emprestimo.copy())
            print('Emprestimo Aceit')
        else:
            print('Valor acima do encontrado em caixa')

        return emprestimo

    def adicionar_cliente(self, nome, cpf, patrimonio):
        cliente = {'Nome': nome, 'cpf': cpf, 'Patrimonio': patrimonio}
        self.clientes.append(cliente)
        return cliente


class AgenciaVirtual(Agencia):
    """
    Eessa Classe é uma subclasse da classe Agencia,
    que terá atributos relacionados a uma classe virtual
    """
    def __init__(self, url, telefone, cnpj):
        super().__init__(telefone, cnpj, 1000)  # O super().__init__ traz todos os atributos do "init" da  classe mãe.
        # Garantindo que sejam mantidas as heranças da classe mãe.
        self.url = url
        self.caixa = 10 ** 6
        self.caixa_paypal = 0


    def depositar_paypal(self, valor):
        """
        Método apenas para classe virtual
        :return:
        """

        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        """
        Método apenas para classe virtual
        :return:
        """

        self.caixa_paypal -= valor
        self.caixa += valor

class AgenciaComum(Agencia):
    """
    Eessa Classe é uma subclasse da classe Agencia,
     que terá atributos relacionados a uma agencia comum
    """
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, random.randint(1000, 9999))
        self.caixa = 10 ** 6


class AgenciaPremiun(Agencia):
    """
        Eessa Classe é uma subclasse da classe Agencia,
         focada em clientes com caixa acima de 1 milhão
        """
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, random.randint(1000, 9999))
        self.caixa = 10 ** 7
