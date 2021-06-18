# WAP
# Store the following information in a dictionary,
# Course code: Course Name, Faculty ,Number of registrations

# perform the following functions:
# a. Find the course Name that has highest number of registrations
# b. Given the course code, display the associated details
# c. Display details of all the courses


def Store_informations(courses):
    print()
    course_code = input("Enter Course Code :: ").upper()
    if course_code not in courses:
        course_name = input("Enter the Course name :: ")
        faculty = input("Enter the Faculty name :: ")
        num_of_registrations = int(
            input("Enter the number of registrations :: "))
        courses[course_code] = {'course_name': course_name,
                                'faculty': faculty, 'num_of_registrations': num_of_registrations}

    else:
        print("No Duplicate records can be created !!")

    print()


def Highest_num_of_registrations(courses):
    print()
    highest_registrations = 0
    course_name = ""
    for course in courses:
        if courses[course]['num_of_registrations'] > highest_registrations:
            highest_registrations = courses[course]['num_of_registrations']
            course_name = course

    print(f"{course_name} has the highest number of registrations of :: ",
          highest_registrations)
    print()


def Details_of(courses, course_code):
    print()
    if course_code in courses:
        print(f"Details of course code {course_code} is ::")
        print("Course Name :: ", courses[course_code]["course_name"])
        print("Course Code :: ", course_code)
        print("Faculty Name :: ", courses[course_code]["faculty"])
        print("Number of registrations :: ",
              courses[course_code]['num_of_registrations'])
    else:
        print("Invalid Course Code!!")

    print()


def Display_all(courses):
    print()
    print("All Course Details ")
    for course_code in courses:
        for parameter in courses[course_code]:
            print(f"{parameter}  :: {courses[course_code][parameter]}")
        print()


def main():
    courses = {}
    ch = 0
    while ch != -1:
        print("Press 1 to Store Information")
        print("Press 2 to Find which course has highest number of registrations")
        print("Press 3 to Find details of a particular course using course code")
        print("Press 4 to Display all the course details")
        print("Press 5 to Exit")
        ch = int(input("Enter Your Choice :: "))

        if ch == 1:
            Store_informations(courses)
        elif ch == 2:
            Highest_num_of_registrations(courses)
        elif ch == 3:
            course_code = input(
                "Enter the course code to find the details :: ").upper()
            Details_of(courses, course_code)
        elif ch == 4:
            Display_all(courses)
        elif ch == 5:
            print("Exiting ... ")
            ch = -1
        else:
            print("Invalid Choice !!!")
            print()


if __name__ == "__main__":
    main()
