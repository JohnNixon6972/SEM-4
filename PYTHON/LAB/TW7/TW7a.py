# Three IA’s are conducted for a class of 10 students for the subject Maths. 
# The name, marks and USN are read from a file in.txt. Find the average of 
# the IA for each student and write the USN and average to a file out.txt. 
# Display the highest average of the class on the console

with open("in.txt", "r") as input_file:
    lines = input_file.readlines()
    # print(lines)
    usns = []
    mks = []
    avgs = []
    for line in lines:
        # print(line)
        name, m1, m2, m3, usn = map(str, line.split())
        # print(name,m1,m2,m3,usn)
        usns.append(usn)
        mks.append([int(m1), int(m2), int(m3)])
        avg = (int(m1)+int(m2)+int(m3))/3
        avgs.append(avg)

    with open("out.txt", "w") as output_file:
        for i in range(len(usns)):
            str = f"USN : {usns[i]}   Avg : {avgs[i]}\n"
            output_file.writelines(str)

    print("Higest Average of the class is :: ", max(avgs))