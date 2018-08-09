"""
The flask application package.
"""
from flask import Flask
from keras.applications import xception
import pickle

#extract bottleneck
xception_bottleneck = xception.Xception(weights='imagenet', include_top=False, pooling='avg')
#load model
logreg = pickle.load(open('./FlaskWeb/models/logreg_model.sav', 'rb'))

UPLOAD_FOLDER = './FlaskWeb/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg']) #permitted file extensions for user upload

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
wsgi_app = app.wsgi_app #Registering with IIS

import FlaskWeb.upload_img
import FlaskWeb.process_and_report
