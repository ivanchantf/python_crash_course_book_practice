import Restaurant
class IceCreamStand(Restaurant.Restaurant):
    def __init__(self,name,cuisine_type):
        super().__init__(name,cuisine_type)
        self.ice_cream_flavours = 'orange'

    def print_flavours(self):
        print(self.ice_cream_flavours)