'''
1．编写程序，计算下列公式中s的值（n是运行程序时输入的一个正整数）。
s =1 + (1 + 2) + (1 + 2 + 3) + … + (1 + 2 + 3 + … + n)
s =12+ 22 + 32 + … + (10×n+2)
s =1×2-2×3+3×4-4×5+ … +(-1) (n-1) ×n×(n+1)
'''
n = int(input("输入一个整数："))
s1=0
for m in range(1,n+1):
    for n in range(1,m+1):
        s1=s1+n
print(s1)

s2=0
for i in range(1,n+1):
    s2=s2+(i*10+2)
print(s2)

s3=0
for j in range(1,n+1):
    s3=s3+((-1)**(j-1)*j*(j+1))
print(s3)

#2．输入某年某月某日，判断这一天是这一年的第几天？
dat = input('请输入某年某月某日，格式为 yyyy-mm-dd ：')
y = int(dat[0:4])  #获取年份
m = int(dat[5:7])  #获取月份
d = int(dat[8:])  #获取日

ly = False

if y%100 == 0:  #若年份能被100整除
    if y%400 == 0:  #且能被400整除
        ly = True  #则是闰年
    else:
        ly = False
elif y%4 == 0:  #其它情况下，若能被4整除
    ly = True  #则为闰年
else:
    ly = False

if ly == True:  #若为闰年，则2月份有29天
    ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0
for i in range(1, 13):  #从1到12逐一判断，以确定月份
    if i == m:
        for j in range(i-1):  #确定月份i之后，则将ms列表中的前i-1项相加
            days += ms[j]
        print('%s是该年份的第%s天。' % (dat, (days + d))) #最后再加上“日”，即是答案



'''
import datetime

y = int(input('请输入4位数字的年份：'))  #获取年份
m = int(input('请输入月份：'))  #获取月份
d = int(input('请输入是哪一天：'))  #获取“日”

targetDay = datetime.date(y, m, d)  #将输入的日期格式化成标准的日期
dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  #减去上一年最后一天
print('%s是%s年的第%s天。'% (targetDay, y, dayCount.days))
'''

#3．输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

Str1 = input('请输入一串字符:')

str_num = 0
spac_num = 0
figue_num = 0

for strs in Str1:
    if strs.isalpha():
        str_num +=1
    elif strs.isdigit():
        figue_num +=1
    elif strs == ' ':
        spac_num +=1
    else:
        pass
print ('英文字母有：%d' %str_num)
print ('数字有：%d'%figue_num)
print ('空格有：%d'%spac_num)








'''
#第一题第一问第一种：
print( "输入一个整数，程序可以自动计算以下结果：\n 类似：1 + (1 + 2) + (1 + 2 + 3) + … + (1 + 2 + 3 + … + n)="  )

n = int(input("输入一个整数："))

def add_num(n):
  result = ''
  for i in range(1,n+1):
    each = '('+'+'.join(map(str,list(range(1,i+1))))+')' if i>1 else '1'
    result += each +'+'
  result = result[:-1]
  print(result+'='+str(eval(result)))



#第一题第一问第二种：
print( "输入一个整数，程序可以自动计算以下结果：\n 类似：1 + (1 + 2) + (1 + 2 + 3) + … + (1 + 2 + 3 + … + n)="  )

n = int(input("输入一个整数："))

if n == 1:
    str2 = '1'
    sum2 = 1
else:
    sum2 = 1
    str2 = "1"
    for j in range(2, n+1):
        str2 = str2 + ' + ('
        sum1 = 0
        str1 = ""
        for i in range(1,j+1):
            sum1 = sum1 + i          #累加和
            str1 = str1 + str(i)     #输出结果控制，形式类似：1+2+3+4+5+=15
            if i != j:               #控制n后面那个+号
                str1 = str1 + "+"
        sum2 = sum2 + sum1
        str2 = str2 + str1 + ')'

print (str2,"=",sum2)

#第一题第一问第三种：
print("请输入一个整数n，程序自动计算出1到n的所有整数循环的和，\n类似：1+(1+2)+(1+2+3)+... = ")
n = input("n = ")
print()

sum0 = 0
lst2 = []

for j in range(1,int(n)+1):
    lst1 = []
    sum1 = 0
    for i in range(1,j+1):
        sum1 += i
        lst1.append(str(i))

    sum0 += sum1
    if len(lst1) == 1:
        str1 = "+".join(lst1)
    else:
        str1 = "("+"+".join(lst1)+")"
    lst2.append(str1)

print("+".join(lst2),"=",sum0)



#第一题第一问第四种：
print( "输入一个整数，程序可以自动计算出1到这个整数的所有整数的和，\n类似：1+(1+2)+(1+2+3)+...+(1+2+3+...+n)="  )
print
n = int(input("输入一个整数："))

sumx=0;
str1=''
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j==1 and i==1):
          str1=str(j)
        else:
            if(j==1):
                str1=str1 +'+('+str(j)
            elif (j==i):
                str1=str1 +'+'+ str(j)+')'
            else:
                str1=str1+'+'+str(j)
    sumx=sumx+sum([k for k in range(1,i+1)])
print(str1+' =',sumx)
'''
