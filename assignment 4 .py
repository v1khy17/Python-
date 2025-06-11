try:
    # Open and read the file
    with open('sample.txt', 'r') as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # strip() removes leading/trailing whitespace
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except IOError:
    print("Error: An issue occurred while reading the file.")