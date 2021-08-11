c=" "
s="*"
#>>> A1 code <<<
a=0
print(c*2+s*16+c*2)
while a<2:
    print(s*20)
    a=a+1
while a<5:
    print(s*6 + c*8 + s*6)
    a=a+1
while a<7:
    print(s*20)  #The same code in the line 5
    a=a+1
while a<10:
    print(s*6 + c*8 + s*6)    #The same code in the line 8
    a=a+1
print("\n")

#>>> H code <<<
h=0
while h<3:
    print("*"*6 + " "*8 + "*"*6)
    h=h+1
while h<5:
    print("*"*20)
    h=h+1
while h<8:
    print("*"*6 + " "*8 + "*"*6)  #The same code in the line 21
    h=h+1
print("\n")

#>>> M code <<<
m=6       #The counter of stars
p=14      #The counter of spaces

for ctr in range(8):      #Stage1 of the M
    print(s*m + c*p + s*m)
    m=m+1
    p=p-2
m=10    #The counter of stars
p=3   #The counter of spaces
for ctr in range(4):        #Stage 2 of the M
    print(s*5 + c*p +s*m +c*p +s*5)
    p=p+1
    m=m-2
m=0
while m<3:   #Stage 3 of the M
    print(s*5 + c*16 +s*5)
    m=m+1
print("\n")

#>>> A2 code <<< (The same code of A1)
a=0
print(c*2+s*16+c*2)
while a<2:
    print(s*20)
    a=a+1
while a<5:
    print(s*6 + c*8 + s*6)
    a=a+1
while a<7:
    print(s*20)  #The same code in the line 5
    a=a+1
while a<10:
    print(s*6 + c*8 + s*6)    #The same code in the line 8
    a=a+1
print("\n")
#>>> D code <<<
d=3    #The counter of stars
p=12   #The counter of spaces
print ("  " + "*"*16)
print ("*"*20)
for ctr in range(4):      #The first stage of D
    print(s*6 + c*p +s*d)
    p=p+1
    d=d+1
    if d==5 and p==20:
        break
for ctr in range (2):  #The second stage of D
    print(s*6 +c*p +s*5)
d = 6  # The counter of stars
p = 15  # The counter of spaces
for ctr in range(4): #The third stage of D
    print(s*6 + c*p + s*d)
    d=d-1
    p=p-1
print ("*"*20)
#Thanks for watching