from lib.interface import *
from models import ContaCorrente

cabecalho('Abertura de Conta Corrente')

# while True:
#     resposta = menu(["Quer Abrir uma Conta", "Finalizar Navegação"])
#
#     if resposta == 1:
#         nome = str(input('Qual o seu nome'))
#         cpf = str(input('Qual o seu CPF'))
#         saldo = int(input('Qual o seu Saldo?[OPCIONAL]'))
#         f'conta_{nome}' = ContaCorrente(nome=nome,cpf=cpf, saldo=saldo)
# FUTURA BARRA DE NAVEGAÇÃO

conta_Joao = ContaCorrente('João', '111111', '3411-1', '77777')

deposito = conta_Joao.depositar(200)

print(f'Como você depositou R${deposito[0]:,.2f} , o seu saldo é R${deposito[1]:,.2f}')
print(conta_Joao.consutar_limite_chequeespecial())
