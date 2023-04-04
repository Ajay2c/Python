# Global Scope
# In this method we are going to see two types how to modify the global scope

#1) using "global" to modify the changes
apple = 5

def usetheapple():
    global apple # here it is
    apple -= 2
    return print(apple)
usetheapple()
#output: 3


#2) using return function to modify the changes

orange = 6

def useOrange(new_orange):
    updated_orange =new_orange + orange # 6 + 6 = 12
    updated_orange += 5 # 12 + 5 = 17
    return updated_orange

theOrange = useOrange(orange)
print(theOrange)


# we should not use the global variable to modify the changes, it will cause bugs