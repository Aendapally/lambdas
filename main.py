def uploadfiles(request):
    files = request.files
		for f in files.items(multi=True):
			k = f[1]
			if k and allowed_file(k.filename):
				filename = secure_filename(k.filename)
				k.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return('Success')
    