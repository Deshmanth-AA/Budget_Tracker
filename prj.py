from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
from flask_mysqldb import MySQL
from pytz import timezone
from datetime import datetime
from dateutil import parser 
import pytz
import json
from json import JSONEncoder
from werkzeug.utils import secure_filename




app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bgt'
CORS(app) 
 
app.secret_key = 'your secret key'
mysql = MySQL(app)
now_utc = datetime.now(timezone('UTC'))
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))

@app.route('/launch',methods=['GET', 'POST'])
def launch():
    return render_template('launchpage.html')

@app.route('/audreg',methods=['GET', 'POST'])
def audreg():
    return render_template('auditorsignup.html')

import hashlib
@app.route('/register', methods=['GET','POST'])
def register():
    aname=request.form.get('aname')
    phnum=request.form.get('phnum')
    pwd=request.form.get('pwd')
    
    cursor=mysql.connection.cursor()
    #pwd = hashlib.md5(pwd.encode('utf-8')).digest()
    cursor.execute(''' INSERT INTO auditor(aname,phnum,pwd) VALUES(%s,%s,MD5(%s))''',(aname,phnum,pwd))
    mysql.connection.commit()
    cursor.close()
    return "success"

@app.route('/audlogin', methods=['GET', 'POST'])

def audlogin():
    aname=request.form.get('aname')
    pwd=request.form.get('pwd')
    cursor=mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM auditor WHERE aname=%s and pwd=MD5(%s)''',(aname,pwd))
    row=cursor.fetchone()
    cursor.close()
    if row:
        
            return ("successfully logged")
        
        
    else:
        return "Failed to login"

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('auditorlogin.html')


@app.route('/deptreg',methods=['GET', 'POST'])
def deptreg():
    return render_template('deptreg.html')

import hashlib
@app.route('/deptregister', methods=['GET','POST'])
def deptregister():
    dname=request.form.get('dname')
    location=request.form.get('location')
    pwd=request.form.get('pwd')
    
    cursor=mysql.connection.cursor()
    #pwd = hashlib.md5(pwd.encode('utf-8')).digest()
    cursor.execute(''' INSERT INTO department(dname,location,pwd) VALUES(%s,%s,MD5(%s))''',(dname,location,pwd))
    mysql.connection.commit()
    cursor.close()
    return "success"

@app.route('/dlogin', methods=['GET', 'POST'])

def dlogin():
    dname=request.form.get('dname')
    pwd=request.form.get('pwd')
    cursor=mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM department WHERE dname=%s and pwd=MD5(%s)''',(dname,pwd))
    row=cursor.fetchone()
    cursor.close()
    if row:
        
            return ("successfully logged")
        
        
    else:
        return "Failed to login"

@app.route('/deptlogin', methods=['GET','POST'])
def deptlogin():
    return render_template('deptlogin.html')

@app.route('/adminlogin', methods=['GET'])
def adminlogin():
    return render_template('adminlogin.html')


@app.route('/admin', methods =['GET', 'POST'])
def admin():
    
     username = request.form.get('aname')
     password = request.form.get('pwd')
     print(username, password)
     if username == 'admin' and password == 'ppp':
        #  return redirect(url_for('adminlogin', username=username))
         
         return ('success')
     else:
         return ('Login failed')
    
