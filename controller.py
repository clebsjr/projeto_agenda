from model import *
from Contato import Contato

def linha():
    print('-' * 65)

def cabecalho_tabela():
    nome = 'Nome'
    email = 'E-mail'
    tel = 'Telefone'
    linha()
    print(f'{nome:<10} {email:30} {tel:>20}')
    linha()


def cadastrar_contato():
    nome = input('Digite o nome: ')
    email = input('Digite o e-mail: ')
    telefone = input('Digite o telefone: ')

    contato = Contato(nome, email, telefone)

    insert(contato)
    linha()
    print('Dados inseridos com sucesso!!')
    linha()

def atualizar_contato():
    nome = input('Digite o nome: ')
    email = input('Digite o e-mail: ')
    telefone = input('Digite o telefone: ')

    contato = Contato(nome, email, telefone)

    update(contato)

    linha()
    print('Dados atualizados com sucesso!!')
    linha()


def listar_contatos():
    cabecalho_tabela()
    for contato in select_all():
        print(f'{contato[1]:<10} {contato[2]:30} {contato[3]:>20}')
    linha()


def deletar_contato():
    pass


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

