"""
Created on Thu June 10 00:00:00 2022

@author: Yuichiro Iwashita
"""

# Modules
# Firebase Admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# JSON
import json


def parse_json_files(filename):
    path = 'json/' + filename
    json_open = open(path, 'r')
    json_load = json.load(json_open)
    print('Parsed: ' + path)
    # json_load.pop('level')
    return json_load


def upload_to_firestore():
    if not len(firebase_admin._apps):
        cred = credentials.Certificate("ServiceAccountKey.json")
        firebase_admin.initialize_app(cred)
    db = firestore.client()

    for i in range(2, 11):
        doc_ref = db.collection(u'articles').document('level' + str(i))  # Write Firestore path
        filename = 'textdata' + str(i) + '.json'
        data = parse_json_files(filename)
        doc_ref.set(data, merge=True)


if __name__ == '__main__':
    upload_to_firestore()
