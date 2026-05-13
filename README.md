# Applied Databases Final Project

## Overview
This project is a Python application that connects to a MySQL database and a Neo4j database to perform different conference management operations.

The MySQL database stores structured data about attendees, companies, sessions, and rooms.<br>  
The Neo4j database stores connections between attendees.

---

### MySQL Database: appdbproj

The MySQL database contains the following tables:
- attendee
- company
- registration
- room
- session

These tables manage relationships between attendees, sessions, companies, registration IDs and rooms.


### Neo4j Database: appdbprojNeo4j

The Neo4j database contains:
- Nodes: Attendee
- Relationships: CONNECTED_TO

Each node represents an attendee, and relationships represent connections between attendees.

---

## Installation & Setup

### Install Required Packages

pip install pymysql neo4j


### MySQL Setup

Import the following SQL script:

appdbproj.sql.txt


### Neo4j Setup

Import the provided dataset:

appdbprojNeo4j.json


### Run the Application

python main.py


---

## Application Menu

1 - View Speakers & Sessions  
2 - View Attendees by Company  
3 - Add New Attendee  
4 - View Connected Attendees  
5 - Add Attendee Connection  
6 - View Rooms  
x - Exit application  

---

## Option 1: View Speakers & Sessions

Prompts the user to enter a speaker name.

Displays:
- Speaker name  
- Session title  
- Room name  

If no matching speakers are found, the message below is displayed:<br>
'No speakers found of that name'

## Option 2: View Attendees by Company

Prompts the user to enter a Company ID.

Displays:
- Attendee name  
- Date of birth  
- Session title  
- Speaker name  
- Session date  
- Room name  

Error handling:
- Input must be numeric  
- Company must exist  
- If no attendees are found, error message is displayed.

## Option 3: Add New Attendee

Prompts the user to enter:
- Attendee ID  
- Attendee name  
- Date of birth (YYYY-MM-DD)
- Gender (Male/Female)
- Company ID  

Validation rules:
- Attendee ID must be numeric  
- Name cannot be empty  
- Date must be in YYYY-MM-DD format  
- Gender must be Male or Female  
- Company ID must exist  
- Attendee ID must be unique  

If successful:

'Attendee successfully added'

If invalid data is entered, MySQL returns an error message which is displayed to the user.


## Option 4: View Connected Attendees

Prompts the user to enter an Attendee ID.

Displays:
- Attendee name  
- Connected attendees  

Behaviour:
- If the attendee exists but has no connections → No connections  
- If the attendee does not exist → error message  

## Option 5: Add Attendee Connection

Prompts the user to enter two Attendee IDs.

Validation:
- Both IDs must be numeric  
- IDs must be greater than 0
- IDs must not be the same  
- Both attendees must exist in the database  
- Connection must not already exist in Neo4j

If successful:

Attendee X is now connected to Attendee Y

## Option 6: View Rooms

Displays:
- Room ID  
- Room name  
- Capacity  

Important behaviour:
- Rooms are loaded once into memory  
- Any rooms added after the first load will not appear until the application is restarted  

## Exit Application

Selecting x terminates the program.

## Invalid Input

Any invalid menu option redisplays the menu.


---

## Implementation Details

- Python is used as the main programming language  
- PyMySQL is used for MySQL interaction  
- Neo4j Python driver is used for graph database interaction  
- Input validation is implemented using try/except and conditional checks  
- SQL is used for relational queries  
- Cypher is used for graph queries 
- MySQL STRICT_TRANS_TABLES mode is used to enforce data integrity


Worked with class notes as a reference and online sources.
⚠️ **Full list of online references provided with the code.**


### Author

Tihana Gray