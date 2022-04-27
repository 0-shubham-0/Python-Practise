class Student1:
    roll_num = None
    name = "No-Name"

    def __init__(self):
        print(f'''Default Constructor:
        Name : {self.name}
        Roll no. : {self.roll_num}''')


class Student2:
    name = ''
    roll_num = ''

    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num
        print(f'''Parameterised Constructor:
        Name : {self.name}
        Roll no. : {self.roll_num}''')


st1 = Student1()
st2 = Student2("Shbham", 58)
