def addFnc(num):
    if num > 0:
        print('num =', num)
        addFnc(num-1)
        print('num =',num)
        
addFnc(10)