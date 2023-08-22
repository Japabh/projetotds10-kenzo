import csv

def pesquisar_cliente(nome_cliente):
    cliente_csv = open('clientes.csv') #abrindo o arquivo CSV
    dados_cliente = csv.DictReader(cliente_csv, delimiter=";") #lendo conteudo

    for cliente in dados_cliente: #percorrendo as linhas do arquivo
        if(cliente["nome"].lower() == nome_cliente.lower()):
            nome =  (cliente["nome"]) #listar o nome do cliente, a partir da chave ["nome"]
            cpf =  (cliente["cpf"])
            return (True,nome, cpf)
            break
    return (False,)


def celular(numero_celular):
    celular_csv = open('celular.csv')#abrindo o arquivo CSV
    dados_livro = csv.DictReader(celular_csv, delimiter=";")# lendo o conteudo

    for livros in dados_livro:
        if(livros["codigo"].lower() == numero_celular.lower()):
            codigo=(livros["codigo"])
            nome=(livros["nome"])
            return (True, codigo, nome)
            break
    return False