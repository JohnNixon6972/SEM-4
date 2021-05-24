#WAP TO SIMULATE QUEUE OPERATIONS 
#1>ADDING
#2>DELETING
#3>DISPLAYING QUEUE

def add(queue,data):
    queue.append(data)
    print("Added data Successfully")

def delete(queue):
    return queue.pop(0)

def display(queue):
    print("---------------------------------------")
    print("Queue is :: ")
    for data in queue:
        print(data)
    
def main():
    queue = []
    while True:
        print("Press 1 to Insert into queue ")
        print("Press 2 to Delete from queue ")
        print("Press 3 to Display queue ")
        print("Press 4 to Exit ")

        ch = int(input("Enter Your Choice :: "))

        if ch == 1:
            add(queue,input("Enter the data to be added in queue :: "))
        elif ch == 2:  
            print("Removed Element is :: ",delete(queue)) 
        elif ch == 3:
            display(queue)
        elif ch == 4:
            print("Exiting !!!")
            break
        else:
            print("Invalid choice !!!")

        print("-------------------------------------------")

if __name__ == "__main__":
    main()

