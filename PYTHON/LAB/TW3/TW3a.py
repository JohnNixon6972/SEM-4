# Write a Python program to read the book information from the user and
# store in a CSV file containing rows in the following format:bookNo, title, author, price
# Develop a menu-driven program (with functions for each) with the
# following options:
# 1:Search Book by author
# 2:Search Books below specified price (Raise an exception if price entered is <= 0)
# 3:Search Books where title contains the specified word
# 4:Exit


import csv as csv


def store_books():
    print()
    with open("books.csv", "a", newline="") as file:
        writer = csv.writer(file)

        book_num = int(input("Enter the book number :: "))
        title = input("Enter the title of the book :: ")
        author = input("Enter the name of the author :: ")
        price = int(input("Enter the price of the book :: "))

        details = [book_num, title, author, price]

        writer.writerow(details)
    print()


def search_book_by_author():
    print()
    with open("books.csv", "r", newline="") as file:
        flag = 0
        reader = csv.reader(file)
        author = input("Enter the Name of the author to search the book :: ")

        for rows in reader:
            if rows[2] == author:
                flag = 1
                print("Book Number :: " + rows[0] + "\tBook Title :: " +
                      rows[1] + "\tBook Author :: " + rows[2] + "\tPrice :: " + rows[3])
        if flag == 0:
            print("Books for given author name is not present !!")
    print()


def search_books_by_price():
    print()
    with open("books.csv", "r", newline="") as file:
        flag = 0
        reader = csv.reader(file)
        price = input("Enter the price of the book to be searched :: ")
        if int(price) > 0:
            for rows in reader:
                if rows[3] == price:
                    flag = 1
                    print("Book Number :: " + rows[0] + "\tBook Title :: " +
                          rows[1] + "\tBook Author :: " + rows[2] + "\tPrice :: " + rows[3])
            if flag == 0:
                print("Books for given price value is not present!!")
        else:
            print("Price cannot be <=0 !!")
    print()


def search_books_by_word():
    print()
    with open("books.csv", "r", newline="") as file:
        flag = 0
        reader = csv.reader(file)
        word = input("Enter the key word of title :: ")

        for rows in reader:
            if word in rows[1]:
                flag = 1
                print("Book Number :: " + rows[0] + "\tBook Title :: " +
                      rows[1] + "\tBook Author :: " + rows[2] + "\tPrice :: " + rows[3])
        if flag == 0:
            print("Books for given title key-word is not present")
    print()


def main():
    ch = 0
    while ch != -1:
        print("Press 1 to Store Book Information")
        print("Press 2 to Search book by author")
        print("Press 3 to Search books by a specific price")
        print("Press 4 to search books by a specific key-word in title")
        print("Press 5 to Exit")

        ch = int(input("Enter Your Choice :: "))

        if ch == 1:
            store_books()
        elif ch == 2:
            search_book_by_author()
        elif ch == 3:
            search_books_by_price()
        elif ch == 4:
            search_books_by_word()
        elif ch == 5:
            print("Exiting ... ")
            ch = -1
        else:
            print("Invalid Choice !!!")
            print()


if __name__ == "__main__":
    main()
