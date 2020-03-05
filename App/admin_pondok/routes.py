from flask import jsonify,request
import json
import uuid
from App.admin_pondok import blueprint
from App import db


@blueprint.route('/admin_pondok/api/tambah/wali',methods=['POST'])
def admin_add_wali():
     
     

     data = request.json

     id = uuid.uuid4().hex

     data_wali = {
          "id_wali":id,
          "nama_lengkap": data['nama_lengkap'],
          "jenis_kelamin":data['jenis_kelamin'],
          "alamat" : data['alamat'],
          "tgl_lahir" : data['tgl_lahir'],
          "url_photo" : data['url_photo'],
          "email": data['email'],
          "telp" : data['telp'],
          "saldo" : data['saldo'],
          "username" : data['username'],
          "password" : data['password']

     }


     result = db.child("wali").child(id).set(data_wali)

     return jsonify(result)

@blueprint.route('/admin_pondok/api/all_wali',methods=['GET'])
def cek_data():

     all_wali = db.child("wali").get()
     all_data = all_wali.val()
     return jsonify(all_data)

@blueprint.route('/admin_pondok/api/singel_wali/<key>',methods=["GET"])
def singel_wali(key):

     wali = db.child("wali").child(key).get()
     data = wali.val()
     return jsonify(data)


     




    


     
     
     
