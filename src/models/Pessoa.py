import json
import platform
import uuid
import requests
from win10toast import ToastNotifier


class Pessoa(object):
    def __init__(self, nome=None, email=None, produto=None, _id=None):
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

        if platform.system() == 'Windows':
            self.show_notification()

        try:
            url = 'http://localhost:8080/mail'
            r = requests.post(url, data=json.dumps(self.json()))
            print("Resposta do servidor: " + str(r.status_code) )
        except:
            print("não foi possível encontrar o webservice que envia email")

        # teste
        # r = requests.post('https://requestb.in/yz8zj5yz', data=json.dumps(self.json()))
        # print (r.status_code)
        # print (r.content)

    def show_notification(self):
        toaster = ToastNotifier()
        toaster.show_toast("Encontrei !!!",
                           self.produto.nome + " por " + self.produto.preco,
                           # icon_path="C:\\Users\\bruno.alves\\OneDrive\\Workspace\\Phyton\\HardMobHunter\src\ico\\buy.png",
                           duration=10)