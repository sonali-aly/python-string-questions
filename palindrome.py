#num = input("enter your number")
# if num == num[::-1]:#for revrsing the number
   # print("yes")
#else:
  #  print("no")

num = int(input("enter the number"))
temp = num
rev = 0
while num >0:
    digit  = num%10
    rev = rev*10+digit
    num = num//10

if temp ==rev:
    print("yes")
else:
    print("no")