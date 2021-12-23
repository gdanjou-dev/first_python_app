import mysql.connector

conn = mysql.connector.connect (user='', password='', host='',buffered=True,database="information_schema")

mycursor = conn.cursor()
 
mycursor.execute("Show tables;")
myresult = mycursor.fetchall()

list_tables = []
for x in myresult:
    print(x[0])
    try:
      mycursor.execute("SELECT * FROM {}".format(x[0]))
      myresult = mycursor.fetchall()
      print(myresult)
    except:
      pass
    

#run = mysql.connector
#connection = run.connect(host="162.241.253.195", user="danalysi_g", password="test1", database="danalysi_name")

