import mysql.connector


try:
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='testorina'
    )
    mycur=conn.cursor()
    mycur.execute("INSERT INTO testi('name','adress') values("ahmed","beni mellal")")
except mysql.connector.Error as r :
    print(r)