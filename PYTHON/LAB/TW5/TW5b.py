# 2. Develop a python program that does the following operations of an EMPLOYEE.
# Fields are :EmpID,Name, Age,Salary
# 1.Add a record
# 2.Find all records above a certain salary
# 3.Update salary of all employers by 5% who have salary less 10,000
# 4.Delete all employees with age greater than 60

import sqlite3

con = sqlite3.connect("database.db")

cur = con.cursor()


def main():
    employee_sql = """
     CREATE TABLE "employee"(
         "EmpID" integer,
         "Name" text,
         "Age" Integer,
         "Salary" Real,
         primary key("EmpID")
         )
     """

    cur.execute(employee_sql)
    # cur.execute("commit")

    # Adding records in employee table
    insert_employees = "INSERT INTO EMPLOYEE VALUES (123,'JOHN',20,'45000')"
    cur.execute(insert_employees)
    insert_employees = "INSERT INTO EMPLOYEE VALUES (111,'ABC',21,'35000')"
    cur.execute(insert_employees)
    insert_employees = "INSERT INTO EMPLOYEE VALUES (222,'DEF',22,'5000')"
    cur.execute(insert_employees)
    insert_employees = "INSERT INTO EMPLOYEE VALUES (333,'HIJ',23,'15000')"
    cur.execute(insert_employees)
    insert_employees = "INSERT INTO EMPLOYEE VALUES (444,'KLM',65,'65000')"
    cur.execute(insert_employees)
    #  #cur.execute("commit")

    # Finding records of employee having salary greater than 10000
    print("Employees Having Salary greater than 10000.0 are :: ")
    fetch_records = "select * from employee where salary > 10000"
    for row in cur.execute(fetch_records):
        print(row)

    # Updating salary of all employees by 5% who have salary less than 10000
    print("Updating salary of employee by 5% who have salary less than 10000")
    cur.execute(
        "update employee set salary = (salary+(salary/5)) where salary < 10000")
    # cur.execute("commit")

    # Deleting all employees with age greater than 60
    print("Deleting all employees having age greater than 60")
    cur.execute("delete from employee where age > 60")
    cur.execute("commit")

    cur.close()


if __name__ == "__main__":
    main()
