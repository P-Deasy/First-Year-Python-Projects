# ScriptName: functions.py
# Author: Paul Deasy 118312303

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


def while_loop(max_number=10, even=False, factorial=False):
    n = 1
    a = 0
    b = 1
    mylist = []
    # Added if else statement to allow for minus numbers
    if max_number > 0:
        while n <= max_number:
            if n > 12:
                break
            # Added if not and if even statements
            if not even:
                mylist.append(n)
                a += n
                n += 1
            if even:
                if n % 2 == 0:
                    mylist.append(n)
                    a += n
                    n += 1
                else:
                    n += 1
        n -= 1
    else:
        while n >= max_number:
            if n < -12:
                break
            if not even:
                # Used + instead of append this time to create correct list
                mylist = [n] + mylist
                a += n
                n -= 1
            if even:
                if n % 2 == 0:
                    mylist = [n] + mylist
                    a += n
                    n -= 1
                else:
                    n -= 1
        n += 1
    mylist.append(a)
    if factorial:
        # Use in built factorial function
        # Had to change to own code as negative values are not supported with built in function
        if n >= 0:
            for i in range(1, n+1):
                b = b*i
        if n <= 0:
            for i in range(n, 0):
                b = b*i
        mylist.append(b)
    print(mylist)
    return mylist
