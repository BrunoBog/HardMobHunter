import uuid
from time import strftime, gmtime


class Produto(object):
    def __init__(self, nome, preco, link, _id=None):
        self.nome =nome
        self.preco = preco
        self.link = link
        self._id = None # uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
         "id": self._id,
         "nome": self.nome,
         "preco": self.preco,
         "link": self.link
        }

    # "preco": self.preco.replace(",","."),
    def is_procurado(self, procura):
        if procura.upper() in self.nome.upper():
            msg = "Encontrei o topico " + self.nome + "\n Com o valor : " + \
                  self.preco + " O link para o Produto e: " + self.link \
                 + " em:" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
            print(msg)
            return True
        return False
