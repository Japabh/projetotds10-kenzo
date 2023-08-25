import os
import csv

def listar_cliente():
    os.system('cls') or os.system('clear')  
    print("-------------LISTAR CLIENTES-------------")

    with open('clientes.csv', 'r', newline='', encoding='utf-8') as clientes_csv:
        reader = csv.DictReader(clientes_csv, delimiter=";")
        for cliente in reader:
            print("nome:", cliente['nome'])
            print("cpf:", cliente['cpf'])
            print("celular:", cliente['celular'])
            print('\n\r')

