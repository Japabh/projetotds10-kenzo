import os
import csv


def registrar_cliente():
    os.system('cls') or os.system('clear')  
    print("-------------REGISTRAR CLIENTE-------------")
    dados = {}


    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    celular = input("Digite seu Celular: ")

    dados[cpf] = [nome, celular]
    coluna = ["cpf", "nome", "celular"]
    print(dados)
    print(coluna)
   
    files_exists = os.path.isfile('clientes.csv')
    with open("clientes.csv","a",newline="", encoding="utf-8")as clientes_csv: #utf-8 padrão brasileiro para acentuação### as é um apelido
        registrar_cliente = csv.DictWriter(clientes_csv,fieldnames=coluna, delimiter=";",lineterminator='\r''\n')
        if not files_exists:
            registrar_cliente.writeheader()
        registrar_cliente.writerow({"cpf":cpf, "nome":nome, "celular":celular})
    print ("Registro realizado com sucesso!!")
    

    # Abre o arquivo para leitura e verifica se o cliente já existe pelo CPF '-'
    '''with open('clientes.csv', 'r', newline='', encoding='utf-8') as clientes_csv:
        reader = csv.DictReader(clientes_csv, delimiter=";")
        for row in reader:
            if row['cpf'] == cpf:
                print("Cliente já registrado com esse CPF.")
                return'''
    
    # Prepara os dados para escrever :P
    

    # Abre o arquivo para escrever
    
    