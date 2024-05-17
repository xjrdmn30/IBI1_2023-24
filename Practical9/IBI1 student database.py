class student :

    def __init__(self, name, major, code_score, project_score, exam_score) :
        self.name = name
        self.major = major
        self.code_score = code_score
        self.project_score = project_score
        self.exam_score = exam_score

    def print_information(self) :
        information = f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_score}, Group Project Score: {self.project_score}, Exam Score: {self.exam_score}"
        print(information)

name, major, code_score, project_score, exam_score = input("Please enter name, major, code score, project score, exam score separated by commas: ").split(',')
person = student(name, major, float(code_score), float(project_score), float(exam_score))

person.print_information()


        
