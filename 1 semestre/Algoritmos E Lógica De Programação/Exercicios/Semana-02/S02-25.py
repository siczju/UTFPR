nome = input("Digite o nome do aluno: ")

print("\n--- Verificação de Documentos ---")

# RG
rg_valido = input("RG válido? (s/n): ").lower()
if rg_valido != "s":
    print("Erro: RG inválido")
    print("Documentação incompleta – verificar pendências")
else:
    # CPF
    cpf_valido = input("CPF válido? (s/n): ").lower()
    if cpf_valido != "s":
        print("Erro: CPF inválido")
        print("Documentação incompleta – verificar pendências")
    else:
        # Matrícula
        matricula = input("Matrícula atualizada? (s/n): ").lower()
        if matricula != "s":
            print("Erro: Matrícula desatualizada")
            print("Documentação incompleta – verificar pendências")
        else:
            # Histórico
            historico = input("Histórico correto? (s/n): ").lower()
            if historico != "s":
                print("Erro: Histórico inválido")
                print("Documentação incompleta – verificar pendências")
            else:
                # Currículo
                curriculo = input("Currículo presente? (s/n): ").lower()
                if curriculo != "s":
                    print("Erro: Currículo ausente")
                    print("Documentação incompleta – verificar pendências")
                else:
                    print("\nCandidato aprovado para estágio")
                    print("Protocolo gerado com sucesso!")