import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def getDocument():

    cred = credentials.Certificate('clave.json')

    app = firebase_admin.initialize_app(cred)

    db = firestore.client()

    users_ref = db.collection(u'mina-1')

    docs = users_ref.stream()

    return docs