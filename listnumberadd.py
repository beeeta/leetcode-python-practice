# practice
# https://leetcode.com/problems/add-two-numbers/#/description

if __name__ == '__main__':
    parse = ArgumentParser()
    parse.add_argument('--first','-f',nargs='*',dest='fparam',type=int)
    parse.add_argument('--second','-s',nargs='*',dest='sparam',type=int)
    args = parse.parse_args()
    fparam = args.fparam
    sparam = args.sparam
    addplase = 0
    maxleng = max(len(fparam),len(sparam))
    res = []
    for i in range(maxleng):
        fvalue = 0
        svalue = 0
        if i<len(fparam):
            fvalue = fparam[i]
        if i<len(sparam):
            svalue = sparam[i]         
        addres = fvalue+svalue+addplase
        if addres>9:
            addres -= 10
            addplase = 1
        else:
            addplase = 0
        res.append(addres)
        
    if addplase ==1:
        res.append(addplase)
    
    print('result is : %s ' % res)
        