import Registro
import listar
import Excluir
import Buscar

resposta = "s"

while resposta == "s":
    menu = '''===================================================
            \r====[1] Registrar cliente                     =====
            \r====[2] Listar clientes                       =====
            \r====[3] Excluir cliente                       =====
            \r====[4] Buscar celular                        =====           
            \r====[5] Sair                                  =====
            \r==================================================='''                                  

    print(menu)

    opcao = int(input("Escolha uma opçao: "))

    if opcao == 1:
        Registro.Registrar_cliente()
    elif opcao == 2:
        listar.listar_cliente()
    elif opcao == 3:
        Excluir.Excluir_cliente()
    elif opcao == 4: 
        Buscar.Buscar_celular()
    elif opcao == 5:
        exit
        break
    else:
        print("Digite uma opçao valida!")

    resposta = input("Deseja continuar? [s/n]")
    