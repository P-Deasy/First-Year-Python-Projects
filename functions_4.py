def count(list, value):
    '''
    return the number of times value occurs in list
    '''
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
    '''
    Returns the first index that value occurs in list.
    Returns -1 if the value does not occur in the list.
    '''
    i = 0
    while i < len(list):
        if list[i] == value:
            print(i)
            return i
        i += 1


def get_value(list, index):
    '''
    Returns the value that occurs in the list at
    index
    '''
    i = 0
    while i < len(list):
        if list[i] == list[index]:
            print(list[i])
            return list[i]
        i += 1


def insert(List, index, value):
    '''
    Returns list, after you have added value at
    index
    '''
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
    '''
    Returns True or False if value occurs in list
    '''
    for i in list:
        if i == value:
            return True
    else:
        return False


def concat(list1, list2):
    '''
    Returns a new list, which is a combination of
    list1 and list2
    '''
    list1 = str(list1)
    list2 = str(list2)
    # Use .join to join two lists
    newlist = ' '.join((list1, list2))
    print(newlist)
    return newlist


def remove(value, List):
    '''
    Returns list with the first occurrence of value
    removed from list
    '''
    i = 0
    List = list(str(List))
    while i < len(List):
        if List[i] == value:
            del(List[i])
            List = ''.join(List)
            print(List)
            return List
        i += 1
