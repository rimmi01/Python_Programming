3####### Escape characters #############
# \' == single quote
# // == backslash
# \n == new line
# \r == carriage return 
# \t == tab 
# \b == backspace 
# \f == form feed 
# \ooo == octal value 
# \xhh == hex value 

print("Tom\'s friend ")
print("Tom\nmarry")


text = "The unexpected always happens"
print(text)
print(len(text))
print(text.find('pp'))
print(text[:11])
print(text.replace('always', 'never'))
text2 = "no matter what"
new_text = text + text2
print(new_text)