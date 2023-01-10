import mysql.connector


try:
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='testorina'
    )
    mycur=conn.cursor()
    mycur.execute("""
    INSERT INTO testi values("valeria","sisil")
    """)
    conn.commit()
except mysql.connector.Error as r :
    print(r)