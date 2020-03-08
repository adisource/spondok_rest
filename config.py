import pyrebase

class Config(object):

    config = {
        "apiKey": "AIzaSyAE3CLRkZwbbbVMiH3vy-B3zMttkZqE19U",
        "authDomain": "spondok-9cfc9.firebaseapp.com",
        "databaseURL": "https://spondok-9cfc9.firebaseio.com",
        "projectId": "spondok-9cfc9",
        "storageBucket": "spondok-9cfc9.appspot.com",
        "messagingSenderId": "162122566274",
        "appId": "1:162122566274:web:247c6b24cd487e1a2d429b",
        "measurementId": "G-MJZMCGQPMB"

    
    }

    firebase = pyrebase.initialize_app(config)
    


    
