class computer:
    def __init__(self,name,age):
        self.have = name
        self.getme= age

    def config(self):
        print("hello we got something here",self.have,self.getme)

    def compare(self, other):
        if self.have == other.have:
            return True
        else:
            return False


x= input("Enter name")
y= int(input("enter age"))
my_comp = computer('we', 45)
youComp = computer(x, y)

my_comp.config()
youComp.config()

if my_comp.compare(youComp):
    print("They are same")
else:
    print("They are different")
