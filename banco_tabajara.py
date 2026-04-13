from Cliente import Cliente
#    arquivo.py     o nome da nossa classe
from criar_conta import Criar_conta
import pandas as pd
import os


caminho_excel = "cliente_banco_tabajara.xlsx"

print("\n=== Banco Tabajara ===")
print("1 - Criar conta")
print("2 - Acessar conta")
print("0 - Sair\n")

opcao = input("Escolha: ")

if opcao == "1":
    print("Opção 1 selecionada!")
    nome_cliente = str(input("Nome: "))
    cpf = int(input("CPF: "))
    tipo_conta = str(input("Tipo de conta (Corrente/Poupança/Salario): "))

    if os.path.exists(caminho_excel): # true
        print("Arquivo já esxiste!")
        df = pd.read_excel(caminho_excel)
    else: # false
        print("Arquivo não existe!")

        df = pd.DataFrame()

        # Instacio para manipular os dados adicionados pelo cliente
        conta = Criar_conta(nome_cliente, cpf, tipo_conta)

        # Identifico o caminho de excel
        novo_dado = conta.salvar_excel(caminho_excel)

        df = pd.concat([df, novo_dado], ignore_index=True)
    
    df.to_excel(caminho_excel, index = False)
    
elif opcao == "2":
    print("Opção 2 selecionada!")