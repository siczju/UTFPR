# Estado inicial
status = "solo"
altitude = 0

print("=== Simulador de Controle de Tráfego Aéreo ===")

while True:
    comando = input("Digite um comando: ").lower()

    match comando:
        case "decolar":
            if status == "solo":
                status = "voo"
                altitude = 1000
                print("Avião decolou.")
            else:
                print("O avião já está em voo.")

        case "subir":
            if status == "voo":
                altitude += 500
                print("Avião subiu.")
            else:
                print("Não é possível subir. O avião está em solo.")

        case "descer":
            if status == "voo":
                if altitude >= 500:
                    altitude -= 500
                    print("Avião desceu.")
                else:
                    print("Altitude mínima atingida.")
            else:
                print("Não é possível descer. O avião está em solo.")

        case "aterrissar":
            if status == "voo":
                status = "solo"
                altitude = 0
                print("Avião aterrissou.")
                break  # encerra o programa
            else:
                print("O avião já está em solo.")

        case "status":
            print(f"Status: {status} | Altitude: {altitude} metros")

        case "sair":
            print("Encerrando o simulador...")
            break

        case _:
            print("Comando não reconhecido.")