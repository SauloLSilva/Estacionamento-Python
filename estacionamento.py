from datetime import datetime
class Estacionamento:

    def __init__(self):
        self.__vagasTotais = 100
        self.__vagasOcupadas = 0
        self.__data = datetime.now().strftime('%H:%M dia:%d/%m/%Y')

    def Cadastrar(self, pessoa, placa):
            cadastroCarro = (pessoa, placa)
            with open('cadastro.txt', 'a') as arquivo:
                arquivo.write(str('Cadastro: Nome e Placa: {}-{} as {}\n'.format(cadastroCarro[0], cadastroCarro[1], self.__data)))
            print('Cadastro: {} as {}'.format(cadastroCarro, self.__data))

    def entrada(self, placa):
        if(self.__vagasOcupadas == self.__vagasTotais):
            print('Estacionamento cheio!')
        else:
            self.__vagasOcupadas += 1
            entradaCarro = (placa, self.__data)
            print('Entrada: {}'.format(entradaCarro))
            with open('controle.txt', 'a') as arquivo:
                arquivo.write(str('Entrada: {} data: {}\n'.format(entradaCarro[0], entradaCarro[1])))

    def saida( self,placa):
        if( self.__vagasOcupadas == 0 ):
            print('Estacionamento vazio!')
        else:
            self.__vagasOcupadas -= 1
            saidaCarro = (placa, self.__data)
            print('Saida: {}'.format(saidaCarro))
            with open('controle.txt', 'a') as arquivo:
                arquivo.write(str('Saída: {} data: {}\n'.format(saidaCarro[0], saidaCarro[1])))
                arquivo.close()

    def maximo(self):
        return self.__vagasTotais

    def disponiveis(self):
        return self.__vagasTotais - self.__vagasOcupadas

    def ocupadas(self):
        return self.__vagasOcupadas
    @property
    def vagas(self):
        print('Vagas ocupadas: {}'.format(self.__vagasOcupadas))
        print('Vagas totais: {}'.format(self.__vagasTotais))
        print('Data da consulta: {}\n'.format(self.__data))



