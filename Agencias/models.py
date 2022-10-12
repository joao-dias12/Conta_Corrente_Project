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
        if self.caixa < 1*10**6:
            print(f'Caixa abaixo do nivel recomendado, Caixa Atual: R${self.caixa:,.2f}')
        else:
            print(f'Caixa Aprovado - Caixa Atual: R${self.caixa:,.2f}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        emprestimo = {'Valor': valor, 'CPF': cpf, 'Juros': juros, 'Data': self._data_hora()}
        self.emprestimos.append(emprestimo.copy()) and print('Emprestimo Aceit') if self.caixa > valor else print(
            'Valor acima do encontrado em caixa'
        )
        return emprestimo

    def adicionar_cliente(self, nome, cpf, patrimonio):
        cliente = {'Nome': nome, 'cpf': cpf, 'Patrimonio': patrimonio }
        self.clientes.append(cliente)
        return cliente