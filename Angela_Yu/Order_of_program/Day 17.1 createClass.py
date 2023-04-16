# CLASS type 1
class User:
    pass


user_1 = User()  # this class will not trigger
user_1.id = "001"
user_1.name = "type 1: Vicky"
print(user_1.name)

user_2 = User()
user_2.id = "002"
user_2.name = "type 1: Vijay"


# CLASS type 2
class User:
    def __init__(self):
        print("type 2: new user begin created......")


user_1 = User()  # this class will trigger because of init function
user_1.id = "001"
user_1.name = "type 2: Vicky"
print(user_1.name)

user_2 = User()
user_2.id = "002"
user_2.name = "type 2: Vijay"


# CLASS type 3
class Users:
    def __init__(self, user_id, username):  # Parameter
        self.id = user_id
        self.name = username


user_1 = Users("001", "ajay")  # Argument for init
user_2 = Users("002", "Akash")  # Argument for init

print(user_1, user_2)


# Adding Method to class
class Users:
    def __init__(self, user_id, username):  # Parameter
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = Users("001", "ajay")  # Argument for init
user_2 = Users("002", "Akash")  # Argument for init

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
