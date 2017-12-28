class Encontrados:

    listaProdutos = []

    def __init__(self, data):
        self.data = data

    def json(self):
        return {
            "data":self.data,
            "produtos": self.listaProdutos
        }