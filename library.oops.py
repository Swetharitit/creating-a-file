class footballer:
    def __init__(self):
        self.name="ronaldo"
        self.team="portugal"
        self.goals="100000"
        print(self.name,self.team,self.goals)
    def shooting(self):
       print("ronaldo is shooting")
    def passing(self):
        print("ronaldo is passing")
    def running(self):
            print("ronaldo is running")
c1=footballer()
c1.shooting()
c1.passing()
c1.running()





class demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a)
        print(self.b)
d1=demo(1000,2000)
d2=demo(2000,3000)



cr=footballer("cristiano","juventu",746)
print(cr.name)
print(cr.team)
print(cr.goals)
cr.shooting()
cr.passing()
cr.running()

messi=footballer("messi","baracelona",700)
print(messi.name)
print(messi.team)
print(messi.goals)
messi.shooting()
messi.passing()
messi.running()
            
        
