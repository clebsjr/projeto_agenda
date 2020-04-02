from prettytable import PrettyTable
from contato import Contato
from banco_dados import insert_contato, select_contato, busca_nome, busca_email, delete_contato

contatos = []

def criar_contato():
    nome = input('Digite o nome para o contato: ')
    email = input('Digite o e-mail para o contato: ')
    telefone = input('Digite o telefone para o contato: ')

    contato = buscar_contato_email(email)

    if contato:
        print(f'O e-mail {email} já está cadastrado.')
        return

    insert_contato(Contato(nome, email, telefone))

    print('Contato salvo com sucesso!')

    listar_contatos()

def listar_contatos():
    table = PrettyTable(['Nome','E-mail','Telefone'])
    for contato in select_contato():
        table.add_row([contato.nome, contato.email, contato.telefone])
    print(table)

def buscar_contato_nome(nome):
    table = PrettyTable(['Nome','E-mail','Telefone'])
    for contato in busca_nome(nome):
        table.add_row([contato.nome, contato.email, contato.telefone])
    print(table)

def buscar_contato_email(email):
    resultado = busca_email(email)

    if not resultado:
        return
    
    return resultado

def alterar_contato(email):
    contato = buscar_contato_email(email)

    if not contato:
        print(f'Contato com email {email} não existente.')
        return
    
    nome = input('Digite o nome para o contato: ')
    telefone = input('Digite o telefone para o contato: ')

    contato.nome = nome
    contato.telefone = telefone

    print('Contato alterado com sucesso.')
    listar_contatos()

def excluir_contato(email):
    contato = buscar_contato_email(email)

    if not contato:
        print(f'Contato com email {email} não existente.')
        return
    
    delete_contato(contato)

    print('Contato removido com sucesso.')
    listar_contatos()