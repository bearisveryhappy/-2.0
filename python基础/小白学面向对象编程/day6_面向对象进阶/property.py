
#
# class Student(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     @property
#     def fly(self):
#         print(self.name,"is flying...")
#
#
#
# s = Student("Jack")
# s.fly






class Flight(object):
    def __init__(self,name):
        self.flight_name = name

    def checking_status(self):
        print("connecting airline company/airport api...... " )
        print("checking flight %s status " % self.flight_name)
        return 1  #1 arrived , 2 departured , 3 cancel

    @property
    def flight_status(self): # get
        status = self.checking_status()
        if status == 0 :
            print("flight got canceled...")
        elif status == 1 :
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter
    def flight_status(self,status):
        print("changing....flight status..",status)
        self.status = status


    @flight_status.deleter
    def flight_status(self):
        print("del .....")

f = Flight("CA980")

f.flight_status
f.flight_status = 0
print(f.flight_status)

del f.flight_status
