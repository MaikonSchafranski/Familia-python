class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def resumo(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


class Pai(Pessoa):
    def __init__(self, nome, idade, trabalho):
        super().__init__(nome, idade)
        self.trabalho = trabalho
        self.filhos = []

    def adicionar_filho(self, filho):
        if isinstance(filho, Filho):
            self.filhos.append(filho)

    def resumo(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Trabalho: {self.trabalho}"


class Mae(Pessoa):
    def __init__(self, nome, idade, ocupacao):
        super().__init__(nome, idade)
        self.ocupacao = ocupacao
        self.filhos = []

    def adicionar_filho(self, filho):
        if isinstance(filho, Filho):
            self.filhos.append(filho)

    def resumo(self):
        return f"nome: {self.nome}, idade: {self.idade}, profissão: {self.ocupacao}"


class Filho(Pessoa):
    def __init__(self, nome, idade, escola):
        super().__init__(nome, idade)
        self.escola = escola

    def resumo(self):
        return f"nome: {self.nome}, idade: {self.idade}, escola: {self.escola}"


pai = Pai('Pai', 40, 'advogado')
mae = Mae('Mãe', 35, 'dentista')
filho1 = Filho('Filho 1', 10, 'Escola A')
filho2 = Filho('Filho 2', 12, 'Escola B')

pai.adicionar_filho(filho1)
mae.adicionar_filho(filho2)

print(pai.resumo())
print(mae.resumo())
print(filho1.resumo())
print(filho2.resumo())
