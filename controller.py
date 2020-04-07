from model import *
from Contato import Contato
from prettytable import PrettyTable


def imprimir_contato(contato):
    table = PrettyTable()
    table.field_names = ['Id', 'Nome', 'E-mail', 'Telefone']
    table.add_row([contato.id, contato.nome, contato.email, contato.phone])
    print(table)


def cadastrar_contato():
    first_name = input('Digite o primeiro nome: ')
    last_name = input('Digite o primeiro nome: ')
    email = input('Digite o e-mail: ')
    phone = input('Digite o telefone (somente números): ')

    name = first_name + ' ' + last_name
    contato = Contato(name, email, phone)

    insert(contato)

    print('Dados inseridos com sucesso!!')


def atualizar_contato():
    id = input('Digite o id: ')
    c = select_one(id)

    if not c:
        print('Id não encontrado')
        return

    name = input('Digite o primeiro nome: ')
    email = input('Digite o e-mail: ')
    phone = input('Digite o telefone (somente números): ')

    contato = Contato(name, email, phone, id)

    update(contato)

    print("Contato atualizado")
    imprimir_contato(contato)


def listar_contatos():
    lista = select_all()
    table = PrettyTable()
    table.field_names = ['Id', 'Nome', 'E-mail', 'Telefone']

    for contato in lista:
        table.add_row([contato[0], contato[1], contato[2], contato[3]])

    print(table)


def deletar_contato():
    id = input('Digite o id: ')
    c = select_one(id)

    if not c:
        print('Id não encontrado')
        return

    delete(id)

    print('Contato deletado')

    listar_contatos()


def main():
    while True:
        print("""
            Menu agenda
            1 - Criar novo contato
            2 - Listar contatos
            3 - Atualizar contato
            4 - Deletar contato
            
            0 - Sair
        """)
        opcao = int(input('Digite  a opção desejada: '))

        if opcao == 1:
            cadastrar_contato()
        elif opcao == 2:
            listar_contatos()
        elif opcao == 3:
            atualizar_contato()
        elif opcao == 4:
            deletar_contato()
        elif opcao == 0:
            return False
        else:
            print('Opção inválida!')


if __name__ == '__main__':
    main()
