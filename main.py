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

        print("\n1 - View Speakers & Sessions")
        print("2 - Exit")

        choice = input("Choice: ")

        if choice == "1":

            name = input("Enter speaker name: ")
            
        elif choice == "2":
            break
        
        else:
            print("Invalid choice.")
            
        except Exception as e:
            print("Error:", e)
           
            
# 📚 References: 
# - https://www.w3schools.com/python/python_while_loops.asp
# - https://www.geeksforgeeks.org/python/how-to-use-while-true-in-python/
# - https://stackoverflow.com/questions/64839728/how-do-i-return-to-the-beginning-of-the-function
# - https://www.w3schools.com/python/python_if_elif.asp
# - https://stackoverflow.com/questions/17166074/most-efficient-way-of-making-an-if-elif-elif-else-statement-when-the-else-is-don
# - https://www.geeksforgeeks.org/python/difference-between-except-and-except-exception-as-e/
# - https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e