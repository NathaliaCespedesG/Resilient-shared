from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.SECRET_KEY.encode())

def encrypt_data(data):
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data):
    return fernet.decrypt(data.encode()).decode()
