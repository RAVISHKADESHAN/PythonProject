import statistics

# Student class
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.grades = {}
        self.attendance = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_grade(self, course):
        return self.grades.get(course)

    def take_attendance(self, date, status):
        self.attendance[date] = status

    def view_attendance(self):
        return self.attendance

    def calculate_gpa(self):
        total_credits = 0
        total_points = 0
        for grade in self.grades.values():
            if 'points' in grade and 'credits' in grade:
                total_credits += grade['credits']
                total_points += self.convert_grade_to_points(grade['grade']) * grade['credits']
        if total_credits == 0:
            return 0
        else:
            return total_points / total_credits

    def convert_grade_to_points(self, grade):
        grade_points = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        return grade_points.get(grade.upper(), 0.0)

# Course class   
class Course:

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.schedule = {}

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def enroll_student(self, student):
        self.students.append(student)

    def set_schedule(self, day, time):
        self.schedule[day] = time

    def view_schedule(self):
        return self.schedule
    
    def assign_grade(self, student, grade, credits):
        student.add_grade(self.name, {'grade': grade, 'credits': credits})


# Menu functions
def add_student():
    name = input("Enter student name: ")
    rollno = input("Enter student roll number: ")
    students.append(Student(name, rollno))
    print("Student added successfully.")

def add_course():
    name = input("Enter course name: ")
    teacher = input("Enter teacher name: ")
    courses.append(Course(name, teacher))
    print("Course added successfully.")

def enroll_student():
    if not students:
        print("No students available to enroll.")
        return
    print("Available students:")
    for idx, student in enumerate(students):
        print(f"{idx+1}. {student.name}")
    try:
        student_idx = int(input("Enter student number to enroll: ")) - 1
        if student_idx < 0 or student_idx >= len(students):
            print("Invalid student number.")
            return
    except ValueError:
        print("Invalid input for student number.")
        return

    if not courses:
        print("No courses available to enroll in.")
        return
    print("Available courses:")
    for idx, course in enumerate(courses):
        print(f"{idx+1}. {course.name}")
    try:
        course_idx = int(input("Enter course number to enroll in: ")) - 1
        if course_idx < 0 or course_idx >= len(courses):
            print("Invalid course number.")
            return
    except ValueError:
        print("Invalid input for course number.")
        return

    courses[course_idx].enroll_student(students[student_idx])
    print("Student enrolled in course successfully.")

def add_grade():
    if not students:
        print("No students available to assign grade.")
        return
    print("Available students:")
    for idx, student in enumerate(students):
        print(f"{idx+1}. {student.name}")
    try:
        student_idx = int(input("Enter student number: ")) - 1
        if student_idx < 0 or student_idx >= len(students):
            print("Invalid student number.")
            return
    except ValueError:
        print("Invalid input for student number.")
        return

    if not courses:
        print("No courses available for grade assignment.")
        return
    print("Available courses:")
    for idx, course in enumerate(courses):
        print(f"{idx+1}. {course.name}")
    try:
        course_idx = int(input("Enter course number: ")) - 1
        if course_idx < 0 or course_idx >= len(courses):
            print("Invalid course number.")
            return
    except ValueError:
        print("Invalid input for course number.")
        return

    grade = input("Enter grade: ")
    credits = input("Enter credits: ")
    try:
        credits = float(credits)
    except ValueError:
        print("Invalid input for credits.")
        return

    courses[course_idx].assign_grade(students[student_idx], grade, credits)
    print("Grade added successfully.")

def take_attendance():
    if not students:
        print("No students available to take attendance.")
        return
    print("Available students:")
    for idx, student in enumerate(students):
        print(f"{idx+1}. {student.name}")
    try:
        student_idx = int(input("Enter student number: ")) - 1
        if student_idx < 0 or student_idx >= len(students):
            print("Invalid student number.")
            return
    except ValueError:
        print("Invalid input for student number.")
        return

    date = input("Enter date (YYYY-MM-DD): ")
    status = input("Enter attendance status (Present/Absent): ")
    if status.lower() not in ['present', 'absent']:
        print("Invalid attendance status.")
        return
    students[student_idx].take_attendance(date, status)
    print("Attendance recorded successfully.")

def timely_reporting():
    if not students:
        print("No students available for reporting.")
        return
    print("Reporting students for any rule violation or exam misuse...")
    for student in students:
        gpa = student.calculate_gpa()
        if gpa < 2.0:
            print(f"{student.name} has a low GPA of {gpa}.")
        attendance = student.view_attendance()
        absent_count = list(attendance.values()).count("Absent")
        if absent_count > 5:
            print(f"{student.name} has been absent for {absent_count} days.")

def analyze_student_info():
    if not students:
        print("No students available for analysis.")
        return
    print("Analyzing student information...")
    subject = input("Enter the subject name to analyze: ")
    grades = []
    for student in students:
        grade = student.get_grade(subject)
        if grade and grade['grade'].isdigit():  # Check if grade is numeric
            grades.append(int(grade['grade']))  # Convert grade to integer
        elif grade and grade['grade'].upper() in ['A', 'B', 'C', 'D', 'F']:  # Check if grade is a letter grade
            # Map letter grades to numeric values
            grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
            grades.append(grade_mapping[grade['grade'].upper()])
    if grades:
        mean = statistics.mean(grades)
        median = statistics.median(grades)
        mode = statistics.mode(grades)
        print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
    else:
        print("No numeric grades found for the specified subject.")

# Main driver code
print("Student Information System")

students = []
courses = []

while True:
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. Add Grade")
    print("5. Take Attendance")
    print("6. Timely Reporting")
    print("7. Analyze Student Information")
    print("8. Quit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        add_course()
    elif choice == '3':
        enroll_student()
    elif choice == '4':
        add_grade()
    elif choice == '5':
        take_attendance()
    elif choice == '6':
        timely_reporting()
    elif choice == '7':
        analyze_student_info()
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")

print("Goodbye!")
