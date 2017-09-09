from collections import defaultdict

class student(object):
    def __init__(self, lastName, gpa, age):
        self.lastName = lastName
        self.gpa = gpa
        self.age = age

    def __str__(self):
        return "Student: %s" '\n' "GPA: %s" '\n' "Age: %s"  % (self.lastName, self.gpa, self.age)

    def __hash__(self):
        return hash(self.lastName)

    def __lt__(self, other):
        if hasattr(self,"gpa"):
            return self.gpa < other.gpa
        return self.gpa < other

    def __eq__(self, other):
        if hasattr(other, "lastName"):
            return self.lastName == other.lastName
        return self.lastName == other

a = student("Edwards", 4.0, 19)
b = student("Bonds", 1.0, 20)
c = student("Daniels", 2.0, 23)
d = student("Bonds", 4.0, 20)
e = student("Alberts", 2.0, 21)

classroom = [a, b, c, d, e]
studentNames =[student.lastName for student in classroom]
studentGpas = [student.gpa for student in classroom]
studentAges = [student.age for student in classroom]
tmpStudentGPATuple = [(studentNames[x], studentGpas[x]) for x in range (0,5)]
gpaDict = dict(tmpStudentGPATuple)
# gpaDict = {}
# i = 0
# for i in range (0,5):
#     gpaDict.setdefault(studentNames, []).append(studentGpas)
# print(gpaDict)
# print(studentNames)
# print(a)
# print(classroom[4])
# print(a == b)
# print(b == c)
# print(sorted(studentNames))

def lambdaSort(nameValue, gpaValue, ageValue):
    sortedGPADict = {}
    for count, gpaNum in enumerate(gpaValue):
        if gpaNum in sortedGPADict:
            sort = lambda name: sortedGPADict.setdefault(gpaNum, []).append(nameValue[count])
        else:
            sortedGPADict[gpaNum] = 1
    return print(sortedGPADict)

lambdaSort(studentNames, studentGpas, studentAges)
# def sortStudents(nameValue, gpaValue, ageValue):
#     name_dict = {}
#     for name in nameValue:
#         if name in name_dict
#
#     # print(nameValue, gpaValue, ageValue)
#     # i = 0
#     # info = (gpaValue, ageValue)
#     # test = defaultdict(list)
#     # test[nameValue].append(info)
#     # print(test)
#     # test2 = defaultdict(list)
#     # test2 = test2[gpaValue]
#     # print(test2)
#     # test[nameValue].append(test2[gpaValue])
#     tmpStudentGPATuple = [(nameValue[x], gpaValue[x]) for x in range (0,5)]
#     studentGPA =dict(tmpStudentGPATuple)
#     studentAge = {}
#     for i in range len(nameValue):
#     #     studentGPA.setdefault(nameValue, []).append(gpaValue)
#     #     studentAge.setdefault(lastName, []).append(age)
#     print(tmpStudentGPATuple)
#     print(studentGPA)
    # print(test)
    # print(studentAge)

# sortStudents(studentNames, studentGpas, studentAges)

#


# def sortStudents(students):
#     for students
# students ={}
# students["Last Name"] = "Alberts", "Edwards", "Bond", "Daniels", "Bond"
# students["GPA"]= 4.0, 1.0, 2.0, 4.0, 2.0
# students["Age"] = 19, 20, 23, 20, 21
# # print(students.keys())
# # print(students.values())
# # print(students["Alberts"])
# print(students["Last Name"])
# studentsSorted = sorted(students["Last Name"])
# print(studentsSorted)
# print(students)
# def mySort(one, two, three, four, five):
#     lambda

# for key in sorted(students):
#     print(key,students.items())
# for key1, value in sorted(students):
#     print(key1, ':', value)
