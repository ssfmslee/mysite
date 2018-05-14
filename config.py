class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://ssfmslee:'
        'databasepw'
        '@ssfmslee.mysql.pythonanywhere-services.com/'
        'ssfmslee$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'somethingthatcannotbeguessed'