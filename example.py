from main import Person, Director, Teacher, Student

dr1 = Director('Van', 'De bak', 22, 23232)
dr2 = Director('Jon', ' ' 'Wik', 29, 98172)

print(dr1.get_area())
tr1 = Teacher('Alim', ' ' 'Last', 22, 14232)
tr2 = Teacher('Jony', ' ' 'Keane', 29, 15233)
# print(tr1.get_area())
st1 = Student('Hanna', ' ' 'Biska', 18, 14236)
st2 = Student('Alan', ' ' 'Dzagoev', 19, 14522)

pers = [dr1, dr2, tr1, tr2, st1, st2]
for person in pers:
    # print(person.get_area())
    pass
