from abc import ABC, abstractmethod

class Person(ABC):
    total_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1

    @classmethod
    def total_people_count(cls):
        return f"Total people (students and professors): {cls.total_people}"

    @abstractmethod
    def display_info(self):
        pass


class Student(Person):
    total_students = 0

    def __init__(self, name, age, student_id, address, grades):
        super().__init__(name, age)
        self.student_id = student_id
        self.address = address
        self.__grades = grades
        self.courses = []
        Student.total_students += 1

    def enroll_in_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course}")

    def get_grades(self):
        return self.__grades

    def is_passed(self):
        return "Passed" if self.__grades[0] >= 50 else "Failed"

    def display_info(self):
        course_list = ', '.join(self.courses) if self.courses else "No courses enrolled"
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Address: {self.address}, Courses: {course_list}, Grades: {self.__grades}, Status: {self.is_passed()}"

    @classmethod
    def total_students_count(cls):
        return f"Total students: {cls.total_students}"


class Professor(Person):
    total_professors = 0

    def __init__(self, name, age, professor_id):
        super().__init__(name, age)
        self.professor_id = professor_id
        self.subjects = []
        Professor.total_professors += 1

    def assign_subject(self, subject):
        self.subjects.append(subject)
        print(f"{self.name} has been assigned to teach {subject}")

    def display_info(self):
        subject_list = ', '.join(self.subjects) if self.subjects else "No subjects assigned"
        return f"Name: {self.name}, Age: {self.age}, Professor ID: {self.professor_id}, Subjects: {subject_list}"

    @classmethod
    def total_professors_count(cls):
        return f"Total professors: {cls.total_professors}"


class University:
    def __init__(self):
        self.available_courses = ["Math", "Physics", "Chemistry"]
        self.students = []
        self.professors = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"Student {student.name} has been added to the university.")
        else:
            print("Only Student instances can be added as students.")

    def add_professor(self, professor):
        if isinstance(professor, Professor):
            self.professors.append(professor)
            print(f"Professor {professor.name} has been added to the university.")
        else:
            print("Only Professor instances can be added as professors.")

    def enroll_student_in_course(self, student, course):
        if course in self.available_courses:
            student.enroll_in_course(course)
        else:
            print(f"Error: Course '{course}' is not available. Allowed courses are: {', '.join(self.available_courses)}.")

    def assign_professor_to_course(self, professor, course):
        if course in self.available_courses:
            professor.assign_subject(course)
        else:
            print(f"Error: Course '{course}' is not available. Allowed courses are: {', '.join(self.available_courses)}.")

    def display_all_students(self):
        print("\nAll Students:")
        if self.students:
            for student in self.students:
                print(student.display_info())
        else:
            print("No students enrolled.")

    def display_all_professors(self):
        print("\nAll Professors:")
        if self.professors:
            for professor in self.professors:
                print(professor.display_info())
        else:
            print("No professors assigned.")

    def display_totals(self):
        print(Student.total_students_count())
        print(Professor.total_professors_count())
        print(Person.total_people_count())


# إنشاء الجامعة
uni = University()

# إنشاء الطلاب
student1 = Student("Ali", 20, "S001", "123 Main St", (38, 98))
student2 = Student("Noor", 22, "S002", "456 Oak St", (93, 80))

# إضافة الطلاب إلى الجامعة
uni.add_student(student1)
uni.add_student(student2)

# تسجيل الطلاب في المواد
uni.enroll_student_in_course(student1, "Math")
uni.enroll_student_in_course(student1, "Biology")  # مادة غير مقبولة
uni.enroll_student_in_course(student2, "Physics")

# إنشاء الأساتذة
prof1 = Professor("Dr. Smith", 45, "P001")
prof2 = Professor("Dr. Jones", 50, "P002")

# إضافة الأساتذة إلى الجامعة
uni.add_professor(prof1)
uni.add_professor(prof2)

# تعيين المواد للأساتذة
uni.assign_professor_to_course(prof1, "Math")
uni.assign_professor_to_course(prof2, "Chemistry")
uni.assign_professor_to_course(prof2, "Astronomy")  # مادة غير مقبولة

# عرض جميع الطلاب والأساتذة
uni.display_all_students()
uni.display_all_professors()
uni.display_totals()
