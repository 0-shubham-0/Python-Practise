class Student:  
    roll_num = 11  
    name = "Joseph"  
  
    def __init__(self):  
        print('Default Constructor',self.roll_num,self.name) 

    def display(self,subj, marks):
        self.subj = subj
        self.marks = marks
        print('Parameterized Constructor',self.subj,self.marks)
    # def show(self):
        # print("student marks",self.marks) 

# Student = student("25")
# Student.show()

    
  
st = Student()  
# st.display() 
st.display('Maths',98)
# Student.show()

 