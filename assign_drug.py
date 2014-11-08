def assign_drug(filename):
    number = filename[13:-4]
    #print number
    result = ''
    if int(number) % 2  == 0:
        output = 'tylenol'
    else:
        output = 'placebo'
    return output

import sys

filename = sys.argv[1]
print assign_drug(filename)

assert assign_drug("inflammation_4.dat") == "tylenol"
assert assign_drug("inflammation_3.dat") == "placebo"
