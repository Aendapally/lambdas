from flask import Flask, flash, request, redirect, render_template
import os
import urllib.request
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = '/Users/vijayakumaryarrampalli/Documents/Code/Lambdas/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def upload_form():
	return render_template('index-wip.html')

@app.route('/uploadFile', methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
        isthisFile=request.files.get('file')
        print(isthisFile)
        print(isthisFile.filename)
        isthisFile.save("./"+isthisFile.filename)
		flash('Files successfully uploaded')
		return redirect('/')
        # # check if the post request has the files part
		# files = request.files.getlist('form_data')
		# for file in files:
		# 	if file and allowed_file(file.filename):
		# 		filename = secure_filename(file.filename)
		# 		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		# flash('Files successfully uploaded')
		# return redirect('/')


if __name__ == '__main__':
    app.run()