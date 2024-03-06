#loop to count up to 100 from 1
for x in range(1,101):

    #checks if the current number is divisible by 3 AND 5, if so prints "FizzBuzz", if not moves on to next statement
    if(x%3 == 0 and x%5 == 0):
        print("FizzBuzz")

    #checks if the current number is divisible by 3, if so prints "Fizz", if not moves on    
    elif(x%3 == 0):
        print("Fizz")

    #checks if the current number is divisible by 5, if so prints "Buzz", if not moves on    
    elif(x%5 == 0):
        print("Buzz")
    
    #none of the other statements were true, so it prints the number and then repeats the loop
    else:
        print(x)