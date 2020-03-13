from flask import Flask,jsonify
from App.wali import blueprint

@blueprint.route('/wali/api/data')
def wali_data():

    return "oke"


    

