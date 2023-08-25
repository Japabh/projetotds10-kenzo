import Registrar
import listar
import Excluir
import Pesquisar
import csv
import emitir_ata

resposta = "s"

while resposta == "s":
    menu = '''===================================================
            \r====[1] Registrar cliente                     =====
            \r====[2] Listar clientes                       =====
            \r====[3] Excluir cliente                       =====
            \r====[4] Pesquisar Cliente                     =====           
            \r====[5] Iniciar Ata                           =====
            \r====[6] Sair                                  =====
            \r==================================================='''                                  

    print(menu)

    opcao = int(input("Escolha uma opçao: "))

    if opcao == 1:
        Registrar.registrar_cliente()
    elif opcao == 2:
        listar.listar_cliente()
    elif opcao == 3:
        Excluir.excluir_cliente()
    elif opcao == 4: 
        Pesquisar.pesquisar_cliente()
    elif opcao == 5: 
        emitir_ata.iniciar_ata()
    elif opcao == 6:
        exit
        break
    else:
        print("Digite uma opçao valida!")

    resposta = input("Deseja continuar? [s/n]")


registrar_cliente = 'exemplo.csv'

with open(registrar_cliente, 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        print(linha)
