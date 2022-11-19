import re

reg = 'Some text 192.168.1.1 with some IP addresses 10.24.3.1 and 1923.168.101.150'


def regexIPSearch(string):
    tempList = re.findall(r'\d+.\d+.\d+.\d+', string)
    for i in tempList:
        if len(i) > 15:
            continue
        else:
            print(i)


regexIPSearch(reg)
