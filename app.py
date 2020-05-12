from flask import Flask, flash, request, redirect, render_template
import os
import urllib.request
from werkzeug.utils import secure_filename
from flask_cors import CORS
import json
import eesdk

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = '/Users/aaendapa/Documents/Code/lambdas/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/getaccounts')
def hello(event_id, token, module_id):
	print(request)
    sdk = eesdk.EESDK("https://api.eventengine.run", token, event_id, module_id)
    return json.dumps(sdk.get_all_teams())

@app.route('/uploadFile', methods=['GET','POST'])
def upload_file():
	print(request.files)
	if request.method == 'POST':
        # isthisFile=request.files.get('file')
        # print(isthisFile)
        # print(isthisFile.filename)
        # isthisFile.save("./"+isthisFile.filename)
		# flash('Files successfully uploaded')
		# 
        # check if the post request has the files part
		files = request.files
		for f in files.items(multi=True):
			print(f)
			print(f[1])
			k = f[1]
			if k and allowed_file(k.filename):
				filename = secure_filename(k.filename)
				k.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		print(files)
		return('Success')
		# for file in files:
		# 	f = file[1]
		# 	print(f)
		# 	if f and allowed_file(f.filename):
		# 		filename = secure_filename(f.filename)
		# 		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


if __name__ == '__main__':
    app.run()