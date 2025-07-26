from fastapi import FastAPI
import mysql.connector
from datetime import datetime,date

app = FastAPI()
mydb = mysql.connector.connect(
    host = "cnlbvh.h.filess.io",
    user = "clgfees_towertrace",
    password="4227ca4efc7d0fa1193fef328a8792f427b6774e",
    database= "clgfees_towertrace",
    port="3307",
     connection_timeout=60
)
mycursor =mydb.cursor()
@app.get("/insert/")
def insert( spr_no : int,
            name : str,
            dept : str,
            ph_no : int,
            tusion_fees : int,
            hostel_fees : int,
            mess_fees : int,
            maintances_fees : int ,
            bus_fees : int,):
    sql = "INSERT INTO stu VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (spr_no, name, dept, ph_no, tusion_fees, hostel_fees, mess_fees, maintances_fees, bus_fees)
    mycursor.execute(sql, val)
    mydb.commit()
    return{"Message":"Values insert successfully "}

@app.get("/fees/")
def fees(spr_no:int,
         details:str,
         bill_no : int,
         bill_date : date,
         amt_payed : int,
         method : str):
    sql = "INSERT INTO fees VALUES(%s,%s,%s,%s,%s,%s)"
    val = (spr_no, details, bill_no,bill_date,amt_payed, method)
    mycursor.execute(sql,val)
    mydb.commit()
    return {"Message": "Values insert successfully "}

@app.patch("/update1")
def update1(old :int , new :int):
    sql = "UPDATE stu SET spr_nO = %s WHERE spr_no =%s"
    val = (new, old)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "SPR NO updated successfully "}

@app.patch("/update2")
def update2(spr_no :int , name:str):
    sql = "UPDATE stu SET name = %s WHERE spr_no =%s"
    val = (name, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "NAME updated successfully "}

@app.patch("/update3")
def update3(spr_no :int , dept:str):
    sql = "UPDATE stu SET dept = %s WHERE spr_no =%s"
    val = (dept, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "DEPT updated successfully "}

@app.patch("/update4")
def update4(spr_no :int , ph_no:int):
    sql = "UPDATE stu SET ph_no = %s WHERE spr_no =%s"
    val = (ph_no, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "PHONE NO  updated successfully "}

@app.patch("/update5")
def update5(spr_no :int , tusion_fees :int):
    sql = "UPDATE stu SET  tusion_fees = %s WHERE spr_no =%s"
    val = (tusion_fees, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "TUSION FEES  updated successfully "}

@app.patch("/update6")
def update6(spr_no :int , hostel_fees :int):
    sql = "UPDATE stu SET  hostel_fees = %s WHERE spr_no =%s"
    val = (hostel_fees, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "HOSTEL FEES  updated successfully "}

@app.patch("/update7")
def update7(spr_no :int , bus_fees :int):
    sql = "UPDATE stu SET  bus_fees = %s WHERE spr_no =%s"
    val = (bus_fees, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "BUS FEES updated successfully "}

@app.patch("/update8")
def update8(spr_no :int , mess_fees :int):
    sql = "UPDATE stu SET  mess_fees = %s WHERE spr_no =%s"
    val = (mess_fees, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "MESS FEES updated successfully "}

@app.patch("/update9")
def update9(spr_no :int , maintances_fees :int):
    sql = "UPDATE stu SET  maintances_fees = %s WHERE spr_no =%s"
    val = (maintances_fees, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "MANITANCES FEES updated successfully "}

@app.get("/delete")
def delete(spr_no:str):

    sql = "DELETE FROM stu WHERE spr_no ='" + spr_no + "'"
    mycursor.execute(sql)
    mydb.commit()
    return {"message": "Data deleted successfully"}

@app.get("/view")
def view():
    mycursor.execute("SELECT * from stu")
    myresult = mycursor.fetchall()
    return{"STUDENT DETAILS":myresult}

@app.get("/view2")
def view():
    mycursor.execute("SELECT * from fees")
    myresult = mycursor.fetchall()
    return{"PAYMENT DETAILS":myresult}
@app.get("/all")
def all():
    sql= "SELECT 
    stu.spr_no,
    stu.name,
    stu.dept,
    stu.ph_no,
    stu.tusion_fees,
    stu.hostel_fees,
    stu.mess_fees,
    stu.bus_fees,
    stu.maintances_fees,
    fees.details,
    fees.bill_no,
    fees.bill_date,
    fees.amt_payed,
    fees.method
FROM stu
INNER JOIN fees ON stu.spr_no = fees.spr_no
GROUP BY  
    stu.spr_no,
    stu.name,
    stu.dept,
    stu.ph_no,
    stu.tusion_fees,
    stu.hostel_fees,
    stu.mess_fees,
    stu.bus_fees,
    stu.maintances_fees,
    fees.details,
    fees.bill_no,
    fees.bill_date,
    fees.amt_payed,
    fees.method;
"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return {"PAYMENT DETAILS": myresult}

@app.get("/det")
def det(spr_no: int):
    val=(spr_no,)
    sql="SELECT stu.spr_no,stu.name,stu.dept,stu.ph_no,stu.tusion_fees,stu.hostel_fees,stu.mess_fees,stu.bus_fees,stu.maintances_fees ,fees.details,fees.bill_no,fees.bill_date,fees.amt_payed,fees.method FROM stu INNER JOIN fees ON stu.spr_no = fees.spr_no where fees.spr_no= %s GROUP BY stu.spr_no,stu.name,stu.dept,stu.ph_no,stu.tusion_fees,stu.hostel_fees,stu.mess_fees,stu.bus_fees,stu.maintances_fees ,fees.details,fees.bill_no,fees.bill_date,fees.amt_payed,fees.method"
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return {"PAYMENT DETAILS": myresult}
@app.get("/bet")
def bet(from_date: date,to_date :date):
    val=(from_date,to_date)
    sql = "SELECT stu.spr_no,stu.name,stu.dept,stu.ph_no,stu.tusion_fees,stu.hostel_fees,stu.mess_fees,stu.bus_fees,stu.maintances_fees ,fees.details,fees.bill_no,fees.bill_date,fees.amt_payed,fees.method FROM stu INNER JOIN fees ON stu.spr_no = fees.spr_no where bill_date between %s and %s GROUP BY stu.spr_no,stu.name,stu.dept,stu.ph_no,stu.tusion_fees,stu.hostel_fees,stu.mess_fees,stu.bus_fees,stu.maintances_fees ,fees.details,fees.bill_no,fees.bill_date,fees.amt_payed,fees.method"
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return {"PAYMENT DETAILS": myresult}
