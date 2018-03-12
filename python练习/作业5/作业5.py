#A,B,C分别表示大于零，小于零，等于零。
'''
import math
def A():
    x1=(-b+math.sqrt(b**b-4*a*c))/2*a
    x1=(-b-math.sqrt(b**b-4*a*c))/2*a
    print(x1,x2)

def B():
    x=-b/(2*a)
    print(x)

def C():
    str1="无解"
    print(str1)


def result(a,b,c):
    if b**b-4*a*c>0:
        A()
    elif b**b-4*a*c==0:
        B()
    else:
        C()


print("***************求一元二次方程******************")
a=int(input("请输入系数a:"))
b=int(input("请输入系数b:"))
c=int(input("请输入系数c:"))
result(a,b,c)
'''
def pyramid(n,str1):
    for i in range(1,n+1):
        print(' '*(n-(i-1))+str1*(2*i-1))

temp=input('请输入行数和所用字符:')
inlist=(temp.split())
nLine=int(inlist[0])
symbol=inlist[1]
pyramid(nLine,symbol)