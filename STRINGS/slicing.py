str = "abcdef"

print(str[:3])

# slicing in string 
# COLLEGE WALLAH 
name1 = "College Wallah"
print(name1[8:])
print(name1[-6:])

# for converting characters to uppercase 
str1 = "new york"
str2 = str1.upper()
print(str2)

# for converting characters to lowercase 
str3 = str2.lower()
print(str3)

str4 = str3.capitalize()  # only the first character will be capitalized 
print(str4)

# for stripping/ removing any trailing whitespaces 
str1 = "    hello world!      "
print(str1.strip())


# replacing substring 
# str5 = "Hello world, what a beautiful world this is!"
# print(str5.replace("world", "earth", 1))


# split()  function 
# string.split(separator, maxsplit)
string2 = "apple banana mango"
str6 = string2.split(",", 2)  # optional parameters 

print(str6)

