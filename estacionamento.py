from datetime import datetime
class Estacionamento:

    def __init__(self):
        self.__vagasTotais = 100
        self.__vagasOcupadas = 0
        self.__data = datetime.now().strftime('%H:%M dia:%d/%m/%Y')

    def Cadastrar(self, pessoa, placa):
            cadastroCarro = (pessoa, placa)
            print('Cadastro: {} as {}'.format(cadastroCarro, self.__data))
            with open('cadastro.txt', 'a') as arquivo:
                for linha in cadastroCarro:
                    arquivo.write(str('Cadastro: Nome e Placa: {} as {}\n'.format(cadastroCarro, self.__data)))

    def entrada(self, placa):
        if(self.__vagasOcupadas == self.__vagasTotais):
            raise Exception('Estacionamento cheio!')
        self.__vagasOcupadas += 1
        entradaCarro = (placa, self.__data)
        print('Entrada: {}'.format(entradaCarro))
        with open('controle.txt', 'a') as arquivo:
            for linha in entradaCarro:
                arquivo.write(str('Entrada: {}\n'.format(entradaCarro)))

    def saida( self,placa):
        if( self.__vagasOcupadas == 0 ):
            raise Exception('Estacionamento vazio!')
        self.__vagasOcupadas -= 1
        saidaCarro = (placa, self.__data)
        print('Saida: {}'.format(saidaCarro))
        with open('controle.txt', 'a') as arquivo:
            for linha in saidaCarro:
                arquivo.write(str('Saída: {}\n'.format(saidaCarro)))

    def maximo(self):
        return self.__vagasTotais

    def disponiveis(self):
        return self.__vagasTotais - self.__vagasOcupadas

    def ocupadas(self):
        return self.__vagasOcupadas


