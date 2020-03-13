import firebase_admin
from firebase_admin import credentials
class Config(object):

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('./serviceAccountKey.json')

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
    'databaseURL': "https://spondok-9cfc9.firebaseio.com"
    })

    


    
