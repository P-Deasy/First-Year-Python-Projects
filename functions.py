# example of a lambda function that takes two lists and chosses largest at each index
chooseLargest = (lambda a, b: map(max, zip(a, b)))


def read_draw():
    '''
    Read lottery result numbes from a txt file and outputs lists of each
    draw as a lists of integers.
    '''
    lotto1 = open('C:.../lotteryNumbers.txt', 'r')
    lotto = lotto1.readlines()
    lotto_result = [list(map(int, i.split())) for i in lotto]
    return list(lotto_result)


#Consider a courier company that has 10 drivers, numbered 0 to 9,
#that records the number of deliveries by each driver, over a 5 day week with days
#numbered 0 to 4, in a table having 10 rows and 5 columns. Thus, for example, the
#entry in row 7 and column 3 gives the number of the deliveries by driver number 8
#on day number 2.


def del_1000(courierData):
    '''
    Returns the total number of days on which at 
    least 1000 deliveries were made.
    '''
    m = 0
    deliver = 0
    while m <= 4:
        templist = []
        n = 0
        total = 0
        while n <= 9:
            templist.append(courierData[n][m])
            n += 1
        for nm in range(0, len(templist) - 1):
            total = total + templist[nm]
        if total >= 1000:
            deliver += 1
        m += 1
    return deliver


def mostdel(courierData):
    '''
    Returns the number of the courrier with the most deliveries.
    '''
    m = 0
    i = 0
    empindex = 0
    empnum = 0
    emplist = []
    while m <= 9:
        templist = []
        total = 0
        n = 0
        while n <= 4:
            templist.append(courierData[m][n])
            n += 1
        for nm in range(0, len(templist) - 1):
            total = total + templist[nm]
        emplist.append(total)
        m += 1
    while i < len(emplist) - 1:
        if emplist[i] > empnum:
            empnum = emplist[i]
            empindex = i
        i += 1
    return empindex


#Adds two lists together at each index (example of lambda functions)
appendlist = lambda list1, list2: map(sum, zip(list1, list2))


# Data Consulting Agency (DCA) needs you to develop software to
#match their clients. The list of clients is in a text file with one line per client. The
#following is an example of six clients although you should assume the client list to be
#larger.
#John Smith, M, 27, F, 24, 29, movies, tennis, walking, computers
#Alison Jones, F, 25, M, 26, 32, walking, golf, movies, reading
#Brian Adams, M, 30, F, 23, 28, golf, cricket
#Chris Jones, M, 27, F, 30, 40, golf, reading
#Paul Fulton, M, 23, M, 21, 25, football, reading
#Peter Jackson, M, 25, M, 20, 30, golf, walking, movies
#The file specifies information about the client. For example, John Smith is male, 27
#years old and wishes to meet a female aged between 24-29 inclusive; his interests
#are movies, tennis, walking and computers.
#Write the code to process the client list, assumed to be in a file named clients.txt into a
#dictionary called clients. The name of the client is the dictionary key which you can assume
#to be unique and the remaining client information i.e. the dictionary value should be a list.
#Clients are compatible if each one is of the gender and age range that the other is seeking.
#For the purposes of this question you can ignore common interests. No-one should be
#matched to themselves. Write the code to a function check_match that accepts a client’s
#name as a string, determines suitable matches and outputs the matches to the screen e.g.
#assuming the client was Alison Jones, potential matches would be John Smith, Brian Adams
#and Chris Jones.


def client_matcher(name):
    '''
    Matches clients to each other
    '''
    x = 0
    client_dictionary = {}
    temp_clients = open('C:.../clients.txt', 'r')
    clients = temp_clients.readlines()
    client_list = [list(i.split(',')) for i in clients]
    for i in client_list:
        client_list[x][-1] = i[-1][0:-1]
        x += 1
    for i in client_list:
        value = []
        key = i[0]
        values = i[1:]
        for y in values:
            value.append(y[1:])
        client_dictionary[key] = value
    for i in client_dictionary:
        if client_dictionary[name][2] == client_dictionary[i][0] and client_dictionary[i][2] == \
                client_dictionary[name][0] and int(client_dictionary[i][4]) >= int(
                client_dictionary[name][1]) >= int(client_dictionary[i][3]) and int(client_dictionary[name][4]) >= int(
                client_dictionary[i][1]) >= int(client_dictionary[name][3]) and name != i:
            print(name, 'should meet', i)
