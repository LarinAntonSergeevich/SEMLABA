import os


class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/sem_lab'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = os.path.join(os.getcwd(), 'flask_session')

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'aslarin@kpfu.ru'
    MAIL_DEFAULT_SENDER = 'aslarin@kpfu.ru'
    MAIL_PASSWORD = 'zoszocjqbtsixyay'

    GITHUB_CLIENT_ID = "Ov23ct9ysKfAEYPaAq0s"
    GITHUB_CLIENT_SECRET = "8975353d17838759facb0e8448acce24cfd2bcb6"

    YANDEX_REDIRECT_URI = "http://127.0.0.1:5000/yandex/callback"
    YANDEX_CLIENT_ID = "57d98ba994b2400a886f9e1265f10d24"
    YANDEX_CLIENT_SECRET = "9323da5d5090478f9d544d9348bb84c2"
