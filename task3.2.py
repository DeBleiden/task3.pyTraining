import re

reg = 'String with some host names: ats01-c01-tel01, ats02-c02-tel02, amr01-c01-pts01'


def regexHostNameSearch(string):
    output = re.findall(r'([a-z]+[0-9][0-9]-[a-z]+[0-9][0-9]-[a-z]+[0-9][0-9])', string)
    print(output)


regexHostNameSearch(reg)
