from model import *
from Contato import Contato


def cabecalho():
    nome = 'Nome'
    email = 'E-mail'
    tel = 'Telefone'
    print('-' * 65)
    print(f'{nome:10} {email:20} {tel:>30}')
    print('-' * 65)


def cadastrar_contato():
    nome = input('Digite o nome: ')
    email = input('Digite o e-mail: ')
    telefone = input('Digite o telefone: ')

    contato = Contato(nome, email, telefone)

    insert(contato)

    print('Dados inseridos com sucesso!!')


def atualizar_contato():
    nome = input('Digite o nome: ')
    email = input('Digite o e-mail: ')
    telefone = input('Digite o telefone: ')

    contato = Contato(nome, email, telefone)

    update(contato)

    print('Dados atualizados com sucesso!!')


def listar_contatos():
    cabecalho()
    for contato in select_all():
        print(f'{contato[1]:<10} {contato[2]:20} {contato[3]:>30}')
    print('-' * 65)


if __name__ == '__main__':
    listar_contatos()


