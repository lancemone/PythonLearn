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

'''条件表达式通常包括以下关系运算符：

==：表示等于，用于判断运算符两侧的内容是否相同。

!=：表示不等于，用于判断运算符两侧的内容是否不相同。

>：表示大于，用于判断运算符左侧内容是否大于右侧内容。

>=：表示大于等于，用于判断运算符左侧内容是否大于等于右侧内容。

<：表示小于，用于判断运算符左侧内容是否小于右侧内容。

<=：表示小于等于，用于判断运算符左侧内容是否小于等于右侧内容。

is：表示是，用于判断运算符左侧内容和右侧内容是否同一对象。

is not：表示不是，用于判断运算符左侧内容和右侧内容是否非同一对象。

in：表示被包含，用于判断运算符左侧内容是否被右侧内容所包含。

not in：表示不被包含，用于判断运算符左侧内容是否不被右侧内容所包含。

除了以上的关系型运算符，还有以下这些逻辑运算符：

and：表示并且。

or：表示或者。

not：表示不是。

这些逻辑运算符能够将多个条件表达式连接到一起，形成更复杂的条件表达式'''
