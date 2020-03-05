import pyrebase

class Config(object):

    config = {
      "apiKey": "AIzaSyAE3CLRkZwbbbVMiH3vy-B3zMttkZqE19U",
      "authDomain": "spondok-9cfc9.firebaseapp.com",
      "databaseURL": "https://spondok-9cfc9.firebaseio.com",
      "storageBucket": "spondok-9cfc9.appspot.com",
    }

    firebase = pyrebase.initialize_app(config)
    


    
