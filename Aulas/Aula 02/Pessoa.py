class Pessoa:
    # Construtor
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    # Método para comprimentar
    def comprimentar(self):
        print(f'Olá! Meu nome é {self.nome} e tenho {self.idade} anos.')

    # Método que mostra as informações
    def mostrarInfo(self):
        print('=-=-=-=-=-=|Informações Completas|=-=-=-=-=-=')
        print(f'Nome.: {self.nome} \n'
              f'Idade: {self.idade} \n'
              f'CPF..: {self.cpf}'
              )