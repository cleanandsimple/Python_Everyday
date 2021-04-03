#오늘도 도형 그리는 연습을 해보겠습니다. 이것저것 툴도 써 봅시다.

import turtle as t
t.pencolor('skyblue')
t.shape('triangle')
t.bgcolor('green')
for x in range(3) :
    t.fd(120)
    t.lt(120)

#방금 어떻게 t를 빼먹고 쳤을수가 있어.............
#인풋이랑 for을 왜 헷갈리는데.............for이 반복이라고 ㅠㅠㅠㅠㅠ


#이번에는 사각형을 만들어보겠습니다....시계반대방향으로 만들어볼까요
import turtle as t
t.pencolor('yellow')
t.bgcolor('black')
for x in range (4) :
    t.fd(120)
    t.lt(90)
#마지막으로 빠르게 원을 만듭니다....
import turtle as t
t.pencolor ('skyblue')
t.speed(0)
t.circle(120)

