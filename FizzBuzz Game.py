# For a number divisible by 3, the program will print 'Fizz'
# For a number divisible by 7, the program will print 'Buzz'
# For a number divisible by 3 and 7 both, the program will print 'FizzBuzz'

print ("Welcome to FizzBuzz!")

def fizzbuzz(int):
    if int %3 == 0 and int %7 == 0:
        return ("FizzBuzz")
    elif int %3 == 0:
        return ("Fizz")
    elif int %7 == 0:
        return ("Buzz")
    else:
        return (int)

x = int(input("Enter a number to start the game: "))
y = fizzbuzz(x)
print (y)