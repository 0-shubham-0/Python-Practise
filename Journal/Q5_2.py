class Dist:
    def __init__(self):
        self.feet = None
        self.feet_1 = None
        self.feet_2 = None
        self.inch = None
        self.inch_1 = None
        self.inch_2 = None

    def distance1(self, feet_1, inch_1):
        self.feet_1 = feet_1
        self.inch_1 = inch_1

    def distance2(self, feet_2, inch_2):
        self.feet_2 = feet_2
        self.inch_2 = inch_2

    def sum(self):
        self.feet = self.feet_1 + self.feet_2
        self.inch = self.inch_1 + self.inch_2
        if self.inch > 11:
            self.feet = self.feet + 1
            self.inch = self.inch - 12
        print(f"Sum is: Feet = {self.feet}, Inch = {self.inch}")


print('Input Distance 1')
feet_1 = int(input("Feet : "))
inch_1 = int(input("Inch : "))
print('Input Distance 2')
feet_2 = int(input("Feet : "))
inch_2 = int(input("Inch : "))

dist_cal = Dist()
dist_cal.distance1(feet_1, inch_1)
dist_cal.distance2(feet_2, inch_2)
dist_cal.sum()
