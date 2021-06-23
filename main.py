from estacionamento import Estacionamento
print('Bem vindo usuário')
print('Digite opção para iniciar: ''\n')
print('[1]Cadastro de carros\n[2]Entrada\n[3]Saida\n[4]Estado estacionamento\n')
inicio = int(input('Digite valor para iniciar: '))

e = Estacionamento()
while (True):
    if 1 == inicio:
        nome = input('Digite nome usuário: ')
        placa = input('Digite placa: ')
        e.Cadastrar(nome, placa)
    elif 2 == inicio:
        placa = input('Digite placa: ')
        e.entrada(placa)
    elif 3 == inicio:
        placa = input('Digite placa: ')
        e.saida(placa)
    elif 4 == inicio:
        print('Informações:\n')
        e.vagas
    else:
        print('Opção indisponível')

    print('[1]Cadastro de carros\n[2]Entrada\n[3]Saida\n[4]Estado estacionamento\n')
    inicio = int(input('Digite valor para iniciar: '))


