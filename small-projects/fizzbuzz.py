# '''The humble fizzbuzz
# Solved here with no particular twist
# It asks the user for a number,
# then prints all numbers from 1 up to that number
# but replaces multiples of 3 with 'Fizz' 
# and multiples of 5 with 'Buzz''''

def fizz_buzz():
    num='x'
    while num.isdigit() == False:
        num=input('Please enter a number here: ')
    num=int(num)
    for i in range(1,num+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)


fizz_buzz()
