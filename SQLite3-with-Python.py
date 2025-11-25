import sqlite3
Database_name='Emplyoee_data.db'

def connect_to_db():
    try:
        con=sqlite3.connect(Database_name)
        cursor=con.cursor()
        print(" Database is Connected Established ")
    except:
        print('Error hai Connection main')
    return con

def create_table(con):
    q="CREATE TABLE IF NOT EXISTS Employee (" \
    "Empid INTEGER PRIMARY KEY," \
    "Empname TEXT NOT NULL," \
    "Department TEXT NOT NULL," \
    "Salary REAL NOT NULL);"
    cursor=con.cursor()
    cursor.execute(q)
    
def insert_record(con,Employee):
    cursor=con.cursor()
    q="INSERT INTO Employee (Empid,Empname,Department,Salary) VALUES (?,?,?,?)"
    cursor.executemany(q,Employee)
    print(len(Employee),' Record Inserted Succesfully!!!!!')
    
def view_records(con):
    cursor=con.cursor()
    q="SELECT * FROM Employee "
    cursor.execute(q)
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    
def main():
    con=connect_to_db()
    create_table(con)
    Employee=[
        (1,'ANANT',"IT",88000),
        (2,'ANSHUMANN',"IT",50000),
        (3,'ANIMESH',"MANAGER",48000),
        (4,'ANIKET',"SALES",82000),
        (5,'ADITYA',"MANAGER",45000),
        ]
    insert_record(con,Employee)
    view_records(con)
    if con: 
        con.close()

if __name__=='__main__':
    main()