
def introKor():
	print('안녕하세요')
def introEng():
	print('hi')
def introJap():
	print('곤니찌와')
#def exitGreet():
#	break	

while True :
	selectNum=int(input('where are you from?\n 1.KOR 2.USA 3.JAP 4.종료\n'))
	
	if(selectNum==1):
		introKor()
	elif(selectNum==2):
		introEng()
	elif(selectNum==3):
		inrtoJap()
	elif(selectNum==4):
		exitGreet()
	else:
		introEng()
