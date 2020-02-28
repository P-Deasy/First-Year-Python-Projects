def seasons():
    '''
    Select the season based on the input value where 1=Winter,
    2=Spring, 3=Summer, and 4=Autumn.
    '''
    while True:
        try:
            season = int(input("Give me a number:"))
            break
        except:
            print("Enter a number")
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    if season == 1:
        print(seasons[0])
    elif season == 2:
        print(seasons[1])
    elif season == 3:
        print(seasons[2])
    elif season == 4:
        print(seasons[3])
    else:
        print("Number has to be between 1 and 4")


def grades():
    '''
    Changes numerical grades to Letter grades and vice-versa
    '''
    try:
        grade = int(input("Enter a result:"))
        if 100 >= grade >= 85:
            print("A")
        elif 84 >= grade >= 70:
            print("B")
        elif 69 >= grade >= 55:
            print("C")
        elif 54 >= grade >= 40:
            print("D")
        elif 39 >= grade >= 25:
            print("E")
        elif 24 >= grade >= 0:
            print("F")
        else:
            print("X")
    except:
        # Added the capitalise statement so as to make grades work better
        gradeletter = (str(input('Enter a grade:'))).capitalize()
        if gradeletter == 'A':
            print('85-100')
        elif gradeletter == 'B':
            print('70-84')
        elif gradeletter == 'C':
            print('55-69')
        elif gradeletter == 'D':
            print('40-54')
        elif gradeletter == 'E':
            print('25-39')
        elif gradeletter == 'F':
            print('0-24')
        else:
            print('Thats not a grade')


def fizz_buzz():
    '''
    For multiples of
    divisor_1 the function return “Fizz”. For multiples of divisor_2, return “Buzz”. For
    numbers which are multiples of both divisor_1 and divisor_2 return “FizzBuzz” 
    '''
    while True:
        try:
            fbnum = float(input("Enter a number:"))
            divisor_1 = float(input("Enter a number:"))
            divisor_2 = float(input("Enter a number:"))
            break
        except:
            print("Enter a number")
    if fbnum % divisor_1 == 0 and fbnum % divisor_2 == 0:
        print("FizzBuzz")
    elif fbnum % divisor_1 == 0:
        print("Fizz")
    elif fbnum % divisor_2 == 0:
        print("Buzz")
    else:
        print(fbnum)


def slice_reverse(b):
    '''
    determine if the input_value is a palindrome
    '''
    a = list(b)
    if a[:] == a[::-1]:
        print(True)
    else:
        print(False)


def add_to_list(value, mylist):
    '''
    The function will add value to the list if
    the list does not already contain the value
    '''
    if value not in mylist:
       mylist.append(value)
    print(mylist)
