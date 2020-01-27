class Pessoa:
    def __init__(self, *filhos, nome=None, idade=38):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"olá {self.nome} com a idade de {self.idade}"

if __name__ == '__main__':
    pessoa1 = Pessoa(nome="jose")
    pessoa2 = Pessoa(pessoa1, nome="joão")
    print (pessoa2.cumprimentar())
    for filho in pessoa2.filhos:
        print (filho.nome)
    print(id(pessoa2.cumprimentar()))
