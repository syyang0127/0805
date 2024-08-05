#-------------------------------------------------------
def printAvgScore(*scores): # 여러 인자를 받을 수 있다.
	print(type(scores)) # score의 타입 확인
	
	totalScore = 0
	cnt = len(scores) # 과목의 갯수를 cnt에 저장

	for score in scores :
		totalScore += score
	
	print('총점 : ',totalScore, '점')
	print('평점 : ',totalScore/cnt, '점')
	print('-----------------------------')
#-------------------------------------------------------

printAvgScore(80,90,100)
printAvgScore(80,100,86,89)
printAvgScore(91,89,94,99,95)


