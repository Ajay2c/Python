programming_dictionary = {
    "Bug": "This the type of error while run the application",
    "Address": "The landmark for the asset",
}
# Retrieving item from dictionary.
print(programming_dictionary["Bug"])

# Adding new item to dictionary

programming_dictionary["Loop"] = "This will run contionusly till bwecome false"

print(programming_dictionary)

# Create an Empty Dictionary

empty_dictionary = {}

# #Wipe the Dictionary
#programming_dictionary = {}

# Edit the Dictionary

programming_dictionary["Bug"] = "error occur while run the application"

# loop the Dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Each key does only have one value

# {
    # Key: [list],
    # Key2: {Dict},
# },

# multiple dictionar insde a single list

# [{
#     Key:[list],
#     Key2:{Dict},
# },
# {
#     Key:Value,
#     Key2:Value,
# }]
