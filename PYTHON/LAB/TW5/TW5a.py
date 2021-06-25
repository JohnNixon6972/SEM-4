# 1. Write a Python program to perform the following:
# a. Create a database named “products.db”
# b. Create a table named “products” that has the following fields:
# prodID: int
# name: text
# quantity: int
# price: real
# c. Insert n records into the table reading the values for each item from the 
# user.
# d. Display the recordset after fetching all the rows.
# e. Delete a product whose product ID is entered by the user.
# f. Increase the price of all products whose current price is less than Rs.50, 
# by 10%.
# g. Display all the products whose quantity is less than 40.

import sqlite3

# Creating a connection to database
conn = sqlite3.connect("products.db")
# Creating a cursor to work on the database
cur = conn.cursor()

# # Creating the required table
# cur.execute("""
#     create table products(
#     proID integer,
#     name text,
#     quantity integer,
#     price real    
# )""")

# Insertion of data into database
n = int(input("Enter total number of data to be inserted into database :: "))
for i in range(n):
    print("Enter the details of product ",i+1)
    pid = int(input("Enter the Product ID :: "))
    name = input("Enter the Product Name :: ")
    quantity = int(input("Enter the Quantity of the Product :: "))
    price = int(input("Enter the Price of the Product :: "))

    cur.execute("insert into products values(:pid,:name,:quantity,:price)",
    {
        'pid':pid,
        'name':name,
        'quantity':quantity,
        'price':price
    })

    # Commit changes
    conn.commit()

# Fetching all data from the products table in database 
data = cur.execute("select * from products")
for rows in data:
    print(rows)

# Delete a product from database by product id given by user
delete_id = input("Enter the Id of product whose data is to be deleted :: ")
cur.execute("delete from products where proid = :pid",{
    'pid':delete_id
})
# Commit changes
conn.commit()

# Increase price of all products whose current price is less than 50 by 10%
cur.execute("update products set price = (price+(price/10)) where price < 50")
# Commit changes
conn.commit()


# Display all the products whose quantity is less than 40
data2 = cur.execute("select * from products where quantity < 40")
for row in data2:
    print(row)

# Commit changes
conn.commit()
# Cloase connection
conn.close()