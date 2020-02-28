def to_english(n=0):
    '''
    Takes a positive or negative integer value
    ‘n’ and that returns a string containing the number expressed in English words.
    (From - to + 999)
    '''
    n = str(n)
    # Created dictionaries to assign names to the numbers
    num1 = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9'
            : 'nine'}
    num2 = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty',
            '9': 'ninety'}
    num3 = {'1': 'one hundred', '2': 'two hundred', '3': 'three hundred', '4': 'four hundred', '5': 'five hundred',
            '6': 'six hundred', '7': 'seven hundred', '8': 'eight hundred', '9': 'nine hundred'}
    teens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
             '16': 'sixteen', '17': 'eighteen', '18': 'eighteen', '19': 'nineteen'}
    # Separated out the minuses so I can just add that value back in later
    if n[0] == '-':
        minus = True
        n = n[1:]
    else:
        minus = False
    # Split the list into three sections for each of the digits and called each
    if len(n) == 1:
        if n == '0':
            number = 'Zero'
        else:
            number = num1[n]
    if len(n) == 2:
        if n[0] == '1':
            number = teens[n]
        elif n[1] == '0':
            number = str(num2[n[0]])
        else:
            number = str(num2[n[0]]) + ' ' + str(num1[n[1]])
    if len(n) == 3:
        if n[1] == '0' and n[2] == '0':
            number = str(num3[n[0]])
        elif n[2] == '0':
            number = str(num3[n[0]]) + ' and ' + str(num2[n[1]])
        elif n[1] == '0':
            number = str(num3[n[0]]) + ' and ' + str(num1[n[2]])
        else:
            number = str(num3[n[0]]) + ' and ' + str(num2[n[1]]) + ' ' + str(num1[n[2]])
    if minus:
        return 'Minus ' + number
    else:
        return number.capitalize()


def sort_a_list(s):
    '''
    Takes a list of number or single characters and returns a sorted list
    '''
    # Set the start of all the lists
    newlist = [0]
    minus_list = ['0']
    minus = []
    for i in s:
        # Check if the value has not already occurred
        if i not in newlist:
            # Create a second case for minus value as for ascii method I need to remove the minus
            if len(str(i)) == 2:
                i1 = (str(i))[1]
                # Check if we're adding it to the start or end of the list
                if ord(str(i1)) > ord(str(minus_list[-1])):
                    # Use two separate lists one for ord and one for our return value
                    minus_list.insert(0, str(i1))
                    minus.insert(0, i)
                    j = 0
                    # Swap numbers until it arrives at the correct position
                    while j < len(minus_list)-1:
                        if ord(str(minus_list[j])) < ord(str(minus_list[j + 1])):
                            num1 = minus_list[j]
                            num3 = minus[j]
                            num2 = minus_list[j+1]
                            num4 = minus[j+1]
                            minus_list[j+1] = num1
                            minus[j+1] = num3
                            minus_list[j] = num2
                            minus[j] = num4
                        j += 1
                if ord(str(i1)) < ord(str(minus_list[-1])):
                    minus_list += str(i1)
                    minus.append(i)
            else:
                # Now for regular numbers and letters do the same and add th result to their own separate list
                if ord(str(i)) < ord(str(newlist[-1])):
                    newlist.insert(0, i)
                    j = 0
                    while j < len(newlist)-1:
                        if ord(str(newlist[j])) > ord(str(newlist[j+1])):
                            num1 = newlist[j]
                            num2 = newlist[j+1]
                            newlist[j+1] = num1
                            newlist[j] = num2
                        j += 1
                if ord(str(i)) > ord(str(newlist[-1])):
                    newlist.append(i)
    # Remove first value, our generic 0 from the start
    newlist = newlist[1:]
    # Add the plus list to the minus list
    for i in newlist:
        minus.append(i)
    return minus


def ascii_difference(m, n):
    '''
    Takes 2 lists 'm' and 'n' and
    will return two lists. The first returned list is the combined ascii value of the
    elements @ the same index number, the second list is the absolute ascii difference
    between each element @ the same index number
    '''
    # Set up our empty lists and accumulators
    list1 = []
    list2 = []
    j = 0
    k = 0
    # Use three different conditions for varying lengths of lists
    if len(m) == len(n):
        for i in m:
            list1.append((ord(str(i))) + ord(str(n[j])))
            list2.append((abs(ord(str(i)) - ord(str(n[j])))))
            j += 1
    if len(m) > len(n):
        while j < len(n):
            list1.append(((ord(str(n[k]))) + ord(str(m[j]))))
            list2.append((abs(ord(str(n[k])) - ord(str(m[j])))))
            j += 1
            k += 1
        # If one list is bigger than the other add bare values after exhausting shorter list
        while j < len(m):
            list1.append(ord(str(m[j])))
            list2.append(ord(str(m[j])))
            j += 1
    if len(n) > len(m):
        while k < len(m):
            list1.append(((ord(str(n[k]))) + ord(str(m[j]))))
            list2.append(((ord(str(n[k]))) + ord(str(m[j]))))
            j += 1
            k += 1
        while k < len(n):
            list1.append(ord(str(n[k])))
            list2.append(ord(str(n[k])))
            k += 1
    return list1, list2

print(to_english(121))
