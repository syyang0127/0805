import os

def add():
	print('덧셈 결과 : ', inputNum1 + inputNum2)

def sub():
	print('뺄셈 결과 : ', inputNum1 - inputNum2)

def mul():
	print('곱셈 결과 : ', inputNum1 * inputNum2)

def div():
	print('나눗셈 결과 : ', inputNum1 / inputNum2)

while True:
	input('계속하려면 아무키 누르세요\n')
	os.system('clear') #화면 클리어 시키는 명령어.
	selectOperator = int(input('연산자 선택 : 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료\n'))
	if(selectOperator==5):
		break


	inputNum1 = float(input('첫 번째 숫자 입력 : '))
	inputNum2 = float(input('두 번째 숫자 입력 : '))

	if(selectOperator==1):
		add()

	elif(selectOperator==2):
		sub()

	elif(selectOperator==3):
		mul()

	elif(selectOperator==4):
		div()

