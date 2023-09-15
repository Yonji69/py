class Student:
    def __init__(self, name):
        self.name = name
        self.marks = [0, 0, 0]  # Initialize marks for three subjects

    def input_marks(self):
        print(f"Enter marks for {self.name}:")
        for i in range(3):
            self.marks[i] = float(input(f"Subject {i + 1}: "))

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        total_marks = self.calculate_total()
        return (total_marks / 300) * 100  # Assuming each subject has a maximum of 100 marks

    def display_scorecard(self):
        total_marks = self.calculate_total()
        percentage = self.calculate_percentage()

        print("\nStudent Scorecard:")
        print(f"Name: {self.name}")
        print(f"Subject 1: {self.marks[0]}")
        print(f"Subject 2: {self.marks[1]}")
        print(f"Subject 3: {self.marks[2]}")
        print(f"Total Marks: {total_marks}")
        print(f"Percentage: {percentage:.2f}%")


# Input student name
student_name = input("Enter student's name: ")

# Create a Student object
student = Student(student_name)

# Input marks for three subjects
student.input_marks()

# Display the scorecard details
student.display_scorecard()