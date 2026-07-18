#1) upper - uppercase
#2) lower - lowercase
#3) rstrip - remove
#4) replace - replace
#5) capitalize - make the first letter uppercase and rest all lowercase
#6) center - center aligns the text as per the parameter given by the user
#7) count - counts the no of times a particular character has appeared in a string
#8) endswith - checks whether a certain string ends in a particular character
#9) find - searches for the 1st occurence of a particular character in a string
#10) index - also searches for the 1st occurence of a particular character in a string
#the difference between find and index is that find return -1 value if a particular
#character is not present in the string but the index function simply gives an 
#error if that particular character is not present in the string 
#11) isalnum - returns true if the string is made up of only alphabets an numbers
#12) isalpha - returns true is the string is made up only of alphabets
#13) islower - returns true if all the characters of the string are lowercase
#14) isprintable - returns true if all the character of a string are printable
#15) isspace - returns true is the string contains white space
#16) istitle - returns true if the first letter of each word of the string is captital
#17) isupper - returns true if all the characters of the string are uppercase
#18) startswith - checks if a string starts with a particular value
#19) swapcase - swaps lowercase with uppercase and uppercase with lowercase
#20) title - capitalizes first letter of each word within the string





x = "Anish"
y = "haRrY"
z = "banana"
str1 = "ronaldo7"
str2 = "       "
str3 = "World health organisation"
str4 = "HELLO"
str5 = "his name is Dan. dan is a good guy"
print (x.lower())
print (x.upper())
print (x.rstrip("h"))
print (x.replace("Anish", "John"))
print (y.capitalize()) 
print (x.center(50))
print (z.count("a"))
print (x.endswith("h"))
print (x.find("i"))
print (x.index("s"))
print (z.isalnum())
print (str1.isalpha())
print (z.islower())
print (z.isprintable())
print (str2.isspace())
print (str3.istitle())
print (str4.isupper())
print (str3.startswith("World"))
print (y.swapcase())
print (str5.title())
