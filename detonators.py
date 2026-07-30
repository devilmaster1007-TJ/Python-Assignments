def welcome_detonator(func):
    def wrapper(*args, **kwargs):
        print("Welcome")
        func(*args,*kwargs)
        print(".")
    return wrapper

def activity_logger(func):
    def wrapper(*args,**kwargs):
        print("Activity Started")
        func(*args,**kwargs)
        print("Activity Finished")
    return wrapper

def make_greeting(msg):
    def greet(student):
        print(f"{msg},{student.name}!")
    return greet

class student:
    def __init__(self,name ,roll_no):
        self.name = name
        self.roll_no = roll_no

    def show_profile(self):
        print(f"name : {self.name}")
        print(f"roll no. : {self.roll_no}")

student.show_profile = welcome_detonator(activity_logger(student.show_profile))

s1 = student("Amit",79)
s2 = student("Aarav",90)

welcome=make_greeting("welcome")
good_afternoon=make_greeting("Good Afternoon")

s1.show_profile()
print()

s2.show_profile()
print()

welcome(s1)
good_afternoon(s2)