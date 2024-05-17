# Define a class named 'student'
class student:
    # Define the constructor method to initialize object properties
    def __init__(self, name, major, code_score, project_score, exam_score):
        # Initialize object properties with provided arguments
        self.name = name
        self.major = major
        self.code_score = code_score
        self.project_score = project_score
        self.exam_score = exam_score
    # Define a method to print student information
    def print_information(self):
        # Format student information as a string
        information = f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_score}, Group Project Score: {self.project_score}, Exam Score: {self.exam_score}"
        # Print the formatted information
        print(information)
# Prompt the user to enter student information separated by commas
name, major, code_score, project_score, exam_score = input("Please enter name, major, code score, project score, exam score separated by commas: ").split(',')
# Create a student object with the provided information
person = student(name, major, float(code_score), float(project_score), float(exam_score))
# Call the print_information method to display student information
person.print_information()
