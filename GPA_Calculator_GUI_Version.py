import tkinter as tk

print("Welcome to the GPA calculator.")
print("Please enter all your letter grades, one per line.")
print("Enter a blank line to designate the end.")


class GPACalc:
    def __init__(self):
        self.n = 0
        self.p = 0
        # map from letter grade to point value
        self.points = {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67,
                       "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33, "D": 1.0, "F": 0.0}
        self.calc = 0
        self.done = False

    def print_result(self):
        self.result = grade.get()
        if str(self.result) == '':  # empty line was entered
            self.done = True
        elif str(self.result).upper() not in self.points:  # unrecognized grade entered
            lb2.config(text="Unknown grade {0} being ignored".format(self.result), bg="red")
            self.done = True
        else:
            self.n += 1
            self.p += self.points[str(self.result).upper()]
        if self.n > 0:  # avoid division by zero
            self.calc = self.p / self.n
            print(self.calc)
            lb2.config(text=str(self.calc), bg="yellow")
            lb3.config(text="Courses taken {0}".format(str(self.n)), bg="green", fg="white", width=20, height=1)
            lb3.place(x=290, y=90)


calc1 = GPACalc()
window1 = tk.Tk()
window1.minsize(width=500, height=220)
grade = tk.StringVar()  # read line from user
txtbx1 = tk.Entry(window1, textvariable=grade)
txtbx1.place(x=20, y=90)
lb1 = tk.Label(window1, text="Please, enter your letter grade in a given course:", width=40, height=3)
lb1.place(x=10, y=1)
lb2 = tk.Label(window1, text="Your GPA will show up here after you click Calculate!", width=44, height=1)
lb2.place(x=50, y=160)
lb3 = tk.Label(window1, text="Number of taken courses \n will be displayed here", width=44, height=2)
lb3.place(x=209, y=82)
bt1 = tk.Button(window1, text="Calculate!", command=calc1.print_result)
bt1.place(x=190, y=85)
window1.mainloop()
