from flask import jsonify,request
import json
import uuid
from App.admin_pondok import blueprint
from firebase_admin import db,auth

#====================== add data wali =======================
@blueprint.route('/admin_pondok/api/tambah/wali',methods=['POST'])
def admin_add_wali():

     data = request.json
     
     uid = uuid.uuid4().hex

     ref = db.reference("wali")
     data_wali = {
          "id_wali":uid,
          "nama_lengkap": data['nama_lengkap'],
          "jenis_kelamin":data['jenis_kelamin'],
          "alamat" : data['alamat'],
          "tgl_lahir" : data['tgl_lahir'],
          "url_photo" : data['url_photo'],
          "phone_number":data['phone_number'],
          "email": data['email'],
          "saldo" : data['saldo'],
          "username" : data['username'],
          "password" : data['password']

          }
     ref.child(uid).set(data_wali)
     return "berhasil"
     
#====================== view all wali =======================
@blueprint.route('/admin_pondok/api/all_wali',methods=['GET'])
def cek_data():
     ref = db.reference("wali").get()
     return jsonify(ref)

#====================== view singel wali =======================
@blueprint.route('/admin_pondok/api/singel_wali/<key>',methods=["GET"])
def singel_wali(key):


     ref = db.reference("wali")
     snap = ref.child(key).get()
     return snap

#====================== update data wali =======================
@blueprint.route('/admin_pondok/api/update/wali/<key>',methods=["PUT"])
def update_wali(key):
     data = request.json
     ref = db.reference("wali")
     
     data_wali = {
          "id_wali":key,
          "nama_lengkap": data['nama_lengkap'],
          "jenis_kelamin":data['jenis_kelamin'],
          "alamat" : data['alamat'],
          "tgl_lahir" : data['tgl_lahir'],
          "url_photo" : data['url_photo'],
          "phone_number":data['phone_number'],
          "email": data['email'],
          "saldo" : data['saldo'],
          "username" : data['username'],
          "password" : data['password']

          }
     wali_update = ref.child(key).update(data_wali)
     return "berhasil di update"
     

@blueprint.route('/admin_pondok/api/add/santri/<key_wali>',methods=['POST'])
def add_santri(key_wali):

     data = request.json

     uid_santri = uuid.uuid4().hex
     data_santri = {
            "id_santri":uid_santri,
            "id_wali":key_wali,
            "no_induk":data["no_induk"],
            'nama_lengkap' : data['nama_lengkap'],
            "jenis_kelamin" : data['jenis_kelamin'],
            "alamat" : data['alamat'],
            "tgl_lahir" : data['tgl_lahir'],
            "url_photo" : data['url_photo'],
            "email" : data['email'],
            "telp" : data['telp'],
            "password" : data['password'],
            "rayon" : data['rayon'],
            "kelas" : data['kelas'],
            "kamar" : data['kamar']
     }

    
     db.child("santri").child(uid_santri).set(data_santri)
     return "Behasil di add"    

@blueprint.route('/admin_pondok/api/view/all_santri',methods=['GET'])
def all_santri():

     
     
            
          

     






     




     




    


     
     
     
