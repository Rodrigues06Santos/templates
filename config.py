import os 
class config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'victor_bjj'