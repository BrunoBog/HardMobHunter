import json
import uuid

import requests


class Pessoa(object):
    def __init__(self, nome, email, produto, _id=None):
        self.nome = nome
        self.email = email
        self.produto = produto
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            "id": self._id,
            "nome": self.nome,
            "email": self.email,
            "produto": self.produto.json()
        }

    # Chama o webservice que envia o email
    def send_hunt_mail(self):
        url = 'http://localhost:8080/mail'
        r = requests.post(url, data=json.dumps(self.json()))
        print(r.status_code)

        # teste
        # r = requests.post('https://requestb.in/yz8zj5yz', data=json.dumps(self.json()))
        # print (r.status_code)
        # print (r.content)