
'''
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
    '''
    
    
    # 1. Take user input
user_input = input("Enter some text to write to the file: ")

# 2. Write user input to output.txt and append additional data
try:
    with open('output.txt', 'w') as file:
        file.write(user_input + '\n')  # Write user input
        file.write("This is additional appended data.\n")  # Append additional data
    print("Data written to output.txt successfully.")
except Exception as e:
    print(f"Error writing to file: {e}")

# 3. Read and display the content of output.txt
try:
    with open('output.txt', 'r') as file:
        content = file.read()
        print("\nContent of output.txt:")
        print(content)
except Exception as e:
    print(f"Error reading file: {e}")