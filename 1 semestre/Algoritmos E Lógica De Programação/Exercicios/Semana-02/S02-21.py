status = "em solo"
altitude = 0

while True:
    comando = input("\nDigite um comando (decolar, subir, descer, aterrissar, status, sair): ")

    match comando:
        case "decolar":
            if status == "em voo":
                print("O avião já está em voo.")
            else:
                status = "em voo"
                altitude = 1000
                print("Avião decolou. Altitude inicial: 1000 metros.")

        case "subir":
            if status == "em voo":
                altitude = altitude + 500
                print(f"Avião subiu. Nova altitude: {altitude} metros.")
            else:
                print("O avião está em solo. Não pode subir.")

        case "descer":
            if status == "em voo":
                if altitude - 500 < 0:
                    altitude = 0
                else:
                    altitude = altitude - 500
                print(f"Avião desceu. Nova altitude: {altitude} metros.")
            else:
                print("O avião está em solo. Não pode descer.")

        case "aterrissar":
            if status == "em solo":
                print("O avião já está em solo.")
            else:
                status = "em solo"
                altitude = 0
                print("Avião aterrissou. Altitude zerada.")

        case "status":
            print(f"Status: {status} | Altitude: {altitude} metros")

        case "sair":
            print("Encerrando o simulador...")
            break

        case _:
            print("Comando não reconhecido.")