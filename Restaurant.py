class Restaurant:
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.num_servered=0
    
    def describe(self):
        print(f"This is a {self.cuisine_type} restaurant, namely {self.name}") 
    
    def open(self):
        print(f"{self.name} is now opened")

    def set_num_served(self,num_served):
        self.num_servered = num_served
    def increment_num_served_one_day(self):
        self.num_servered+=100