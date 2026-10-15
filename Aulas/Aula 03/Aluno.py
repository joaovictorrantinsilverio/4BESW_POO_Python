class Aluno:
    # Construtor
    def __init__(self, nome, idade, identificador, instituicaoEnsino):
        self.nome = nome
        self.idade = idade
        self.instituicaoEnsino = instituicaoEnsino
        self.identificador = +1

    # Método comprimentar
    def comprimentar(self):
        print(f'Olá! Me chamo {self.nome}, tenho {self.idade} e estudo na {self.instituicaoEnsino}')

    # Método mostrarInfo
    def mostrarInfo(self):
        print('=-=-=-=-=|Informações Completas|=-=-=-=-=')
        print(f'Nome: {self.nome}'
              f'Identificador: {self.identificador}'
              f'Idade: {self.idade}'
              f'Instituição de ensino: {self.instituicaoEnsino}'
              )