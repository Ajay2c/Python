# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# name = "e"
# print(alphabet.index(name))
# print(alphabet[5])

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1
 
 
# Driver code
s = ['Geeks', 'for', 'Geeks']
print(listToString(s))


shift = 10
if shift > 26:
    new_shift = shift % 26
print(new_shift)
