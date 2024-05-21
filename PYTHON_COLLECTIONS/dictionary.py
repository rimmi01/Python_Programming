# Values are stored in pairs in a dictionary 
# key value pairs are stored in this dictionary in python 

phone_numbers = {
    "John" : 8826970,
    "Ria" : 888343,
    "Joy" : 987654
}
print(phone_numbers)
print(type(phone_numbers))
print(len(phone_numbers))

phone_numbers["John"] = 3435234
print(phone_numbers)

phone_numbers["kia"] = 234235234
print(phone_numbers)

moreOptions = {
    
}

# phone_numbers.clear()  # it will empty up the dictionary 
# print(phone_numbers)


# printing values of a dictionary 
for x in phone_numbers:
    print(phone_numbers[x])


# nested dictionaries 
phone_numbers = {
    "Area1" : {
        "x" : 0,
        "y" : 1,
        "z" : 2
    },
    "Area2" : {
        "a" : 3,
        "b" : 4,
        "c" : 5
    }
}
print(phone_numbers["Area1"]["y"])
print(phone_numbers["Area2"]["c"])
