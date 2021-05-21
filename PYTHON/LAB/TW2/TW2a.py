# Develop a menu driven program to implement the mapping:
# {USN:[m1,m2,m3]...} and perform the following using function:
# a.Add an Entry
# b.Delete An Entry
# c.Displa y all entries
# d.Compute and display average of best two marks of a specific USN

def Add_entry(students):
    print()
    usn = input(f"Enter the USN of student ::").upper()
    if usn not in students:
        m1 = int(input("Enter marks of sub 1 :: "))
        m2 = int(input("Enter marks of sub 2 :: "))
        m3 = int(input("Enter marks of sub 3 :: "))
        students[usn] = [m1, m2, m3]
        print("Successfully Added the Entry")

    else:
        print("No Duplicate Entries can be Added!!")

    print()


def Delete_entry(usn, students):
    print()
    if usn in students:
        del students[usn]
        print("Deleted data of USN :: ", usn)
    else:
        print("Invalid USN!!!")

    print()


def Compute_average_of_best_2(usn, students):
    print()
    if usn in students:
        marks = students[usn]
        marks.sort()

        avg = (marks[-1]+marks[-2])/2
        print(f"Average of Best of two marks for USN {usn} is :: ", avg)

    else:
        print("Invalid USN!!!")

    print()


def Display_All_entries(students):
    print()
    print("Entries :: ")
    for student in students:
        print(student, " marks :: ", students[student])

    print()


def main():
    students = {}
    ch = 0
    while ch != -1:
        print("Press 1 to Add an Entry")
        print("Press 2 to Delete an Entry")
        print("Press 3 to compute average of best of 2 marks for a given USN")
        print("Press 4 to Display all Entries")
        print("Press 5 to Exit")
        ch = int(input("Enter Your Choice :: "))

        if ch == 1:
            Add_entry(students)
        elif ch == 2:
            usn = input(
                "Enter the USN of the student whose entry is to be deleted :: ").upper()
            Delete_entry(usn, students)
        elif ch == 3:
            usn = input(
                "Enter the USN of the student whose best of 2 average is to be computed :: ").upper()
            Compute_average_of_best_2(usn, students)
        elif ch == 4:
            Display_All_entries(students)
        elif ch == 5:
            print("Exiting ... ")
            ch = -1
        else:
            print("Invalid Choice !!!")
            print()


if __name__ == "__main__":
    main()
