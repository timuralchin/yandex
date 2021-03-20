class PearsBasket:

    def __init__(self, pears_count):
        if not isinstance(pears_count, int):
            raise ValueError('Invalid devider type!')  
        elif pears_count < 0:
            raise ValueError('Incorrect devider value. Should be greater than 0') 
        self.pears_count = pears_count
        
    def __floordiv__(self, other):   
        if not isinstance(other, int):
            raise ValueError('Invalid devider type!')  
        elif other <= 0:
            raise ValueError('Incorrect devider value. Should be greater than 0')            
        baskets_array = []
        balance = self.pears_count
        if balance <= other:
            return PearsBasket(balance)
        pear_per_basket = int(balance / other)         
        balance = balance % other
        for i in range(other):
            baskets_array.append(PearsBasket(pear_per_basket)) 
        baskets_array.append(PearsBasket(balance))        
        return baskets_array

    def __mod__(self, other):
        if not isinstance(other, int):
            raise ValueError('Invalid type!')  
        elif other <= 0:
            raise ValueError('Incorrect value. Should be greater than 0')
        return self.pears_count % other

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Invalid type!') 
        return PearsBasket(self.pears_count + other.pears_count)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise ValueError('Invalid devider type!')          
        if self.pears_count < other:
            self.pears_count = 0
        else:
            self.pears_count -= other

    def __str__(self):
        return str(self.pears_count)

    def __repr__(self):
        return f'PearsBasket({self.pears_count})'



pb = PearsBasket(17)
array = pb // 4
print(array)
pb_2 = PearsBasket(13)
pb_3 = pb + pb_2
print(pb_3)
print(pb_3 % 7)
pb - 100
print([pb])