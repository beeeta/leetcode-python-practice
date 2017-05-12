from argparse import ArgumentParser
import sys

# practice
# https://leetcode.com/problems/two-sum/#/description

if __name__ == '__main__':
    parse = ArgumentParser()
    parse.add_argument('--array','-a',dest='array',nargs='*')
    parse.add_argument('--target','-t',dest='target',type=int)
    args = parse.parse_args()
    ar = args.array
    tg = args.target
    for i in range(len(ar)):
        for j in range(i,len(ar)):
            if i==j:
                continue
            if int(ar[i])*int(ar[j]) == tg:
                print('beego! the target index is: %s %s ' % (i,j))
                sys.exit(0)  
    else:
        print('not find correct answer~')