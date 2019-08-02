from flask import Flask,redirect,url_for,render_template
app = Flask('__name__')
@app.route("/home")
def home():
	return"hi bvc"
@app.route("/santosh")
def hi():
	return"hi python"
@app.route("/data/<name><age><village><cllg>")
def data(name,age,village,cllg):
	name ="santosh"
	age = 19
	village = "rajahmundry"
	cllg = "bvc"
	return "<font color = 'blue'>" "hello {} <p></p> my name is {} <p></p> my age is {} <p></p> my village {}".format(name,age,village,cllg)
@app.route("/user/<name>")
def user(name):
	if name == 'home':
		return redirect(url_for("home"))
	if name =='santosh':
		return redirect(url_for("santosh"))
		@app.route("/likhi/<int:num>")
def table(num):
	return render_template("likhi.html",n=num)

dummy_data=[
{'name':'saral',
'org':'APSSDC',
'DOB':'30 jun 1993'},
{'name':'satya',
'clg':'BVC',
'DOB':'11 2 2001'}]

@app.route("/show2")
def show2_data():
	return render_template("show2_data.html",d=dummy_data)


@app.route("/rigister")
def rigister():
	return render_template("rigister.html")
if __name__ =='__main__':
	app.run(debug=True)
