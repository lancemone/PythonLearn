#if语句用来检验一个条件， 如果 条件为真，我们运行一块语句（称为 if-块 ）， 否则 我们处理另外一块语句（称为 else-块 ）。 else 从句是可选的。

#猜数字

num = 23
guess = int(input('Enter your guess number :'))

if guess == num:
    print('Congratulations, you guessed it')
    print('Done')

elif guess < num:
    print('No, it is a little higher than that')

else:
    print('No, it is a little lower than that')


