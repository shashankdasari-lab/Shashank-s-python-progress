class Car:
    def __init__(self):
        self.acc= False
        self.brk=False
        self.cl=False

    def start(self):
        self.acc= True
        self.cl=True
        print("car started..")


car1=Car()
(car1.start())


