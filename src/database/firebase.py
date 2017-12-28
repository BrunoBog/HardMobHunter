import pyrebase

from src.models import Pessoa, Desejos
class DbFirebase(object):
    config = {
        "apiKey": "AIzaSyBZIuABAkRcq2dnRbRL39WPmUG45rT5Hvs",
        "authDomain": "hunterpromo-26348.firebaseapp.com",
        "databaseURL": "https://hunterpromo-26348.firebaseio.com",
        "projectId": "hunterpromo-26348",
        "storageBucket": "hunterpromo-26348.appspot.com",
        "messagingSenderId": "30161898656"
    }
    # "serviceAccount": "C:\\Users\\BOG\\OneDrive\\Documentos\\autoh\\Hunter.json"

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password('teste@testadormaster.com', 'RootsBloodRoots')
    db = firebase.database()

    @staticmethod
    def incluir(collection, item, child=None):
        if child:
            DbFirebase.db.child(collection).child(child).push(item, DbFirebase.user['idToken'])
        else:
            DbFirebase.db.child(collection).push(item,  DbFirebase.user['idToken'])

    @staticmethod
    def buscar_todos( collection=None):
        if collection:
            return DbFirebase.db.child(collection).get(DbFirebase.user['idToken'])
        else:
            return DbFirebase.db.child().child().get(DbFirebase.user['idToken'])

    @staticmethod
    def refresh_token():
        DbFirebase.user = DbFirebase.auth.refresh(DbFirebase.user['refreshToken'])

    @staticmethod
    def incluir2( collection, item):
        DbFirebase.db.child(collection).chield('pessoas').push(item,  DbFirebase.user['idToken'])

