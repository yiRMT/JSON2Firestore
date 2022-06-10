# -*- coding: utf-8 -*-
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
import codecs


def parse_json_files(filename):
    path = 'json/' + filename
    json_open = codecs.open(path, 'r', 'utf-8-sig')
    json_load = json.load(json_open)
    print(json_load)
    print('Parsed: ' + path)
    return json_load


def upload_namelist_to_firestore():
    if not len(firebase_admin._apps):
        cred = credentials.Certificate("ServiceAccountKey.json")
        firebase_admin.initialize_app(cred)
    db = firestore.client()

    doc_ref = db.collection(u'worddata').document('namelist')  # Write Firestore path
    filename = 'namelist.json'
    data = parse_json_files(filename)
    doc_ref.set({'namelist': data}, merge=True)


def upload_lemma_to_firestore():
    if not len(firebase_admin._apps):
        cred = credentials.Certificate("ServiceAccountKey.json")
        firebase_admin.initialize_app(cred)
    db = firestore.client()

    doc_ref = db.collection('worddata').document('lemma')  # Write Firestore path
    filename = 'lemma.json'
    data = parse_json_files(filename)
    doc_ref.set({'lemma': data}, merge=True)


if __name__ == '__main__':
    upload_namelist_to_firestore()
    upload_lemma_to_firestore()
