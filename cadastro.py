from datetime import datetime
class Cadastro:

    def __init__(self):
        self.__usuario = 'ADM'
        self.__data = datetime.now().strftime('%H:%M dia:%d/%m/%Y')


    def Cadastrar(self, pessoa, placa):
            cadastroCarro = (pessoa, placa)
            print('Cadastro: {} as {}'.format(cadastroCarro, self.__data))
            with open('cadastro.txt', 'a') as arquivo:
                for linha in cadastroCarro:
                    arquivo.write(str('Cadastro: Nome e Placa: {} as {}\n'.format(cadastroCarro, self.__data)))