@app.route('/empinsert', methods =['GET', 'POST'])
def empinsert():
    
    ename = request.form.get('ename')
    position = request.form.get('position')
    deptID = request.form.get('deptID')
    
    # date_object = parser.parse(sdate)
    # sdate = date_object.astimezone(pytz.timezone('Asia/Kolkata')) 
    #print(date_object)
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO employee(ename,position,deptID) VALUES(%s,%s,%s)''',(ename,position,deptID))
    mysql.connection.commit()
    cursor.close()
    return "Inserted successfully"

@app.route('/budinsert', methods =['GET', 'POST'])

def budinsert():
    amnt_san=request.form.get('amnt_san')
    dateofsan=request.form.get('dateofsan')
    head=request.form.get('head')
    deptID=request.form.get('deptID')
    empID=request.form.get('empID')

    cursor=mysql.connection.cursor()
    cursor.execute(''' INSERT INTO budget(amnt_san,dateofsan,head,deptID,empID) VALUES(%s,%s,%s,%s,%s)''',(amnt_san,dateofsan,head,deptID,empID))
    mysql.connection.commit()
    cursor.close()
    return "Inserted successfully"

@app.route('/expinsert', methods =['GET', 'POST'])
def expinsert():
    
    
    edate = request.form.get('edate')
    purpose=request.form.get('purpose')
    amount=request.form.get('amount')
    budgetID=request.form.get('budgetID')
    # f = request.files['rfile']       
    # filename = secure_filename(f.filename)
    # now = datetime.now()
    # dt_string = now.strftime("%d%m%Y%H%M%S")
    # rimg=dt_string+"_"+filename
    # f.save("static/resources/" + rimg)
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO expense(edate,purpose,amount,budgetID) VALUES(%s,%s,%s,%s)''',(edate,purpose,amount,budgetID))
    mysql.connection.commit()
    cursor.close()
    return "Inserted successfully"


@app.route('/empupdate', methods =['GET', 'POST'])
def empupdate():
    
    ename = request.form.get('ename')
    position = request.form.get('position')
    deptID = request.form.get('deptID')
    empID = request.form.get('empID')
    
    # date_object = parser.parse(sdate)
    # sdate = date_object.astimezone(pytz.timezone('Asia/Kolkata')) 
    #print(date_object)
    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE employee SET ename=%s,position=%s,deptID=%s WHERE empID=%s''',(ename,position,deptID,empID))
    mysql.connection.commit()
    cursor.close()
    return "Updated successfully"

@app.route('/budupdate', methods =['GET', 'POST'])
def budupdate():
    
    amnt_san=request.form.get('amnt_san')
    dateofsan=request.form.get('dateofsan')
    head=request.form.get('head')
    deptID=request.form.get('deptID')
    budgetID=request.form.get('budgetID')
    empID=request.form.get('empID')
    
    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE budget SET amnt_san=%s,dateofsan=%s,head=%s,deptID=%s,empID=%s WHERE budgetID=%s''',(amnt_san,dateofsan,head,deptID,budgetID,empID))
    mysql.connection.commit()
    cursor.close()
    return "Updated successfully"


@app.route('/empdelete', methods =['GET', 'POST'])
def empdelete():
    
    empID=request.form.get('empID')
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM employee WHERE empID=%s''',(empID,))
    mysql.connection.commit()
    cursor.close()
    return "Deleted successfully"

@app.route('/buddelete', methods =['GET', 'POST'])
def buddelete():
    
    budgetID=request.form.get('budgetID')
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM budget WHERE budgetID=%s''',(budgetID,))
    mysql.connection.commit()
    cursor.close()
    return "Deleted successfully"

