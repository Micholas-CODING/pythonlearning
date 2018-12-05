a=input()
m=eval(a) #该行不能使用a[0:-1]会删除最后一位导致不正确
b=m*m
c=m*m*m
d=b*b
e=b*c
print(1,m,b,c,d,e)
