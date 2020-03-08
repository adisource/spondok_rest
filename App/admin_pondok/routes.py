from flask import jsonify,request
import json
import uuid
from App.admin_pondok import blueprint
from App import db,auth

#====================== add data wali =======================
@blueprint.route('/admin_pondok/api/tambah/wali',methods=['POST'])
def admin_add_wali():

     data = request.json
     uid = uuid.uuid4().hex
     data_wali = {
          "id_wali":uid,
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

     try:
          get_id = db.child("wali").child(data['id_wali']).get()
          for wali in get_id.each():
               key_wali = wali.key()
               username = db.child("wali").child(key_wali).child("username").get()
               username_val = username.val()
               if username_val == data["username"]:
                    return "data sudah di input"
               else:
                    db.child("wali").child(uid).set(data_wali)
                    return jsonify("berhasil")
     except:
          db.child("wali").child(uid).set(data_wali)
          return jsonify("berhasil")

#====================== view all wali =======================
@blueprint.route('/admin_pondok/api/all_wali',methods=['GET'])
def cek_data():

     all_wali = db.child("wali").get()
     all_data = all_wali.val()
     return jsonify(all_data)

#====================== view singel wali =======================
@blueprint.route('/admin_pondok/api/singel_wali/<key>',methods=["GET"])
def singel_wali(key):

     wali = db.child("wali").child(key).get()
     data = wali.val()
     return jsonify(data)

#====================== update data wali =======================
@blueprint.route('/admin_pondok/api/update/wali/<key>',methods=["PUT"])
def update_wali(key):
     data = request.json
     data_wali = {
          "id_wali":key,
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
     db.child("wali").child(key).update(data_wali)
     return "berhasil di update"

#====================== Hapus data wali ================================
@blueprint.route('/admin_pondok/api/hapus/wali/<key>',methods=["DELETE"])
def delete_wali(key):
     db.child("wali").child(key).remove()
     return jsonify("Berhasil di hapus")




     




     




    


     
     
     
