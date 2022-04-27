# define distance with ap. members to find sum of 2 distances given in feet, inches
feet1 = int(input("Enter feets "))
inch1 = int(input("Enter inches "))
feet2 = int(input("Enter feets "))
inch2 = int(input("Enter inches "))


class Conversion:
    def sum(self, i1, i2, f1, f2):
        f1 += f2
        i1 += i2
        if i1 > 11:
            f1 += 1

    def printval(self):
        print('f1', 'i1')
