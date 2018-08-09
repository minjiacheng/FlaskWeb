from FlaskWeb import app, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import render_template
from os.path import join
import os
import datetime

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():		
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            time = '{date:%Y-%m-%d_%H-%M-%S_}'.format(date=datetime.datetime.now())
            filename = time + filename
            file.save(join(app.config['UPLOAD_FOLDER'], filename)) #save user input
            return render_template('index.html', filename=filename) #display result in html
    return render_template('upload.html')
