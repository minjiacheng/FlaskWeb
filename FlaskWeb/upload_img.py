from FlaskWeb import app, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import render_template
from os.path import join
import os

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
		   
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    #delete any existing files on the uploads folder
    folder = app.config['UPLOAD_FOLDER']
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)	
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
            file.save(join(app.config['UPLOAD_FOLDER'], filename)) #save user input
            return render_template('index.html', filename=filename) #display result in html
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload your dog picture to predict its breed</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
