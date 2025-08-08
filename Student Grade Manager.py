class GradeManager:
    def __init__(self):
        # Phase 1: What data structure do you need?
        self.student = {}

    def add_grade(self, student_name, subject, subject_grade):
        if student_name not in self.student:
            self.student[student_name] = {}     #Create an outer key

        self.student[student_name][subject] = subject_grade     #Adding subject grade to the subject
        # print(self.student)
        # print(f"{subject_grade} has been added for {subject} for student {student_name}")

    #GET STUDENT INFO
    def get_student_info(self, student_name):
        student_info = {}
        for student, subject_dict in self.student.items():
            if student_name in student:
                student_info[student_name] = subject_dict
        print(f"Here is the info for '{student_name}': {student_info}")
        print("=" * 160)
        return student_info

    #Calculate gpa
    def calculate_gpa(self, student_name):
        if student_name not in self.student:
            return None

        grades = self.student[student_name]
        if not grades:
            return None

        gpa_points = []
        for subject, student_grade in grades.items():
            if 90<=student_grade<=100:
                gpa_point = 4
            elif 80<=student_grade<90:
                gpa_point = 3
            elif 70<=student_grade<80:
                gpa_point = 2
            elif 60<=student_grade<70:
                gpa_point = 1
            else:
                gpa_point = 0

            gpa_points.append(gpa_point)

        print(gpa_points)
        #CALCULATE GPA POINTS
        average_gpa_point = sum(gpa_points) / len(gpa_points)
        return round(average_gpa_point, 2)


    def find_top_students(self):

        subjects = set()

        for student_name, subject_dict in self.student.items():
            for subject in subject_dict.keys():
                subjects.add(subject)

        top_student = {}

        for subject in subjects:
            best_student = None
            highest_score = -1
            for student_name, subject_dict in self.student.items():
                if subject in subject_dict:
                    if subject_dict[subject] > highest_score:
                        highest_score = subject_dict[subject]
                        best_student = student_name
            top_student[subject] = (best_student, highest_score)


        print(f"The students with the highest score for each subject are: {top_student}")
        print("=" * 160)

        return subjects, top_student


    def calculate_class_averages(self):
        subjects = set()

        for student_name, subject_dict in self.student.items():
            for subject in subject_dict.keys():
                subjects.add(subject)
        # print(subjects)

        subject_grades = {}
        for subject in subjects:
            grades = []
            for student_name, subject_dict in self.student.items():
                if subject in subject_dict:
                    grades.append(subject_dict[subject])

            subject_grades[subject] = round((sum(grades) / len(grades)),2)

        all_grades = []
        for student_name, subject_dict in self.student.items():
            for grade in subject_dict.values():
                all_grades.append(grade)

        class_average = sum(all_grades) / len(all_grades)


        print(f"The average score for each of the subject is: {subject_grades}")
        print("=" * 160)
        # print(all_grades)
        print(f"Class average grade is: {class_average}")

        return subject_grades, class_average



    # def calculate_gpa(self):


grade = GradeManager()

grade1 = grade.add_grade("Alice", "Math", 90)
grade2 = grade.add_grade("Alice", "Biology", 86)
grade3 = grade.add_grade("Alice", "History", 93)
grade4 = grade.add_grade("Alice", "English", 83)
grade5 = grade.add_grade("Max", "Math", 79)
grade6 = grade.add_grade("Max", "Biology", 93)
grade7 = grade.add_grade("Max", "History", 90)
grade8 = grade.add_grade("Max", "English", 92)

student1 = grade.get_student_info("Alice")

# alice_gpa = grade.calculate_gpa("Alice")
# max_gpa = grade.calculate_gpa("Max")
# print(alice_gpa)
# print(max_gpa)

top_student = grade.find_top_students()
class_avaerage = grade.calculate_class_averages()
