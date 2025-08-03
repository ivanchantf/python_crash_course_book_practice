#Importing class
# import pizza as p
# p.makepizza()

# from pizza import make_pizza as mp
# make_pizza()


import hello as h #--1
from hello import hello #--2

from Restaurant import Restaurant
from User  import User,Admin
from IceCreamStand import IceCreamStand

h.hello() #--1
hello() #--2
print('---------')
#Class [OOP]
my_restaurant = Restaurant('Cafe Ce coral','Fast Food')
print (my_restaurant.name)
print(my_restaurant.cuisine_type)
my_restaurant.open()
my_restaurant.describe()

print('---------')

my_restaurant = Restaurant('Tao Heung','Chinese Restaurant')
print (my_restaurant.name)
print(my_restaurant.cuisine_type)
my_restaurant.open()
my_restaurant.describe()

print('---------')

userA= User('Tsz Fujng','Chan',24,'M','Skating')
userA.describe_user()
userA.greet_user()

print('---------')
print(my_restaurant.num_servered)
my_restaurant.num_servered=313 #direct set
print(my_restaurant.num_servered)
my_restaurant.set_num_served(203)#setter
print(my_restaurant.num_servered)
my_restaurant.increment_num_served_one_day()#increment after one day
print(my_restaurant.num_servered)

print('---------')

print(userA.login_attempts)
userA.increment_login_attempts()
print(userA.login_attempts)
userA.increment_login_attempts()
print(userA.login_attempts)
userA.increment_login_attempts()
print(userA.login_attempts)
userA.reset_attempts()
print(userA.login_attempts)


print('---------')
'''Inheritance'''

my_restaurant_ice_cream = IceCreamStand('ABC Icecream','Dessert')
my_restaurant_ice_cream.open()
my_restaurant_ice_cream.describe()
my_restaurant_ice_cream.print_flavours()
print('---------')
adminUser= Admin('Ming','Chan',12,'M','cycling')
adminUser.describe_user()
adminUser.print_priv()

print('---------')
adminUser= Admin('Hui','Chan',12,'M','cycling')
adminUser.describe_user()
adminUser.print_priv()
print('---------')


print('\n\t--Reading File all at once read() ')
with open('learning_python.txt') as file_object:
    content= file_object.read()
    print(content)

print("\n\n\n-------------------FILES HANDLING-------------------\n\n\n")

print('\n\t--Reading File looping file obj')
content=''
with open('learning_python.txt') as file_object:
    for i in file_object:
        content += i
    print(content)

print('\n\t--Reading File storing lines as list & work outside the block')
with open('learning_python.txt') as file_object:
    content_li = file_object.readlines()

for line in content_li:
    print(line.rstrip())

print('\n\t Modifying content')
with open('learning_python.txt') as file_object:
    content= file_object.read()

print(content.replace('python','C++'))


# print('\n\n Writing to Files')
# for i in range(3):
#     name = input("What is the name of the guest? ")

#     with open('guests.txt','a') as file_obj: #'w' will rewrite whole file 
#         file_obj.write(f'{name}\n')

# inStr=''
# while inStr!= 'q':
#     inStr= input('why u like programming')
#     with open ('reasons_like_programming.txt','a') as file_obj:
#         file_obj.write(f"{inStr}\n")



