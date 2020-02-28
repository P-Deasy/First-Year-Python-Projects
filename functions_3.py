def while_loop(max_number=10, even=False, factorial=False):
    '''
    Contains a while loop that loops from 1 to
    n, where n is a positive number (passed as parameter - max_number), saving the number in
    a list on each loop. The function will return the list of all numbers.
    If a negative number is passed to
    while_loop(max_number), the list shall return the numbers from 1 to the negative number
    It will also add the numbers as they gousing an accumulator and add this value as the 
    last value in the list
    Irrespective of the value of the max_number parameter, the output list will never go 
    higher than 12, or lower than -12
    It takes a second parameter (even), aboolean value which when True only adds 
    the even numbers to the list
    If boolean is True it will add the factorial value of the last number in the while loop as the last parameter
    '''
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
