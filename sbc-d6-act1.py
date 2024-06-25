string = []
lol = input("TYPES the word: ")
palindrome = "".join(reversed(lol.replace(" ","").lower()))

d = lol.replace(" ","").lower() 
string.append(d)

for i in string:
    if i == palindrome:
       print( lol, "Is a Palindrome" )
    else:
       print(f"'{lol}', {palindrome} Is not a palindrome",)