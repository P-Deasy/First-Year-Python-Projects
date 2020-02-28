# ScriptName: functions.py
# Author: Paul Deasy 118312303

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


#def count(list, value):
#    '''
 #   function - count how many times <value> occurs in <list>
  #  :param list: - <list> input
   # :param value: - <value> to search for
    #:return:
    #'''
    # set counter
 #   i = 0
    # accumulator to count how many times <value> occurs
    # set to zero to cover no <value> in <list>
  #  num_values = 0
    # loop over the length of the <list>
   # while i < len(list):
        # if <value> and <list> index i are the same
    #    if list[i] == value:
            # increment the accumulator
     #       num_values += 1
        # increment the counter
      #  i += 1
    # return how many times <value> occurs in <list>
    #return num_values


def count(list, value):
    i = 0
    number = 0
    # Added str so function could accept numbers too
    list = str(list)
    while i < len(list):
        if list[i] == str(value):
            number += 1
        i += 1
    print(number)
    return number


def index(list, value):
    i = 0
    while i < len(list):
        if list[i] == value:
            print(i)
            return i
        i += 1


def get_value(list, index):
    i = 0
    while i < len(list):
        if list[i] == list[index]:
            print(list[i])
            return list[i]
        i += 1


# Had to change list variable to List so list() function would work
def insert(List, index, value):
    # Added str() argument so integers etc could be used
    List = list(str(List))
    i = 0
    if index >= len(List):
        List.append(str(value))
    else:
        while i < len(List):
            if List[i] == List[index]:
                List[i] = str(value)
            i += 1
    print(''.join(List))
    return ''.join(List)


def value_in_list(list, value):
    for i in list:
        if i == value:
            return True
    else:
        return False


def concat(list1, list2):
    list1 = str(list1)
    list2 = str(list2)
    # Use .join to join two lists
    newlist = ' '.join((list1, list2))
    print(newlist)
    return newlist


def remove(value, List):
    i = 0
    List = list(str(List))
    while i < len(List):
        if List[i] == value:
            del(List[i])
            List = ''.join(List)
            print(List)
            return List
        i += 1
