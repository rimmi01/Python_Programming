# Write a Python function that checks if the given string is a palindrome or not 
# input = mama 
# output = True 

# string = "mam"
# # reverse_string = ''.join(reversed(string))
# reverse_string = string[::-1]  # reversing by giving no. of steps 
# if string == reverse_string:
#     print("The string is a palindrome.")
# else:
#     print("The given string is not a palindrome.")


#######using function##########

def check_palindrome(str):
    clean_str = (str.replace(" ", "").lower())

    reverse_str = clean_str[::-1]
    return clean_str == reverse_str

str = input("Enter a string: ")
if check_palindrome(str):
    print("It is a palindrome string.")
else:
    print("Not a palindrom.")

