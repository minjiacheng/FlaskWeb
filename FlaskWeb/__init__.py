"""
The flask application package.
"""
from flask import Flask
from keras.applications import xception
#from keras.applications import inception_v3
import pickle

#extract bottleneck
#inception_bottleneck = inception_v3.InceptionV3(weights='imagenet', include_top=False, pooling='avg')
xception_bottleneck = xception.Xception(weights='imagenet', include_top=False, pooling='avg')
#can't load both models onto azure at same time
#make do with just one
#load model
logreg = pickle.load(open('./FlaskWeb/models/logreg_model.sav', 'rb'))

UPLOAD_FOLDER = './FlaskWeb/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg']) #permitted file extensions for user upload

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
wsgi_app = app.wsgi_app #Registering with IIS

import FlaskWeb.upload_img
#import FlaskWeb.process_and_report
