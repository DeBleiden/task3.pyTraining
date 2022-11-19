import re

reg = '255.255.255.255 8.8.8.8 256.255.255.255 192.168.1.1 0.0.0.0 10.24.3.1 109.210.53.211 172.217.22.14'
result = []
counterList = []


def regexIPSearch(defaultReg):
    selectionList = re.findall(r'\d+.\d+.\d+.\d+', defaultReg)

    for tstValue in selectionList:
        for x in tstValue.split('.'):
            if 0 <= int(x) < 256:
                counterList.append(x in tstValue)
                if counterList.count(True) == 4:
                    result.append(tstValue)
                    counterList.clear()
            else:
                break
    print(result)


regexIPSearch(reg)
