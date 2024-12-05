class accountholder:

    def __init__(self):
        self.bal=10000

ah =accountholder()
print(ah.bal)
ah.bal=-20000
print(ah.bal)









def add():
    a,b=10,20
    c=a+b
    return c
a=add()
print(a)











class AccountHolder:

    def __init__(self):
      self._bal=10000

    def get_bal(self):
        return self._bal

    def set_bal(self,amt):
        if amt>0:
           self._bal=amt
        else:
            print('invalid amount')

ah=AccountHolder()
print(ah.get_bal())
ah.set_bal(-20000)
print(ah.get_bal())
print(ah._bal)
ah._bal=-20000
print(ah._bal)
        
