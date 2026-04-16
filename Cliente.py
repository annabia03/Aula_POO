# A evolução de um dicionário é a criação de uma classe
# __init__ (Construtor) -> Cria um molde dos dados do cliente, o objetivo é conseguir transferir dados por todos os arquivos python
class Cliente:
    def __init__(self, nome_cliente, cpf, tipo_conta, numero_conta = 0, agencia = 400, extrato_bancario = 0):
        # Atributos
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self. tipo_conta = tipo_conta
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.extrato_bancario = extrato_bancario

    # __str__ (string)- > trabalha com textos
    def __str__(self):
        return f"Nome: {self.nome_cliente} | CPF: {self.cpf} | Tipo de Conta: {self.tipo_conta} | Número de Conta: {self.numero_conta} | Agência: {self.agencia} | Extrato Bancário: {self.extrato_bancario}"
    
    def dicionario_cliente(self):
        return {chave: [valor] for chave, valor in self.__dict__.items()}