@app.route('/expdelete', methods =['GET', 'POST'])
def expdelete():
    
    expID=request.form.get('expID')
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM expense WHERE expID=%s''',(expID,))
    mysql.connection.commit()
    cursor.close()
    return "Deleted successfully"

@app.route('/empnameshow', methods =['GET', 'POST'])

def empnameshow():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM employee")
    DBData = cursor.fetchall() 
    cursor.close()
    
    empnames=''
    for result in DBData:
        print(result)
        empnames+="<option value="+str(result[0])+">"+result[1]+"</option>"
    return empnames

@app.route('/deptnameshow', methods =['GET', 'POST'])

def deptnameshow():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM department")
    DBData = cursor.fetchall() 
    cursor.close()
    
    deptnames=''
    for result in DBData:
        print(result)
        deptnames+="<option value="+str(result[0])+">"+result[1]+"</option>"
    return deptnames

@app.route('/budnameshow', methods =['GET', 'POST'])

def budnameshow():
    
    
    
    
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM budget ")
    DBData = cursor.fetchall() 
    cursor.close()
    
    budheads=''
    for result in DBData:
        print(result)
        budheads += "<option value=" + str(result[0]) + ">" + str(result[1]) + "</option>"
    return budheads    
        
           
@app.route('/empshow', methods =['GET', 'POST'])
def empshow():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM employee")
    row_headers=[x[0] for x in cursor.description] 
    DBData = cursor.fetchall() 
    cursor.close()
    json_data=[]
    rstr="<table border><tr>"
    for r in row_headers:
        rstr=rstr+"<th>"+r+"</th>"
    rstr=rstr+"<th>Update</th><th>Delete</th></tr>"
    cnt=0
    empID=-1
    for result in DBData:
        cnt=0
        ll=['A','B','C','D','E','F','G','H','I','J','K']
        for row in result:
            if cnt==0:
                empID=row
                rstr=rstr+"<td>"+str(row)+"</td>" 
            elif cnt==3:
                rstr=rstr+"<td>"+"<input type=int id="+str(ll[cnt])+str(empID)+" value="+str(row)+"></td>"  
            else:
                rstr=rstr+"<td>"+"<input type=text id="+str(ll[cnt])+str(empID)+" value=\""+str(row)+"\"></td>"     
            cnt+=1
            
        rstr+="<td><a ><i class=\"fa fa-edit\" aria-hidden=\"true\" onclick=update("+str(empID)+")></i></a></td>"
        rstr+="<td><a ><i class=\"fa fa-trash\" aria-hidden=\"true\" onclick=del("+str(empID)+")></i></a></td>"
        
        rstr=rstr+"</tr>"
    
    rstr=rstr+"</table>"
    rstr=rstr+'''
    <script type=\"text/javascript\">
    function update(empID)
    {
       ename=$("#B"+empID).val();
       position=$("#C"+empID).val();
       deptID=$("#D"+empID).val();
       $.ajax({
        url: \"/empupdate\",
        type: \"POST\",
        data: {empID:empID,ename:ename,position:position,deptID:deptID},
        success: function(data){    
        alert(data);
        loademployees();
        }
       });
    }
   
    function del(empID)
    {
    $.ajax({
        url: \"/empdelete\",
        type: \"POST\",
        data: {empID:empID},
        success: function(data){
            alert(data);
            loademployees();
        }
        });
    }
    function loademployees(){

       $.ajax({
        url: 'http://127.0.0.1:5000/empshow',
        type: 'POST',
        success: function(data){
          $('#eshow').html(data);
        }
      });
    }
    
    
    </script>

'''
    return rstr


@app.route('/budshow', methods =['GET', 'POST'])
def budshow():
    
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM budget")
    row_headers=[x[0] for x in cursor.description] 
    DBData = cursor.fetchall() 
    cursor.close()
    json_data=[]
    rstr="<table border><tr>"
    for r in row_headers:
        rstr=rstr+"<th>"+r+"</th>"
    rstr=rstr+"<th>Update</th><th>Delete</th></tr>"
    cnt=0
    budgetID=-1
    for result in DBData:
        cnt=0
        ll=['A','B','C','D','E','F','G','H','I','J','K']
        for row in result:
            if cnt==0:
                budgetID=row
                rstr=rstr+"<td>"+str(row)+"</td>" 
           
            else:
                rstr=rstr+"<td>"+"<input type=text id="+str(ll[cnt])+str(budgetID)+" value=\""+str(row)+"\"></td>"     
            cnt+=1
            
        rstr+="<td><a ><i class=\"fa fa-edit\" aria-hidden=\"true\" onclick=budupdate("+str(budgetID)+")></i></a></td>"
        rstr+="<td><a ><i class=\"fa fa-trash\" aria-hidden=\"true\" onclick=buddel("+str(budgetID)+")></i></a></td>"
        
        rstr=rstr+"</tr>"
    
    rstr=rstr+"</table>"
    rstr=rstr+'''
    <script type=\"text/javascript\">
    function budupdate(budgetID)
    {
       //alert('aha no');
       amnt_san=$("#B"+budgetID).val();
       dateofsan=$("#C"+budgetID).val();
       head=$("#D"+budgetID).val();
       deptID=$("#E"+budgetID).val();


       $.ajax({
        url: \"/budupdate\",
        type: \"POST\",
        data: {budgetID:budgetID,amnt_san:amnt_san,dateofsan:dateofsan,head:head,deptID:deptID},
        success: function(data){
       
        alert(data);
        loadbudgets();
        }
       });
    }
   
    function buddel(budgetID)
    {
    $.ajax({
        url: \"/buddelete\",
        type: \"POST\",
        data: {budgetID:budgetID},
        success: function(data){
        alert(data);
        loadbudgets();
        }
        });
    }
   
    function loadbudgets(){
       $.ajax({
        url: 'http://127.0.0.1:5000/budshow',
        type: 'POST',
        success: function(data){
          $('#bshow').html(data);
        }
      });
    }
    
    
    </script>

