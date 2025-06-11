'''
# 1. Create a dictionary with student names and marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95
}

# 2. Ask user for a student's name
student_name = input("Enter the student's name: ")

# 3. Retrieve and display the corresponding marks
# 4. Handle case where student name is not found
try:
    marks = students[student_name]
    print(f"{student_name}'s marks: {marks}")
except KeyError:
    print(f"Student '{student_name}' not found in the records.")
    '''
    
    # 1. Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# 2. Extract the first five elements
extracted = numbers[:5]

# 3. Reverse the extracted elements
reversed_list = extracted[::-1]

# 4. Print both lists
print("Extracted list:", extracted)
print("Reversed list:", reversed_list)