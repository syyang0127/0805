def calc(num1,num2):
    result1=num1+num2
    result2=num1-num2
    result3=num1*num2
    result4=num1/num2
    
    # 대괄호는 list, 중괄호는 set, 소괄호는 tuple
    # 중괄호 안에 'key:value'로 입력하면 dictionary
    return(result1,result2,result3,result4) 

inputNum1 = int(input('첫 번째 정수 입력:'))
inputNum2 = int(input('두 번째 정수 입력:'))

result = calc(inputNum1, inputNum2)

print(type(result))
print('사칙연산결과 : ',result)
print('덧셈 : ',result[0])
print('뺄셈 : ',result[1])
print('곱셈 : ',result[2])
print('나눗셈 : ',result[3])