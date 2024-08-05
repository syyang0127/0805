def fac(num):
    if num == 1:
        return 1
    else :
        return num * fac(num-1)

inputData = int(input('0보다 큰 숫자 입력'))
result = fac(inputData)
print('%d! = %d\n'%(inputData,result))

"""
fac(5)호출
    5*fac(4)
        4*fac(3)
            3*fac(2)
                2*fac(1)
                ->(1)일때, 값이 1로 return되고
            역순으로
        호출된 함수의 리턴값이
    저장되고
마지막 단에서 출력되고 종료.
"""