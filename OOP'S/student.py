
# teacher ias a super class and student is a derived class
# syntax  --   class subclass(superclass):
#                     subclass  body


from teacher import *
class student(teacher):

    def setmarks(self, marks):
        self.marks = marks
    def getmarks(self):
        return self.marks

    def setGF(self,GF):
        self.GF = GF
    def getGF(self):
        return self.GF

