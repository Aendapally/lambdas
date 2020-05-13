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
@app.route('/getaccounts', methods=['GET','POST'])
def hello():
    print(request.form)
    eventid = request.form['eventid']
    authtoken = request.form['authtoken']
    moduleid = request.form['moduleid']
    # print(eventid)
    # print(authtoken)
    # print(moduleid)
    sdk = eesdk.EESDK("https://api.eventengine.run", authtoken, eventid, moduleid)
    #print(sdk)
    items = (sdk.get_all_teams()[0]['team-hash'])
    print(items)
    return('Success')

@app.route('/uploadFile', methods=['GET','POST'])
def upload_file():
    #print(request.files)
    #print(request)
    if request.method == 'POST':
        files = request.files
        for f in files.items(multi=True):
            #print(f)
            #print(f[1])
            k = f[1]
            if k and allowed_file(k.filename):
                filename = secure_filename(k.filename)
                k.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #print(files)
                return('File upload was Successful')


if __name__ == '__main__':
    app.run()