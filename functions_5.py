# ScriptName: functions.py
# Author: 118312303 Paul Deasy

# template for calling functions in another file

import random


def print_function():
    print("I'm in another file :)")


def is_stairs(s):
    n = 1
    y = True
    x = True
    z = True
    for i in s:
        if n >= len(s):
            break
        # Use str and lower so ascii method will work
        if ord((str(i)).lower()) + 1 == ord((str(s[n])).lower()):
            # used these variables so as to avoid 'a' 'b' 'a' like patterns coming as true
            x = True
            y = False
            if not z:
                return False
        elif ord((str(i)).lower()) - 1 == ord((str(s[n])).lower()):
            x = True
            z = False
            if not y:
                return False
        else:
            return False
        n += 1
    return x


def factorial(n=0):
    i = 1
    if n == 0:
        return 1
    for i in range(n):
        i = i*(i+1)
    return i


def is_okay_to_feed(time):
    if time in range(0, 4):
        return False
    if time in range(5, 24):
        return True


def is_wet():
    return True or False


def is_to_bright(lux_level):
    if lux_level > 80:
        return True
    else:
        return False


def gremlins(name='Gizmo'):
    title = 'the one and only'
    for i in range(5):
        # using true or false to add randomness
        x = True or False
        if x is True:
            if not is_okay_to_feed(random.randint(0, 24)):
                name = 'Stripe'
        z = True or False
        if z is True:
            if is_to_bright(random.randint(0, 100)):
                return name + ' ' + title + ' is very dead'
        c = True or False
        if c is True:
            if is_wet() is True:
                title = 'the third'
    # using variable results to determine what is returned
    if name == 'Stripe':
        if title == 'the third':
            return name + ' is a triplet now'
        return name + ' is a gremlin'
    elif title == 'the third':
        return name + ' is a triplet now'
    else:
        return name + ' ' + title + ' ' + 'is still a cute Mogwai'
