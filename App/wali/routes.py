from flask import Flask,jsonify
from App.wali import blueprint
from App import db




@blueprint.route('/wali/api/data')
def wali_data():

    #db = firebase.firebase.database()
    data = {
        "nama":"adi"
    }
    result = db.child("Wali").push(data)

    return result

    

