from flask import Flask, redirect,url_for,request,render_template
from werkzeug.utils import secure_filename
import re
app = Flask(__name__)
import pymysql

db = pymysql.connect("46.4.115.158", "root", "Admin@123", "rhombus")

x = db.cursor()


@app.route('/fresher')
def fresher():
      return render_template("uploadR.html")


@app.route('/experienced')
def experienced():
      return render_template("uploadRE.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file_Given():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "file uploaded successfully"


@app.route('/signup', methods = ['GET'])
def signup():
    user_name = request.args.get('user_name')
    password = request.args.get('password')
    conform_password = request.args.get('conform_password')
    x_passout = request.args.get('x_passout')
    x_percent = request.args.get('x_percent')
    xii_passout = request.args.get('xii_passout')
    xii_percent = request.args.get('xii_percent')
    college_passout = request.args.get('college_passout')
    college_percent = request.args.get('college_percent')
    experience = request.args.get('experience')
    print(experience)
    x.execute("""INSERT INTO demo VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (user_name, password, conform_password, x_passout, x_percent, xii_passout, xii_percent, college_passout,college_percent, experience))
    print("Successful")
    db.commit()
    db.close()
    try:
     if experience == 0:
            return (redirect(url_for('fresher')))
     else:
            return (redirect(url_for('experienced')))
    except:
        print("Something Error")
    return render_template("first.html")


@app.route('/login')
def login():
    username = request.args.get('username')
    print(username)
    password = request.args.get('password')
    print(password)
    x.execute("SELECT name FROM demo")
    xx = x.fetchall()
    new1 = str(xx)
    aa = re.sub(r"[^\w]", " ", new1)
    print(aa)
    x.execute("SELECT password FROM demo")
    y = x.fetchall()
    new2 = str(y)
    bb = re.sub(r"[^\w]", " ", new2)
    print(bb)
    if username in aa and password in bb:
        print("username and password Present")
    else:
        print("username or password wrong")
    return render_template("login.html")




if __name__ == '__main__':
    app.run(debug = True)