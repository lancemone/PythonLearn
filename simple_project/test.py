class Children:
    age = 10

    def activitie(self):
        print('玩具')


class Student:
    grade = 3

    def activitie(self):
        print('作业')


class Pupil(Student, Children):
    def __init__(self):
        print('我今年%s岁，已经上%s年级了' % (self.age, self.grade))


p = Pupil()
p.activitie()
