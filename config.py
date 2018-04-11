import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repo')
#
#WTF_CSRF_ENABLED = True
#
#OPENID_PROVIDERS = [ {'name': 'Yahoo', 'url': 'https://me.yahoo.com'} ]
#
#DEBUG = False
#USERNAME = 'dirty_admin'
#PASSWORD = 'da2017'
#
##SQLALCHEMY_DATABASE_URI = 'mysql://' + USERNAME + ':' + PASSWORD \
##    + '@localhost/dirty_blog'
##SQLALCHEMY_ECHO = True
