from flask import Flask,redirect,url_for,render_template,request
app = Flask('__name__')
@app.route("/file")
def file_upload():
	return render_template("file_upload.html")

@app.route("/success",methods =["post"])
def success():
	if request.method=='post':
		f=request.files["files"]
		f.save(f.filename)
		return render_template("display.html",name=f.filename)
		if __name__ =='__main__':
			app.run(debug=True)