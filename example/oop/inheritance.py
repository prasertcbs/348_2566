# %%
import re


# %%
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname.strip().title()
        self.lastname = lastname.strip().title()

    @property
    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __str__(self):
        return "firstname: {}, lastname: {}".format(self.firstname, self.lastname)


# %%
class Student(Person):
    def __init__(self, firstname, lastname, studentid, school, major):
        super().__init__(firstname, lastname)
        self.studentid = studentid
        self.school = school
        self.major = major

    @staticmethod
    def remove_non_digit(s):
        return re.sub(r"[\D]", "", s)

    def pretty_student_id(self):
        s = self.remove_non_digit(self.studentid)
        return re.sub(r"(\d{3})(\d{5})(\d{2})", r"\1 \2 \3", s)

    @property
    def email(self):
        return "{}.{}{}@cbs.chula.ac.th".format(self.firstname,
                                                self.lastname[:2],
                                                self.studentid[:2])

    def __str__(self):
        return "student ID: {}, {}".format(self.pretty_student_id(), super().__str__())


# %%
class ExchangeStudent(Student):
    def __init__(self, firstname, lastname, studentid, school, major, partner_univ):
        super().__init__(firstname, lastname, studentid, school, major)
        self.partner_univ = partner_univ
        self.studentid = self.remove_non_digit(studentid)


# %%
class Teacher(Person):
    def __init__(self, lastname, firstname, office, subjects: list):
        super().__init__(firstname, lastname)
        self.office = office
        self.subjects = subjects


# %%
if __name__ == '__main__':
    s = Student("Peter", "Parker", "5941234526", "CBS", "MIS")
    print(s)
    print(s.email)
    print(issubclass(Student, Person))
    print(isinstance(s, Student))
    print(isinstance(s, Person))
