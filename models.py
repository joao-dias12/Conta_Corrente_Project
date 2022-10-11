class ContaCorrente:
    def __init__(self, nome, cpf,  agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo, valor, f'R${self.saldo:,.2f}', f'R${valor:,.2f}'

    def _limite_conta(self):   # por ter um underline, se forna um método privado
        self.limite = -1000
        return self.limite

    def sacar(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente')
        else:
            self.saldo -= valor
            print(f'{self.nome} sacou {valor} e o seu saldo ficou {self.saldo}')
        return self.saldo, valor, f'R${self.saldo:,.2f}', f'R${valor:,.2f}'

    def consutar_limite_chequeespecial(self):
        return f'Seu lime no cheque especial é {self._limite_conta()}'
