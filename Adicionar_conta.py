from Cliente import Cliente
import pandas as pd

class adicionar_conta:

    def __init__(self, nome_cliente, cpf, tipo_conta):
        # numero_conta = 0
        # agencia = 400
        # extrato_bancario = 0

        self.cliente = Cliente (nome_cliente, cpf, tipo_conta)

#Criar molde de classe cliente para manipular dados digitar pelo usuario

    def adicionar(self, caminho_excel):
        nova_linha = len (caminho_excel) # visao da nova linha do excel
        ultima_linha = caminho_excel.iloc[-1]

        dados_cliente = self.cliente.dicionario_cliente()

        dados_cliente["numero_conta"] = ultima_linha ["numero_conta"] +1
        dados_cliente["agencia"] = ultima_linha ["agencia"] +1

        novo_dado = pd.DataFrame(dados_cliente)
        return novo_dado