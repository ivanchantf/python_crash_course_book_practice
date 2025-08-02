class User:
    def __init__(self,fname,lname,age,sex,hobbies):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.sex=sex
        self.hobbies=hobbies
        self.login_attempts=0
    
    def describe_user(self):
        print('///////////////')
        print(f"This is a user :")
        print(f" Name : {self.lname} {self.fname}")
        
        print(f" Age : {self.age}")
        print(f" Sex : {self.sex}")
        print(f" Hobbies : {self.hobbies}")
        print('////////////////')

    def greet_user(self):
        print(f"Hello! {self.fname} {self.lname}")

    def reset_attempts(self):
        self.login_attempts=0
    def increment_login_attempts(self):
        self.login_attempts+=1

class Admin(User):
    def __init__(self,fname,lname,age,sex,hobbies):
        super().__init__(fname,lname,age,sex,hobbies)
        self.priv=Priv()
    def print_priv(self):
        self.priv.print_priv_from_PrivClass()
        
class Priv :
    def __init__(self,li_priv = ['add post','ban user']):
        self.li_priv=li_priv

    def print_priv_from_PrivClass(self):
        print(self.li_priv)