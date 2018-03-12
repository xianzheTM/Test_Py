temp=input('输入你的原价（大于1000参与活动）：')
while temp != 'exit':
    i = int(temp)
    if 1000 <= i < 2000:
        i = i * 0.95
        print('你的优惠价格为%d' % i)
    elif 2000 <= i < 3000:
        i = i * 0.9
        print('你的优惠价格为%d' % i)
    elif 3000 <= i < 5000:
        i = i * 0.85
        print('你的优惠价格为%d' % i)
    else:
        i = i * 0.8
        print('你的优惠价格为%d' % i)
   

else:
    print('退出')
