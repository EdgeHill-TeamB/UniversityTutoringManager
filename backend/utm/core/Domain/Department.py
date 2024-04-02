class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.staff = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

    def add_staff(self, staff):
        self.staff.append(staff)

    def get_staff(self):
        return self.staff