'''
    return rstr
@app.route('/expupdate', methods=['GET', 'POST'])

def expupdate():
    edate=request.form.get('edate')
    purpose=request.form.get('purpose')
    amount=request.form.get('amount')
    budgetID=request.form.get('budgetID')
    expID=request.form.get('expID')
    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE expense SET edate=%s,purpose=%s,amount=%s,budgetID=%s WHERE expID=%s''',(edate,purpose,amount,budgetID,expID))
    mysql.connection.commit()
    cursor.close()
    return "Updated successfully"

@app.route('/expshow', methods=['GET', 'POST'])

def expshow():
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM expense")
    row_headers=[x[0] for x in cursor.description] 
    DBData = cursor.fetchall() 
    cursor.close()
    json_data=[]
    rstr="<table border><tr>"
    for r in row_headers:
        rstr=rstr+"<th>"+r+"</th>"
    rstr=rstr+"<th>Update</th><th>Delete</th></tr>"
    cnt=0
    expID=-1
    for result in DBData:
        cnt=0
        ll=['A','B','C','D','E','F','G','H','I','J','K']
        for row in result:
            if cnt==0:
                expID=row
                rstr=rstr+"<td>"+str(row)+"</td>" 
            else:
                rstr=rstr+"<td>"+"<input type=text id="+str(ll[cnt])+str(expID)+" value=\""+str(row)+"\"></td>"     
            cnt+=1
            
        rstr+="<td><a ><i class=\"fa fa-edit\" aria-hidden=\"true\" onclick=expupdate("+str(expID)+")></i></a></td>"
        rstr+="<td><a ><i class=\"fa fa-trash\" aria-hidden=\"true\" onclick=expdel("+str(expID)+")></i></a></td>"
        
        rstr=rstr+"</tr>"
    
    rstr=rstr+"</table>"
    rstr=rstr+'''
    <script type=\"text/javascript\">
    function expupdate(expID)
    {
       //alert('aha no');

       edate=$("#B"+expID).val();
       purpose=$("#C"+expID).val();
       amount=$("#D"+expID).val();
       budgetID=$("#E"+expID).val();
       var fd=new FormData();
       fd.append('edate',edate);
       fd.append('purpose',purpose);
       fd.append('amount',amount);
       fd.append('budgetID',budgetID);

       $.ajax({
        url: \"/expupdate\",
        type: \"POST\",
        data: fd,
        processData: false,
        contentType: false,
        success: function(data){
       
        alert(data);
        loadexpenses();
        }
       });
    }
   
    function expdel(expID)
    {
    $.ajax({
        url: \"/expdelete\",
        type: \"POST\",
        data: {expID:expID},
        success: function(data){
        alert(data);
        loadexpenses();
        }
        });
    }


     
   
    
    function loadexpenses(){
       $.ajax({
        url: 'http://127.0.0.1:5000/expshow',
        type: 'POST',
        success: function(data){
          $('#expshow').html(data);
        }
      });
    }
    
    
    </script>

'''
    return rstr


                              
@app.route('/deptnav', methods =['GET', 'POST'])
def deptnav():
    return render_template('deptnav.html')

@app.route('/audnav', methods =['GET', 'POST'])
def audnav():
    return render_template('demo.html')


if __name__ == '__main__':
    app.run(debug=True)