#기본 도형 그리는 것을 반복문을 사용해서 연습해보겠습니다.
import turtle as t
t.color('blue')
for x in range (3) :
    t.fd(120)
    t.lt(120)
#방향을 왼쪽으로 설정하면 반시계방향으로 그려짐 화살표 방향을 원래 있던대로


#사각형
t.color('red')
for x in range (4) :
    t.fd (120)
    t.lt(90)
    
#원
t.color('yellow')
t.circle(120)
