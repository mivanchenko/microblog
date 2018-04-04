import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

#basedir = os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repo')
#SQLALCHEMY_TRACK_MODIFICATIONS = True
#
#WTF_CSRF_ENABLED = True
#SECRET_KEY = 'you-will-never-guess'
#
#OPENID_PROVIDERS = [ {'name': 'Yahoo', 'url': 'https://me.yahoo.com'} ]
#
#
#DEBUG = False
#USERNAME = 'dirty_admin'
#PASSWORD = 'da2017'
#
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
##SQLALCHEMY_DATABASE_URI = 'mysql://' + USERNAME + ':' + PASSWORD \
##    + '@localhost/dirty_blog'
##SQLALCHEMY_ECHO = True
#
