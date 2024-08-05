def fncA():
    print("function A start")
    fncB()
    print("function A end")

def fncB():
    print("function B start")
    fncC()
    print("function B end")
    
def fncC():
    print("function C start")
    print("function C end")
    
fncA()



"""
stack 개념을 알 수 있는 예제
*함수는 memory에서 stack으로 쌓인다.
호출된 함수가 먼저 실행되고 memory에 남은 것들이 다 실행되고
메인 전체가 종료된다.

main에서 호출된 함수는 fncA뿐이라서
fncA안의 내용이 다 실행돼야 main의 동작이 마무리된다.

fncA 호출 
-> fnca start 출력 
-> fncB 호출 (이때, fncA end 출력 명령이 memory에 남음)
~~~
-> fncC 호출
-> fnc C start 출력 -> fncC end 출력
-> 그리고 memory에 쌓여서 실행되지 않던 작업들이 수행됨
~~~
-> 마지막에 fncA end 출력되고 main 종료
"""