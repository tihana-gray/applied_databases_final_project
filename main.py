import pymysql

# Function for option 1: View Speakers & Sessions
def view_speakers(conn):

    name = input("Enter speaker name: ")

    query = """
SELECT session.speakerName, session.sessionTitle, room.roomName
FROM session
JOIN room ON session.roomID = room.roomID
WHERE session.speakerName LIKE %s
"""

    try:
        cursor = conn.cursor()
        cursor.execute(query, ("%" + name + "%",))
        results = cursor.fetchall()

        for row in results:
            print("\nSpeaker:", row["speakerName"])
            print("Session:", row["sessionTitle"])
            print("Room:", row["roomName"])

    except Exception as e:
        print("Error:", e)

        # 📚 References:
            # https://www.w3schools.com/sql/sql_like.asp
            # https://stackoverflow.com/questions/5266430/how-to-see-the-real-sql-query-in-python-cursor-execute-using-pyodbc-and-ms-acces
            # https://www.w3schools.com/python/python_for_loops.asp
            # https://stackoverflow.com/questions/17861152/cursor-fetchall-vs-listcursor-in-python
            # https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/


# Function for option 2: View Attendees by Company
def view_attendees_by_company(conn):

    while True:
        company_id = input("Enter Company ID: ")

        try:
            company_id = int(company_id)

            if company_id > 0:
                break
            else:
                print("Invalid input. Please enter a number greater than 0.")

        except:
            print("Invalid input. Please enter a valid number.")

    query = """
SELECT attendee.attendeeName, attendee.attendeeDOB,
session.sessionTitle, session.speakerName,
session.sessionDate, room.roomName
FROM attendee
JOIN company ON attendee.attendeeCompanyID = company.companyID
JOIN registration ON attendee.attendeeID = registration.attendeeID
JOIN session ON registration.sessionID = session.sessionID
JOIN room ON session.roomID = room.roomID
WHERE company.companyID = %s
"""

    try:
        cursor = conn.cursor()
        cursor.execute(query, (company_id,))
        results = cursor.fetchall()

        print("\nCompany ID:", company_id)
        
        for row in results:
            print(
                row["attendeeName"], "|",
                row["attendeeDOB"], "|",
                row["sessionTitle"], "|",
                row["speakerName"], "|",
                row["sessionDate"], "|",
                row["roomName"]
            )

    except Exception as e:
        print("Error:", e)

# Function for option 3: Add New Attendee
def add_attendee(conn):

    cursor = conn.cursor()

    # Collecting inputs
    attendee_id = input("Enter Attendee ID: ")
    name = input("Enter Attendee Name: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    gender = input("Enter Gender (Male/Female): ")
    company_id = input("Enter Company ID: ")
    
    errors = False

    # Attendee ID 
    try:
        int(attendee_id)
    except:
        print("*** ERROR *** Invalid Attendee ID")
        errors = True

    # Name must not be empty
    if name == "":
        print("*** ERROR *** Invalid Name")
        errors = True

    # DOB must be YYYY-MM-DD
    try:
        parts = dob.split("-")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        if month < 1 or month > 12:
            print("*** ERROR *** Invalid Date Format")
            errors = True

        if day < 1 or day > 31:
            print("*** ERROR *** Invalid Date Format")
            errors = True

    except:
        print("*** ERROR *** Invalid Date Format")
        errors = True

    # Gender check
    if gender.lower() != "male" and gender.lower() != "female":
        print("*** ERROR *** Gender must be Male/Female")
        errors = True

    # Company ID 
    valid_company_id = True
    try:
        int(company_id)
    except:
        print("*** ERROR *** Invalid Company ID")
        errors = True
        valid_company_id = False

    try:
        # Duplicate check (only if ID is valid integer)
        if not errors:
            check_query = "SELECT * FROM attendee WHERE attendeeID = %s"
            cursor.execute(check_query, (attendee_id,))
            result = cursor.fetchone()

        if result:
            print(f"*** ERROR *** Attendee ID: {attendee_id} already exists")
            errors = True

        # Company exists check (only if integer was valid)
        if valid_company_id:
            check_company = "SELECT * FROM company WHERE companyID = %s"
            cursor.execute(check_company, (company_id,))
            company_result = cursor.fetchone()

        if not company_result:
            print(f"*** ERROR *** Company ID: {company_id} does not exist")
            errors = True
            
        # STOP before insert if any errors
        if errors:
            return

        # Insert
        insert_query = """
        INSERT INTO attendee (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (attendee_id, name, dob, gender, company_id))
        conn.commit()
        print("Attendee successfully added")

    except Exception as e:
        print(f"*** ERROR *** {e}")

# 📚 References:
# https://stackoverflow.com/questions/48143659/cursor-fetchone-returns-none-even-though-a-value-exists
# https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
# https://stackoverflow.com/questions/48143659/cursor-fetchone-returns-none-even-though-a-value-exists
# https://stackoverflow.com/questions/70787236/inserting-a-sql-query-from-python
# https://www.w3schools.com/PYTHON/python_mysql_insert.asp
# https://www.geeksforgeeks.org/python/python-mysql-insert-into-table/
# https://www.geeksforgeeks.org/sql/sql-not-equal-operator/
# https://www.w3schools.com/python/gloss_python_comparison_operators.asp

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
    # https://stackoverflow.com/questions/32754461/how-to-install-mysql-connector-via-pip
    # https://www.w3schools.com/python/python_mysql_getstarted.asp
    # https://www.geeksforgeeks.org/python/how-to-install-mysql-connector-package-in-python/

    while True:
        print("\nConference Management")
        print("---------------------")
        print("\nMENU")
        print("====")
        print("1 - View Speakers & Sessions")
        print("2 - View Attendees by Company")
        print("3 - Add New Attendee")
        print("4 - View Connected Attendees")
        print("5 - Add Attendee Connection")
        print("6 - View Rooms")
        print("x - Exit application")

        choice = input("Choice: ")

        if choice == "1":
            view_speakers(conn)

        elif choice == "2":
            view_attendees_by_company(conn)

        elif choice == "3":
            add_attendee(conn)

        elif choice == "4":
            print("This option is not available yet")

        elif choice == "5":
            print("This option is not available yet")

        elif choice == "6":
            print("This option is not available yet")

        elif choice.lower() == "x":
            print("Exiting application...")
            break

        else:
            print("Invalid choice.")

except Exception as e:
    print("Error:", e)


# 📚 References: 
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.geeksforgeeks.org/python/how-to-use-while-true-in-python/
# https://stackoverflow.com/questions/64839728/how-do-i-return-to-the-beginning-of-the-function
# https://www.w3schools.com/python/python_if_elif.asp
# https://stackoverflow.com/questions/17166074/most-efficient-way-of-making-an-if-elif-elif-else-statement-when-the-else-is-don
# https://www.geeksforgeeks.org/python/difference-between-except-and-except-exception-as-e/
# https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e



