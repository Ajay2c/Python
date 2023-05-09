# create class with attributes
# The attributes are the things that the object has
# The methods are the things that the object does

class Users:
    def __init__(self):
        ''' the init function, calls the object every time by using class'''
        print("i am triggered")


user_1 = Users() # because of __init__ it calls each and every time
user_1.id = "01"
user_1.name = "Ajay"

user_2 = Users() # because of __init__ it calls each and every time
user_2.id = "02"
user_2.name = "Vijay"

class NewUsers:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username

user_3 = NewUsers(user_id= 10000,username= "Ajay")

print(user_3.id)