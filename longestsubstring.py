# practice
# https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
from argparse import ArgumentParser

if __name__ == '__main__':
    parse = ArgumentParser()
    parse.add_argument('sstr',type=str)
    args = parse.parse_args()
    sstr = args.sstr
    aindex = 0
    longestr = []
    currentStr = []
    for i in range(len(sstr)):
        if sstr[i] in currentStr:
            if len(currentStr)>=len(longestr):
                longestr = currentStr
            currentStr = []
            currentStr.append(sstr[i])
        else:
            currentStr.append(sstr[i])
        
    print('the longest substring is: %s ' % ''.join(longestr))

