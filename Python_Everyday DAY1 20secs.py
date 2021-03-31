import time
input("엔터를 누르고 마음속으로 20초를 세세요.")
start=time.time()
input("20초를 다 세셨으면, 다시 엔터를 눌러주세요.")
end=time.time()
et=end-start
print ('실제시간 :',et,'초')
print ('차이 :',abs(et-20),'초')
