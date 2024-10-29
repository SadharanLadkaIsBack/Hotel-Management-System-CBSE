import mysql.connector as mc
db = mc.connect(host = "localhost", password = "dav123", user = "root", database = "hotel")
cur = db.cursor()
user = "SadharanLadka"
passw = "dav123dav123"
t = cur.execute(f'select * from employee where Employee_Id = "{user}" and password = "{passw}"')
print(t)