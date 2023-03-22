class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduce(self) :
         print(f'제 이름은 {self.name}, 나이는 {self.age}, 키는 {self.height}입니다.')
    
    def yell(self) : 
         print("아?")
    
class Developer(Person):
    keyboard = "기계식"
    
    def yell(self) : 
        print("어?")

class Designer(Person):
    def __init__(self, name, age, height, desease):
        super().__init__(name, age, height)
        self.desease = desease

class Productdevelopment(Person):
    def aging(self) : 
        self.age = self.age + 2
        self.height = self.height - 5
        print('개발자 새롭게 뽑아버릴까??... u r fired')
        Developer.keyboard = "멤브레인"
       
    def yell(self) : print("개발자야... 오류 발견했다.. 고치자")
        
    

d1 = Developer("일론 머스크", 40, 170)
d2 = Designer("스티븐 잡스", 56, 190, "싸이코패스")
p1 = Productdevelopment("최성호", 24, 178)

d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
print(Developer.keyboard)
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()
print(d2.desease) 
print(Developer.keyboard)

    
        

