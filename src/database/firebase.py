import pyrebase

from src.models import Pessoa, Desejos


class DbFirebase(object):
    def __init__(self):
        self.config = {
                "apiKey": "AIzaSyB7_2SlMHnnXx96vDcVjY9CFMdsLUEnv3I",
                "authDomain": "financaspessoais-45f54.firebaseapp.com",
                "databaseURL": "https://financaspessoais-45f54.firebaseio.com",
                "storageBucket": "financaspessoais-45f54.appspot.com",
                "serviceAccount": "C:\\Users\\BOG\\OneDrive\\Documentos\\autoh\\Financas-b85e1f6526a1.json"
            }

        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.user = self.auth.sign_in_with_email_and_password('teste@testadormaster.com', 'RootsBloodRoots')
        self.db = self.firebase.database()

    def incluir(self, collection, item):
        self.db.child(collection).push(item,  self.user['idToken'])

    def buscar_todos(self, collection):
        data = self.db.child(collection).get(self.user['idToken'])
        return data

    def refresh_token(self):
        self.user = self.auth.refresh(self.user['refreshToken'])

    def incluir2(self, collection, item):
        self.db.child(collection).chield('pessoas').push(item,  self.user['idToken'])