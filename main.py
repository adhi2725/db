from fastapi import FastAPI
import mysql.connector
from datetime import datetime,date

app = FastAPI()
mydb = mysql.connector.connect(
    host = "cnlbvh.h.filess.io",
    user = "clgfees_towertrace",
    password="4227ca4efc7d0fa1193fef328a8792f427b6774e",
    database= "clgfees_towertrace",
    port="3307"
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
         detail:str,
         bill_no : int,
         amt_payed : int,
         method : str,
         bill_date : date):
    sql = "INSERT INTO fees VALUES(%s,%s,%s,%s,%s,%s)"
    val = (spr_no, detail, bill_no,amt_payed, method,bill_date)
    mycursor.execute(sql,val)
    mydb.commit()
    return {"Message": "Values insert successfully "}

@app.patch("/update1")
def update1(old :int , new :int):
    sql = "UPDATE stu SET spr_NO = %s WHERE spr_NO =%s"
    val = (new, old)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "SPR NO updated successfully "}

@app.patch("/update2")
def update2(spr_no :int , name:str):
    sql = "UPDATE stu SET name = %s WHERE spr_NO =%s"
    val = (name, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "NAME updated successfully "}

@app.patch("/update3")
def update3(spr_no :int , dept:str):
    sql = "UPDATE stu SET dept = %s WHERE spr_NO =%s"
    val = (dept, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "DEPT updated successfully "}

@app.patch("/update4")
def update4(spr_no :int , ph:int):
    sql = "UPDATE stu SET PH_NO = %s WHERE spr_NO =%s"
    val = (ph, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "PHONE NO  updated successfully "}

@app.patch("/update5")
def update5(spr_no :int , tf :int):
    sql = "UPDATE stu SET  TUSION_FEES = %s WHERE spr_NO =%s"
    val = (tf, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "TUSION FEES  updated successfully "}

@app.patch("/update6")
def update6(spr_no :int , hf :int):
    sql = "UPDATE stu SET  HOSTEL_FEES = %s WHERE spr_NO =%s"
    val = (hf, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "HOSTEL FEES  updated successfully "}

@app.patch("/update7")
def update7(spr_no :int , bf :int):
    sql = "UPDATE stu SET  BUS_FEES = %s WHERE spr_NO =%s"
    val = (bf, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "BUS FEES updated successfully "}

@app.patch("/update8")
def update8(spr_no :int , mf :int):
    sql = "UPDATE stu SET  MESS_FEES = %s WHERE spr_NO =%s"
    val = (mf, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "MESS FEES updated successfully "}

@app.patch("/update9")
def update9(spr_no :int , mtf :int):
    sql = "UPDATE stu SET  maintances_FEES = %s WHERE spr_NO =%s"
    val = (mtf, spr_no)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"Message": "MANITANCES FEES updated successfully "}

@app.get("/delete")
def delete(spr_no:str):

    sql = "DELETE FROM STU WHERE spr_no ='" + spr_no + "'"
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
    mycursor.execute("SELECT * from FEES")
    myresult = mycursor.fetchall()
    return{"PAYMENT DETAILS":myresult}
@app.get("/all")
def all():
    sql= "SELECT STU.SPR_NO,STU.NAME,STU.DEPT,STU.PH_NO,STU.TUSION_FEES,STU.HOSTEL_FEES,STU.MESS_FEES,STU.BUS_FEES,STU.maintances_fees ,FEES.DETAIL,FEES.BILL_NO,FEES.BILL_DATE,FEES.AMT_PAYED,FEES.METHOD FROM STU INNER JOIN FEES ON STU.SPR_NO = FEES.SPR_NO GROUP BY STU.SPR_NO,STU.NAME,STU.DEPT,STU.PH_NO,STU.TUSION_FEES,STU.HOSTEL_FEES,STU.MESS_FEES,STU.BUS_FEES,STU.maintances_fees ,FEES.DETAIL,FEES.BILL_NO,FEES.BILL_DATE,FEES.AMT_PAYED,FEES.METHOD "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return {"PAYMENT DETAILS": myresult}

@app.get("/det")
def det(spr_no: int):
    val=(spr_no,)
    sql="SELECT STU.SPR_NO,STU.NAME,STU.DEPT,STU.PH_NO,STU.TUSION_FEES,STU.HOSTEL_FEES,STU.MESS_FEES,STU.BUS_FEES,STU.maintances_fees ,FEES.DETAIL,FEES.BILL_NO,FEES.BILL_DATE,FEES.AMT_PAYED,FEES.METHOD FROM STU INNER JOIN FEES ON STU.SPR_NO = FEES.SPR_NO where fees.spr_no= %s GROUP BY STU.SPR_NO,STU.NAME,STU.DEPT,STU.PH_NO,STU.TUSION_FEES,STU.HOSTEL_FEES,STU.MESS_FEES,STU.BUS_FEES,STU.maintances_fees ,FEES.DETAIL,FEES.BILL_NO,FEES.BILL_DATE,FEES.AMT_PAYED,FEES.METHOD"
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return {"PAYMENT DETAILS": myresult}
@app.get("/bet")
def bet(from_date: date,to_date :date):
    val=(from_date,to_date)
    sql = "SELECT STU.SPR_NO,STU.NAME,STU.DEPT,STU.PH_NO,STU.TUSION_FEES,STU.HOSTEL_FEES,STU.MESS_FEES,STU.BUS_FEES,STU.maintances_fees ,FEES.DETAIL,FEES.BILL_NO,FEES.BILL_DATE,FEES.AMT_PAYED,FEES.METHOD FROM STU INNER JOIN FEES ON STU.SPR_NO = FEES.SPR_NO where bill_date between %s and %s GROUP BY STU.SPR_NO,STU.NAME,STU.DEPT,STU.PH_NO,STU.TUSION_FEES,STU.HOSTEL_FEES,STU.MESS_FEES,STU.BUS_FEES,STU.maintances_fees ,FEES.DETAIL,FEES.BILL_NO,FEES.BILL_DATE,FEES.AMT_PAYED,FEES.METHOD"
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return {"PAYMENT DETAILS": myresult}
