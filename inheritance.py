class SchoolMember():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('I was create')

    def sayInfo(self):
        print('I`m {0} and i`m {1}'.format(self.name,self.age),end=' ')

class Teacher(SchoolMember):

    def __init__(self, name, age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('I`m teacher')

    def sayInfo(self):
        SchoolMember.sayInfo(self)
        print('and i have {0} $ salary'.format(self.salary))



class student(SchoolMember):

    def __init__(self, name, age, mark):
        SchoolMember.__init__(self,name,age)
        self.mark = mark
        print('I`m student')

    def sayInfo(self):
        SchoolMember.sayInfo(self)
        print('My mark is {0}'.format(self.mark))


t = Teacher('Olga',22,459)
s = student('Nike',19,67)
print()

mass = [t,s]

for members in mass:
    members.sayInfo()

    