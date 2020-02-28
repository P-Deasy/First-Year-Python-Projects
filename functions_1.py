# ScriptName: functions.py
# Author: Paul Deasy 118312303

# template for calling functions in another file


def a_function():
    return ("I'm in another file :)")


def removeVowels(sentence):
    vowels = 'aeiou'
    filtered_list = [l for l in sentence if l not in vowels]
    return ''.join(filtered_list)


def hailStone(n):
    hail_sequence = []
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        hail_sequence.append(int(n))
    return hail_sequence


hexToBinaryTable = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                    '6': '0110', '7': '0111', '8': '1000 ', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D':
                        '1101', 'E': '1110', 'F': '1111'}


def hexToBinary(hex, d):
    hexlist = [d[i] for i in hex]
    return ''.join(hexlist)


codon_map = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
             'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine',
             'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine', 'UGC':
             'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'stop', 'UAG': 'stop', 'UGA': 'stop'}


def RNA_Transcript(rna):
    protein_list = []
    rna_list = [rna[i:i + 3] for i in range(0, len(rna), 3)]
    for i in rna_list:
        if codon_map[i] == 'stop':
            break
        protein_list.append(codon_map[i])
    print(rna_list)
    print(protein_list)


def tenkSteps(stepData):
    n = 0
    m = 0
    day = 0
    while m <= 4:
        templist = []
        total = 0
        while n <= 9:
            templist.append(stepData[n][m])
            for nm in range(0, len(templist)):
                total = total + templist[nm]
            if total >= 100000:
                day += 1
            n += 1
        m += 1
    return total


def mostSteps(stepData):
    n = 0
    m = 0
    i = 0
    empindex = 0
    empnum = 0
    while m <= 9:
        templist = []
        total = 0
        while n <= 4:
            templist.append(stepData[m][n])
            for nm in range(0, len(templist)):
                total = total + templist[nm]
                emplist.append(total)
            n += 1
        m += 1
    while i < len(emplist):
        if emplist[i] > empnum:
            empnum = emplist[i]
            empindex = i
    return empindex