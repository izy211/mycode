#!/usr/bin/env python3
import sqlite3

def print_rows(conn):
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print(f"ID = {row[0]}")
        print(f"NAME = {row[1]}")
        print(f"ADDR = {row[2]}")
        print(f"SALARY = {row[3]}\n")
    return 0


def main():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully!")
    
    conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
            (ID INT PRIMARY KEY NOT NULL,
            NAME    TEXT    NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50),
            SALARY  REAL);''')
    print("Table created successfully!")
    
    conn.execute("INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
    conn.execute("INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
    conn.execute("INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
    conn.execute("INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
    conn.commit()
    print("Records created successfully!")
    print_rows(conn)
    
    conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
    conn.commit()
    print_rows(conn)

    conn.execute("DELETE from COMPANY where ID = 2;")
    conn.commit()
    print_rows(conn)
    
    conn.close()

if __name__ == "__main__":
    main()
