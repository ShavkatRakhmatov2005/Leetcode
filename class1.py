class Uy:
    def __init__(self,sum_room,area,price):
        self.sum_room=sum_room
        self.area=area
        self.price=price
    def get_price(self):
        return f"""
    Price: {self.price}$
    """
class Flat(Uy):
    def __init__(self, sum_room, area, price,loaction,condition):
        super().__init__(sum_room, area, price)
        self.location=loaction
        self.condition=condition
        self.get_price() 
class House(Uy):
    def __init__(self, sum_room, area, price,loaction,condition):
        super().__init__(sum_room, area, price)
        self.location=loaction
        self.condition=condition
        self.get_price()
uy=Uy(4,"70kv",100_000)
flat=Flat(5,'45kv',90_000,'center','new')
house=House(7,'65kv',89_000,'out of town','modern')
uylar=[uy,flat,house]
max_price=max(uylar,key=lambda x:x.price)
print(max_price.get_price())