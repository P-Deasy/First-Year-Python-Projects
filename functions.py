# ScriptName: functions.py
# Author: Paul Deasy 118312303


def a_function():
    return ("I'm in another file :)")


chooseLargest = (lambda a, b: map(max, zip(a, b)))


def read_draw():
    lotto1 = open('C:.../lotteryNumbers.txt', 'r')
    lotto = lotto1.readlines()
    lotto_result = [list(map(int, i.split())) for i in lotto]
    return list(lotto_result)


def del_1000(courierData):
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


appendlist = lambda list1, list2: map(sum, zip(list1, list2))


def client_matcher(name):
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
