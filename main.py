import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="appdbproj",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

    print("Connected successfully!")

# 📚 References: 
# - https://stackoverflow.com/questions/32754461/how-to-install-mysql-connector-via-pip
# - https://www.w3schools.com/python/python_mysql_getstarted.asp
# - https://www.geeksforgeeks.org/python/how-to-install-mysql-connector-package-in-python/

# Running a simple query to test the connection
    query = "SELECT * FROM attendee"

    with conn:
        cursor = conn.cursor()  
        cursor.execute(query)

        subjects = cursor.fetchall()

        for s in subjects:
            print(s)  
# Prevents crashing the program and prints any errors that occur during the connection or query execution
except Exception as e:
    print("Error:", e)