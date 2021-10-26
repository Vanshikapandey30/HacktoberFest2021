class student:

    school = "MAISM"

    def __init__(self, m1, m2, m3):
        self.maths = m1
        self.science = m2
        self.computer = m3

    def getAvg(self): #They are simple instance methods
        return (self.maths+self.science+self.computer)/3

    @classmethod   #This is a decorator
    def schoolName(cls): #because this is class method
       return cls.school

    ''' NOw we are going to discuss about static methods In this we should also use decorators'''

    @staticmethod
    def info():         #should be without argument
        print("This is a static method")    #It does nothing but it has nothing To do with class and instance methods



s1 = student(12, 45, 67)
s2 = student(22, 44, 97)
print(s1.getAvg())
print(s2.getAvg())
print(student.schoolName())


#To call this method we use

student.info()      #But this will not work until we have to use a decorator before that method

