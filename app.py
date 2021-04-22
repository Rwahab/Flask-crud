from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/flaskcrud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='your_user', password='password', server='localhost', database='dname')

db = SQLAlchemy(app)

  

class Employees(db.Model):
    
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(100),nullable =False)
    email = db.Column(db.String(100),nullable =False)
    phone = db.Column(db.Integer,nullable =False)

    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

class Mydb(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    address = db.Column(db.String(100),nullable =False)
    contact = db.Column(db.String(100),nullable =False)
    status = db.Column(db.Integer,nullable =False)

    def __init__(self,name,email,phone):
        self.address = address
        self.contact = contact
        self.status = status





@app.route('/')
def Index():
    all_data = Employees.query.all()


    return render_template("index.html", employees= all_data )




@app.route('/insert', methods= ['POST'])
def insert():
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Employees(name,email,phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee inserted successfully")

        return redirect(url_for('Index'))

@app.route('/update', methods= ['GET', 'POST'])
def update():

    if request.method == 'POST':

        my_data = Employees.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()
        flash("Empoyee updated successfully")

        return redirect(url_for('Index'))

@app.route('/delete/<id>', methods =['GET', 'POST'])
def delete(id):
    my_data = Employees.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee deleted successfully")

    return redirect(url_for('Index'))



if __name__ == '__main__':
    app.run(debug=True)   
    




    

