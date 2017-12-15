import pyrebase

from src.models import Pessoa, Desejos


class DbFirebase(object):
    def __init__(self):
        self.config = {
                "apiKey": "AIzaSyBZIuABAkRcq2dnRbRL39WPmUG45rT5Hvs",
                "authDomain": "hunterpromo-26348.firebaseapp.com",
                "databaseURL": "https://hunterpromo-26348.firebaseio.com",
                "projectId": "hunterpromo-26348",
                "storageBucket": "hunterpromo-26348.appspot.com",
                "messagingSenderId": "30161898656"
            }
                # "serviceAccount": "C:\\Users\\BOG\\OneDrive\\Documentos\\autoh\\Hunter.json"
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.user = self.auth.sign_in_with_email_and_password('teste@testadormaster.com', 'RootsBloodRoots')
        self.db = self.firebase.database()

    def incluir(self, collection, item):
        self.db.child(collection).push(item,  self.user['idToken'])

    def buscar_todos(self, collection=None):
        if collection:
            data = self.db.child(collection).get(self.user['idToken'])
        else:
            data = self.db.child().child().get(self.user['idToken'])
        return data

    def refresh_token(self):
        self.user = self.auth.refresh(self.user['refreshToken'])

    def incluir2(self, collection, item):
        self.db.child(collection).chield('pessoas').push(item,  self.user['idToken'])