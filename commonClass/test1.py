class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age  = age
        self.sex = sex

    def display(self):
        print "name:%s age:%s sex:%s" % (self.name, self.age, self.sex)

person = Person("xiaoming", 10, "male")
person.display()