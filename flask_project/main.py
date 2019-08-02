from flask import Flask,redirect,url_for,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Register,Base

engine=create_engine('sqlite:///bvc.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine
Dbsession=sessionmaker(bind=engine)
session=Dbsession()


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
@app.route("/sample/<int:num>")
def table(num):
	return render_template("sample2.html",n=num)

@app.route("/register")
def register():
		return render_template("register.html")

@app.route("/show_data")
def  show_data():
	register=session.query(Register).all()
	return render_template('show.html',register=register)


@app.route('/add',methods=["POST","GET"])
def addData():
	if request.method == 'POST':
		newData=Register(name=request.form['name'],
			surname=request.form['surname'],
			roll_no=request.form['roll_no'],
			mobile=request.form['mobile'],
			branch=request.form['branch'])
		session.add(newData)
		session.commit()
		return redirect(url_for ('show_data'))
	else:
	    return render_template('new.html')	  
			



@app.route('/<int:register_id>/edit',methods=["POST","GET"])
def editData(register_id):
	editedData=session.query(Register).filter_by(id=register_id).one()

	if request .method=="POST":
		editedData.name=request.form['name']
		editedData.surname=request.form['surname']
		editedData.roll_no=request.form['roll_no']
		editedData.mobile=request.form['mobile']
		editedData.branch=request.form['branch']
		session.add(editedData)
		session.commit()
		return redirect(url_for('show_data'))
	else:
		return render_template('edit.html',register=editedData)



@app.route('/<int:register_id>/delete/',methods=["POST","GET"])
def deleteData(register_id):
	deletedData=session.query(Register).filter_by(id=register_id).one()
	if request.method=="POST":
		session.delete(deletedData)
		session.commit()
		return redirect(url_for('show_data',register_id=register_id))
	else:
		return render_template('delete.html',register=deletedData)







if __name__ =='__main__':
	app.run(debug=True)
