def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 60)
        print("DYNAMIC REPORT GENERATOR".center(60))
        print("=" * 60)

        # Call the original function
        func(*args, **kwargs)

        print("=" * 60)
        print("END OF REPORT".center(60))
        print("=" * 60)

    return wrapper

class report:
   company_name = "ABC Technologies Pvt. Ltd."

   def __init__(self, title, author):
        self.title = title
        self.author = author
        self.contents = []

   def add_content(self, text):
        self.contents.append(text)

   @classmethod
   def change_company(cls, new_company):
        cls.company_name = new_company

   @staticmethod
   def line():
        print("-" * 60)

   def __str__(self):
        return f"Report Title : {self.title}\nAuthor : {self.author}"

   def __len__(self):
        return len(self.contents)

   @report_decorator
   def display_report(self):

        print("Company :", report.company_name)
        print(self)

        report.line()

        print("Report Contents:")

        for i, item in enumerate(self.contents, start=1):
            print(f"{i}. {item}")

        report.line()

        print("Total Sections :", len(self))

r1 = report("Advanced Python Practical Report", "Tejas Joshi")

r1.add_content("Completed Practical No. 2 successfully.")
r1.add_content("Implemented Decorators, Class Methods, Static Methods and Magic Methods.")
r1.add_content("Learned Object-Oriented Programming concepts.")
r1.add_content("Report prepared by Tejas Joshi.")

r1.display_report()

print("\nChanging Company Name...\n")
report.change_company("XYZ Solutions Pvt. Ltd.")

r2 = report("Employee Performance Report", "Tejas Joshi")

r2.add_content("Attendance : 89%")
r2.add_content("Projects Completed : 7")
r2.add_content("Rating : Excellent")
r2.add_content("Department : Computer Engineering")
r2.add_content("Recommendation : Promotion Approved")

r2.display_report()

r3 = report("Student Result Report", "Tejas Joshi")

r3.add_content("Student Name : Ramesh")
r3.add_content("Roll No : 1001")
r3.add_content("CGPA : 9.5")
r3.add_content("Status : Pass with Distinction")
r3.add_content("Result : Pass")

r3.display_report()