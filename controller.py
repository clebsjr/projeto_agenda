from model import *
from Contato import Contato


def imprimir(contato):
    print('{:<6}{:<10}{:<20}{:<20}'.format('Id', 'Nome', 'E-mail', 'Telefone'))
    print('-' * 65)
    print(f'{contato.id:<6}{contato.nome:<10} {contato.email:<20} {contato.telefone:<20}')


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
    imprimir(contato)


def listar_contatos():
    lista = select_all()
    print('{:<6}{:<10}{:<20}{:<20}'.format('Id', 'Nome', 'E-mail', 'Telefone'))
    print('-' * 65)
    for contato in lista:
        print(f'{contato[0]:<6}{contato[1]:<10} {contato[2]:<20} {contato[3]:<20}')
    print('-' * 65)


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
