#Object-orientated programming
class Student:

    def __init__(self):
        self.Name = ""
        self.NRIC = ""
        self.FormClass = ""
        self.Subjects = [""]*10

    def getName(self):
        return self.Name

    def setName(self, name):
        self.Name = name

    def getNRIC(self):
        return self.NRIC

    def setNRIC(self, nric):
        self.NRIC = nric

    def getFormClass(self):
        return self.FormClass

    def setFormClass(self, formclass):
        self.FormClass = formclass

    def getSubjects(self):
        return self.Subjects

    def setSubjects(self, subjects): #subjects is a list of strings
        self.Subjects = subjects

    def Display(self):
        line = self.Name+" ("+self.NRIC+") "+"is from "+self.FormClass+" and takes "
        for i in self.Subjects:
            line = line + i + ", "
        print(line)
