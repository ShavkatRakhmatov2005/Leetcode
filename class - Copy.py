class Animal:
    def __init__(self,animal_type,color,long_age,speed,teeth_sum):
        self.animal_type=animal_type
        self.color=color
        self.long_age=long_age
        self.speed=speed
        self.teeth_sum=teeth_sum
    def get_info(self):
        return f'''
    {self.animal_type}
    {self.color}
    {self.long_age}
    {self.speed}
    {self.teeth_sum}'''
class Dog(Animal):
    def __init__(self, animal_type, color, long_age,speed,teeth_sum):
        super().__init__(animal_type, color, long_age,speed,teeth_sum)

class Cat(Animal):
    def __init__(self, animal_type, color, long_age,speed,teeth_sum):
        super().__init__(animal_type, color, long_age,speed,teeth_sum)
        
class Horse(Animal):
    def __init__(self, animal_type, color, long_age,speed,teeth_sum):
        super().__init__(animal_type, color, long_age,speed,teeth_sum)
        
dog=Dog('Olapar','yellow',15,40,25)
cat=Cat('Tom','white',18,25,29)
horse=Horse('Mustang','black',18,40,32)

animals=[dog,cat,horse]
print(max(animals,key=lambda x:x.speed and x.teeth_sum).get_info())