from lib.interface import *
from models import ContaCorrente, CartaoCredito

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

# cabecalho('Primeiro Depósito')
# conta_Joao.depositar(200)
# lista = conta_Joao._transacoes
# print(lista)
#
# cabecalho('Segundo Depósito')
# conta_Joao.depositar(1500)
# lista = conta_Joao._transacoes
# print(lista)
#
# cabecalho('Primeiro Saque')
# conta_Joao.sacar(200)
# print(lista)
#
#
# cabecalho('Primeira Transferência')
# conta_mae_joao = ContaCorrente('Marilda', '1100011', '1103211-1', '111321')
# print(f' O saldo da {conta_mae_joao.nome} é {conta_mae_joao.consultar_saldo()}')
# print('-'*20)
#
# conta_Joao.transferir(1000, conta_mae_joao)
#
# print(f'O saldo de {conta_Joao.nome} é {conta_Joao.consultar_saldo()}')
# print(f'O saldo da {conta_mae_joao.nome} é {conta_mae_joao.consultar_saldo()}')

cartao_joao = CartaoCredito('João', conta_Joao)

print(cartao_joao.conta_corrente._num_conta)
print(conta_Joao.cartoes)

cabecalho('Inserindo Campos de Data , numero do cartão e código de segurança')
print(cartao_joao.validade)
print(cartao_joao.numero)
print(cartao_joao.cod_seguranca)

cabecalho('Criando e validando senha')
cartao_joao.senha = '12'
print(cartao_joao.senha)

cabecalho('Como acessar todos os atributos de um objeto')
print(conta_Joao.__dict__)