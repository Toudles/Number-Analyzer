#even number

def is_even(num):
    return num % 2 == 0


#odd number (remainder not 0)
def is_odd(num):
    return num % 2 == 1

#determine if it's prime
def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

#determine if the number is perfect
def is_perfect(num):
    sum = 0 
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

#determine if the number is abundant
def is_abundant(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return num < sum

#^that's from my analyzer code

#anaylze abundant numbers
def abundant(start, end):
    print('All abundant number between {} and {}'.format(start, end))
    print('#' * 15)
    for num in range(start, end + 1):
        if is_abundant(num): print(num)
    print('#' * 15)

#analyze prime numbers
def prime(start, end):
    print('All prime number between {} and {}'.format(start, end))
    print('#' * 15)
    for num in range(start, end + 1):
        if is_prime(num): print(num)
    print('#' * 15)

#analyze perfect numbers
def perfect(start, end):
    print('All perfect number between {} and {}'.format(start, end))
    print('#' * 15)
    for num in range(start, end + 1):
        if is_perfect(num): print(num)
    print('#' * 15)

#create the chart to determine if the numbers are certain categories
def chart(start, end):
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('Number', 'Even', 'Odd', 'Prime', 'Perfect','Abundant'))
    for num in range(start, end + 1):
        even = 'x' if is_even(num) else ''
        odd = 'x' if is_odd(num) else ''
        prime = 'x' if is_prime(num) else ''
        perfect = 'x' if is_perfect(num) else ''
        abundant = 'x' if is_abundant(num) else ''
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(num, even, odd, prime, perfect, abundant))

#set function to determine the starting/ending number for the range
def Range():
    while True:
        start = int(input('Enter starting number (positive only): '))
        if start < 0:
            print('Invalid, try again')
        else:
            break
    while True:
        end = int(input('Enter ending number: '))
        if end <= start:
            print('Invalid, try again')
        else:
            break
    return start, end

#create the main menu to ask the user what they want to search for
def main():
    while True:
        print('Main Menu')

        print('')

        print('1 - Find all prime numbers within a given range')
        print('2 - Find all perfect numbers within a given range')
        print('3 - Find all abundant numbers within a given range')
        print('4 - Chart all even, odd, prime, perfect and abundant numbers within a given range') 
        print('5 - Quit')

        print('')

        choice = input('Your choice: ')

        if choice == '1':
            starts, ends = Range()
            prime(starts, ends)

        elif choice == '2':
            starts, ends = Range()
            perfect(starts, ends)

        elif choice == '3':
            starts, ends = Range()
            abundant(starts, ends)

        elif choice == '4':
            starts, ends = Range()
            chart(starts, ends)

        elif choice == '5':
            print('')
            print("Goodbye!")
            break

        else:
            print('I don''' 't understand that ...')

main()