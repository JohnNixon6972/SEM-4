# Write a Python program to read from a file input.txt and write the contents
# in reverse order to file output.txt, raise an exception if there is no content
# in input.txt.

def execute():
    try:
        with open("input.txt", "r") as input_file:
            contents = input_file.read()
            with open("output.txt", "w") as output_file:
                reverse_order = contents.split()
                reverse_order = reverse_order[::-1]
                for words in reverse_order:
                    output_file.write(words+" ")

    except FileNotFoundError:
        print("File Not found!!")


def main():
    execute()


if __name__ == "__main__":
    main()
