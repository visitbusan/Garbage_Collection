import sys

text = '가비지 컬렉션'
print('변수 text의 초기 카운트 : ', sys.getrefcount(text))  #초기 카운트가 4

lst = [text]
print('리스트 참조 후 카운트 : ', sys.getrefcount(text))  #리스트에 사용되면서 카운트가 5가된다

tup = (text)
print('튜플 참조 후 카운트 : ', sys.getrefcount(text))  #튜플에 사용되면서 카운트가 6이된다

dic = {'text': text}
print('딕셔너리 참조 후 카운트 : ', sys.getrefcount(text))  #딕셔너리에 사용되면서 카운트가 7이된다

a = text
print('변수 참조 후 카운트 : ', sys.getrefcount(text))  #변수에 사용되면서 카운트가 8이된다
print('삭제--------------------------')
del a
print('변수 삭제 후 카운트 : ', sys.getrefcount(text))  #text를 사용한 a가 삭제되면서 카운트가 7이된다

del dic
print('딕셔너리 삭제 후 카운트 : ',
      sys.getrefcount(text))  #text를 사용한 dic이 삭제되면서 카운트가 6이된다

del tup
print('튜플 삭제 후 카운트 : ', sys.getrefcount(text))  #text를 사용한 tup가 삭제되면서 카운트가 5가된다

del lst
print('리스트 삭제 후 카운트 : ',
      sys.getrefcount(text))  #text를 사용한 lis가 삭제되면서 카운트가 4가된다
print('변수 text의 카운트가 초기값으로 돌아왔다\n\n')

print('메모리 누수가 발생하는 경우===========')

a = [1]
print('a 리스트 생성 후 카운트 : ', sys.getrefcount(a))
a.append(a)
print('본인참조(a.append(a)) 후 카운트 : ', sys.getrefcount(a))
print(a, '출력 후 카운트 : ', sys.getrefcount(a))
print('출력 종료 후 칸운트 : ', sys.getrefcount(a))
del a  #a 삭제
# print(a)                         #오류발생

#상호참조
#클래스 변수에 서로를 참조하고있는 경우에도 메모리 누수가 발생한다
# a = Obj()    #Obj라는 가상 클래스
# b = Obj()

# a.x = b    #Obj클래스에 x라는 변수에 서로를 대입
# b.x = a

# del a
# del b

print('순환참조 해결방안 ==================')

import gc

print(gc.get_threshold())  #순서대로 0세대 1세대 2세대 객체한도
#0세대의 객체 한도가 차면 가비지를 비운 후 살아남은 객체를 1세대로 이동시킨다 1세대도 마찬가지로 살아남으면 2세대로 이동한다
gc.set_threshold(1000, 100, 100)  #쓰레기통 한도설정
gc.collect()  #수동 비우기
