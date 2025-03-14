class complex:
    def __init__(self , real , img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real , "i+" , self.img , "j" )

    def add(self , num2):
        new_real=self.real+num2.real
        new_img=self.img+num2.img
        return complex(new_real , new_img)
    
num1=complex(1 , 3)
num1.shownumber()

num2=complex(3 , 4)
num2.shownumber()

num3=num1.add(num2)
num3.shownumber()