class Pessoa:
    def __init__(self, nome=None, idade=38):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"olá {self.nome} com a idade de {self.idade}"

if __name__ == '__main__':
    p = Pessoa(nome="jose")
    print (p.cumprimentar())
    print(id(p.cumprimentar()))
