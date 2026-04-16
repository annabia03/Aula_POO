import pandas as pd
from Cliente import Cliente

class Criar_conta:
   def __init__(self, nome_cliente, cpf, tipo_conta):
    # numero_conta = 0
    # agencia = 400
    # extrato_bancario = 0

    # self.nome_cliente = nome_cliente
    # self.cpf = cpf
    # self.tipo_conta = tipo_conta
    # self.numero_conta = numero_conta
    # self.agencia = agencia
    # self.extrato_bancario = extrato_bancario

    self.cliente = Cliente(nome_cliente, cpf, tipo_conta)

   def salvar_excel(self, caminho_excel):
        dados_cliente = {
            "nome_cliente": [self.cliente.nome_cliente],
            "cpf": [self.cliente.cpf],
            "tipo_conta": [self.cliente.tipo_conta],
            "numero_conta": [self.cliente.numero_conta],
            "agencia": [self.cliente.agencia],
            "extrato_bancario": [self.cliente.extrato_bancario],
        }

        excel = pd.DataFrame(dados_cliente)
        return excel