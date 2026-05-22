class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def mostrar(self):
        self.nome + 'llll'
        return self.nome , self.idade
pessoa=[Pessoa('roberto',12)]
for pes in pessoa:
    print(pes.mostrar())