import pyrebase

from src.models import Pessoa, Desejos


class DbFirebase(object):
    def __init__(self):
        self.config = {
                "apiKey": "",
                "authDomain": "",
                "databaseURL": "",
                "storageBucket": "",
                "serviceAccount": "local"
            }

        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.user = self.auth.sign_in_with_email_and_password('teste@testadormaster.com', 'RootsBloodRoots')
        self.db = self.firebase.database()


    # salvar
    def incluir(self, collection, item):
        self.db.child(collection).push(item,  self.user['idToken'])

    def buscar_todos(self, collection):
        data = self.db.child(collection).get(self.user['idToken'])
        return data
