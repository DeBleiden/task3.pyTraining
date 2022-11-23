import re

reg = 'String with some host names: ats01-c01-tel01, ats02-p02-tel02, amr01-c01-pts01, amr03-p02-tel01'


def regexHostNameSearch(string):
    output = re.findall(r'(amr0[1-9]-[cp]0[1-9]-[a-z]{3}0[1-9])', string)
    print(output)


regexHostNameSearch(reg)
