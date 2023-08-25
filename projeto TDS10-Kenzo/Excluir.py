import csv,os

def excluir_cliente():
    nome_usuario = input("Entre com o código do cliente: ")

    listas = []    
    with open ('clientes.csv', 'r+', newline='', encoding='utf-8') as clientes_csv:
        dados = csv.DictReader(clientes_csv,delimiter=';')
        
        for linhas in dados:
            if linhas['cpf'] == '90':
                del linhas['cpf']
                del linhas['nome']
                del linhas['celular']
            listas.append(linhas)

    os.remove('clientes.csv')

    with open ('clientes.csv', 'a', newline='', encoding='utf-8') as clientes_csv:
        cadastrar = csv.DictWriter(clientes_csv, fieldnames=['cpf','nome','celular'], delimiter=';', lineterminator='\r\n')
        cadastrar.writeheader()
        print(listas)

        lista = []
        for i in range(len(listas)):
            a = dict(listas[i])
            lista.append(a)
        
        for i in range(len(lista)):
           cadastrar.writerow(lista[i])

        os.system('cls') or None
        lista.listar_clientes()
        print("-----------Usuário excluido com sucesso -------------")  

