
import firebase_admin
from firebase_admin import credentials
from os import environ


cred_json = {
    "type": environ.get('FIREBASE_type'),
    "project_id": environ.get('FIREBASE_project_id'),
    "private_key_id": environ.get('FIREBASE_private_key_id'),
    "private_key": environ.get('FIREBASE_private_key').replace('\\n', '\n'),
    "client_email": environ.get('FIREBASE_client_email'),
    "client_id": environ.get('FIREBASE_client_id'),
    "auth_uri": environ.get('FIREBASE_auth_uri'),
    "token_uri": environ.get('FIREBASE_token_uri'),
    "auth_provider_x509_cert_url": environ.get('FIREBASE_auth_provider_x509_cert_url'),
    "client_x509_cert_url": environ.get('FIREBASE_client_x509_cert_url')
}

cred = credentials.Certificate(cred_json)

firebase_client = firebase_admin.initialize_app(cred)
