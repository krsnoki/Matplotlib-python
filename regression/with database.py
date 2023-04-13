import mysql.connector  #importing packages
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "db2");
mycursor = mydb.cursor() # creating object of class cursor,, established the connection.

mycursor.execute("create table if not exists petrol(Sr integer(10)auto_increment primary key, Language varchar(20), Remarks integer(20))");

io = "insert into data(Language, Remark)values(%s,%d)"
value = ("Python", "255")
mycursor.execute(io, value)
mydb.commit()
