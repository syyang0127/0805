def introKor():
	print('안녕하세요')

def introEng():
	print('hi')

def introJap():
	print('곤니찌와')

print('where are you from?')
selectNum = int(input('1. 한국 , 2.USA, 3.Japan\n'))

if(selectNum==1):
	introKor()

elif(selectNum==2):
	introEng()

elif(selectNum==3):
	introJap()

else:
	introEng()


