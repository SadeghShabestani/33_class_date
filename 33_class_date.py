import termcolor2


class Date:
    def __init__(self):
        self.day1 = int(input("Enter Day: "))
        self.month1 = int(input("Enter Month: "))
        self.year1 = int(input("Enter Year: "))

    def validation(self):
        if 1 > self.year1 > 9999 or 1 > self.month1 > 12 or 1 > self.day1 > 30:
            return f"Validation: {False}"
        else:
            return f"Validation: {True}"

    def show(self):
        print(f"Show: {self.year1} / {self.month1} / {self.day1}")

    def nameMonth(self):
        if self.month1 == 1:
            return f"Name Month: Farvardin"
        elif self.month1 == 2:
            return f"Name Month: Ordibehsht"
        elif self.month1 == 3:
            return f"Name Month: Khordad"
        elif self.month1 == 4:
            return f"Name Month: Tir"
        elif self.month1 == 5:
            return f"Name Month: Mordad"
        elif self.month1 == 6:
            return f"Name Month: Shahrivar"
        elif self.month1 == 7:
            return f"Name Month: Mehr"
        elif self.month1 == 8:
            return f"Name Month: Aban"
        elif self.month1 == 9:
            return f"Name Month: Azar"
        elif self.month1 == 10:
            return f"Name Month: Day"
        elif self.month1 == 11:
            return f"Name Month: Bahman"
        elif self.month1 == 12:
            return f"Name Month: Esfand"

    def show_nameMonth(self):
        print(self.nameMonth())

    def leapYear(self):
        if self.year1 % 4 == 3:
            result = True
        else:
            result = False
        return f"Leap Year: {result}"

    def add(self):
        print(termcolor2.colored("Sum Time2", color="blue"))
        self.day2 = int(input("Enter Day: "))
        self.month2 = int(input("Enter Month: "))
        self.year2 = int(input("Enter Year: "))

        self.year = self.year1 + self.year2
        self.month = self.month1 + self.month2
        self.day = self.day1 + self.day2

        if self.day > 30:
            self.day -= 30
            self.month += 1

        if self.month > 12:
            self.month -= 12
            self.year += 1

        return f"{self.year} / {self.month} / {self.day}"

    def show_add(self):
        print(f"Sum: {self.add()}")

    def sub(self):
        print(termcolor2.colored("Submission Time2", color="blue"))
        self.year = self.year1 - self.year2
        self.month = self.month1 - self.month2
        self.day = self.day1 - self.day2

        if self.day < 1:
            self.month -= 1
            self.day += 30

        if self.month < 1:
            self.year -= 1
            self.day += 12

        return f"{self.year} / {self.month} / {self.day}"

    def show_sub(self):
        print(f"Submission: {self.sub()}")


res = Date()

print(res.validation())

res.show()

res.show_nameMonth()

print(res.leapYear())

res.show_add()

res.show_sub()
