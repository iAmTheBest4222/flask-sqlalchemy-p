import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template,request


app=Flask(__name__)
 #engine confrigation
dir_try=os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(dir_try,"university.sqlite3")

db=SQLAlchemy()
db.init_app(app)
app.app_context().push()

#these are models
class Students(db.Model):
    __tablename__="students"
    roll_no=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    mail=db.Column(db.String,nullable=False,unique=True)
    age=db.Column(db.Integer)
    cource=db.Column(db.String,db.ForeignKey("cources.c_name"),nullable=False)
    
    
class Cources(db.Model):
    __tablename__="cources"
    c_name=db.Column(db.String,primary_key=True,nullable=False)
    c_code=db.Column(db.Integer,nullable=False,unique=True)
    students=db.relationship("Students",backref="cources")

    
@app.route("/")
def f1():
    #var11=Cources.query.filter_by(c_name="btech cse").all()
    if request.method=="GET":
        return render_template("index.html",title="Login As -:")
    
@app.route("/student.html",methods=["GET","POST"])
def f2():
    #var11=Cources.query.filter_by(c_name="btech cse").all()
    if request.method=="GET":
        return render_template("student.html",a="get",b="s",title="Log in using Roll no.")
    else:
        var111=Students.query.filter_by(roll_no=request.form["RollNO"]).all()
        return render_template("student.html",a="post",b="s",var111=var111,title="Details -:")
        
@app.route("/student.html/<cource>",methods=["GET","POST"])
def f4(cource):
    if request.method=="GET":
        var111=Students.query.filter_by(cource=cource).all()
        return render_template("student.html",a="post",b="s",var111=var111,title=cource+" table -:")

@app.route("/regester.html",methods=["GET","POST"])
def f5():
    if request.method=="GET":
        return render_template("regester.html",title="Form -:")
    else:
        new_student={"name":request.form["name"],"mail":request.form["mail"],"age":request.form["age"],"cource":request.form["cource"]}
        return render_template("regester.html",title="Form -:",a="post")

@app.route("/head.html",methods=["GET","POST"])
def f3():
    
    if request.method=="GET":
        return render_template("head.html",a="get",title="Diractory of -:")
    elif request.method=="POST":
        if request.form["HOD"]=="Students":
            var11=Students.query.all()
            return render_template("student.html",a="post",b="s",var111=var11,title="Students Table -:")
        elif request.form["HOD"]=="Cources":
            var11=Cources.query.all()
            return render_template("student.html",a="post",b="c",var111=var11,title="Cource Table -:")

if __name__=="__main__":
    app.debug=True
    app.run()