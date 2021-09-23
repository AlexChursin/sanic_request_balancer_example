from os import environ
from dotenv import load_dotenv

load_dotenv()


class SERVER_CONFIG:
    HOST = environ.get('HOST')
    PORT = environ.get('PORT')
    HOST_CDN = environ.get('HOST_CDN')
    DEBUG = environ.get('DEBUG', 0)

