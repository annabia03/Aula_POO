# Será a criação zero do nosso excel!

import pandas as pd
from Cliente import Cliente

class Criar_conta:
   def __init__(self, nome_cliente, cpf, tipo_conta):
    numero_conta = 0
    agencia = 400
    extrato_bancario = 0

    self.nome_cliente = nome_cliente
    self.cpf = cpf
    self.tipo_conta = tipo_conta
    self.numero_conta = numero_conta
    self.agencia = agencia
    self.extrato_bancario = extrato_bancario

    self.cliente = Cliente(nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario)
    def salvar_excel(self, caminho_excel):
        dados_cliente = {
            "nome_cliente": [self.nome_cliente],
            "cpf": cpf,
            "tipo_conta": [self.tipo_conta],
            "numero_contaa": [self.numero_conta],
            "agencia": [self.agencia],
            "extrato_bancario": [self.extrato_bancario],
        }

        excel = pd.DataFrame([dados_cliente])