def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")


def listar_contatos(agenda):
    print("Lista de contatos:")
    for nome, telefone in sorted(agenda.items()):
        print(f"{nome}: {telefone}")


def ordenar_lista_por_nome(agenda):
    agenda_ordenada = dict(sorted(agenda.items()))
    print("Lista de contatos ordenada por nome:")
    for nome, telefone in agenda_ordenada.items():
        print(f"{nome}: {telefone}")


def menu():
    agenda = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Ordenar lista por nome")
        print("4. Sair")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            adicionar_contato(agenda)
        elif opcao == '2':
            listar_contatos(agenda)
        elif opcao == '3':
            ordenar_lista_por_nome(agenda)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")


def main():
    menu()


if __name__ == "__main__":
    main()
