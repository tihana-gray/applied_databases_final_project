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

while True:

        print("1 - View Speakers & Sessions")
        print("2 - Exit")

        choice = input("Choice: ")

        if choice == "1":

            name = input("Enter speaker name: ")