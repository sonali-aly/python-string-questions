from collections import deque 
s = input("Enter string :")
dq = deque(s)
flag = True
while len(dq) > 1:
     first = dq.popleft() 
     last = dq.pop()
     if first!= last:
        flag = False
        break
if flag:
        print("palindrome")
else:
        print("non palindrome")
