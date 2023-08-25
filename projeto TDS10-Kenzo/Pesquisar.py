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
    dados_celular = csv.DictReader(celular_csv, delimiter=";")# lendo o conteudo

    for celular in dados_celular:
        if(celular["celular"].lower() == numero_celular.lower()):
            celular=(celular["celular"])
            nome=(celular["número"])
            return (True, celular, nome)
            break
    return False


def cpf(numero_cpf):
    cpf_csv = open('cpf.csv')#abrindo o arquivo CSV
    dados_cpf = csv.DictReader(cpf_csv, delimiter=";")# lendo o conteudo

    for cpf in dados_cpf:
        if(cpf ["cpf"].lower() == numero_cpf.lower()):
            cpf=(cpf["cpf"])
            nome=(cpf["número"])
            return (True, cpf, nome)
            break
    return False