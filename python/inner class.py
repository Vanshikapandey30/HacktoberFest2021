class student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.lap = self.laptop()

    def show(self):
        print("name is:{} age is:{}".format(self.name, self.age))
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'hp'
            self.price = 30000

        def show(self):
            print(self.brand, self.price)

s1 = student('gaurav',19)
s1.show()
