import json


class Pedidos(object):
    def __init__(self, nome, email, desejos):
        self.nome = nome
        self.email = email
        self.desejos = desejos

    def json(self):
        pedido ={}
        pedido['nome'] = self.nome
        pedido['email'] = self.email
        pedido['desejos'] = self.desejos.pedidos
        return pedido


class Desejos(object):
    def __init__(self, pedido=None):
        self.pedidos = []
        if pedido is not None:
            self.pedidos.append(pedido)

    def adicionarItem(self,item):
        self.pedidos.append(item)

