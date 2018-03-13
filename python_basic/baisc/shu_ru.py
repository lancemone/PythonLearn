# 获取手动输入的内容，需要使用input()方法

id = input('please input your school number:')
print(id)

# 格式化  %操作符
id1 = input('please input your IDcard number:')
print('你的身份证号码是：' + id1)
print('你的出生日期是:%s' % id1[6:14])
print('你的出生日期是：%s年%s月%s日' % (id1[6:10], id1[10:12], id1[12:14]))

# format(args,kwargs)：对字符串进行格式化的函数；参数args表示可以输入多个参数（argument），参数间以逗号分隔；参数kwargs表示可以输入多个关键词参数，关键字函数的写法例如：age=’18’，age为关键字，’18’为这个关键字对应的值。

id2 = input('please input your IDcard number:')
print('birthday is {}-{}-{}'.format(id2[6:10], id2[10:12], id2[12:14]))
print('birthday is {1}-{0}-{2}'.format(id2[6:10], id2[10:12], id2[12:14]))
print('birthday is {year}-{month}-{day}'.format(id2[6:10], id2[10:12], id2[12:14]))

'''please input your IDcard number:2164129378614829
birthday is 9378-61-48
birthday is 61-9378-48
birthday is 9378-61-48'''
'''第1条：在字符串中我们嵌入了3对“{}”，并且在format函数的参数中写入了3个参数，程序按照参数从左至右的顺序将字符串进行了格式化。

第2条：在字符串中我们仍然嵌入了3对“{}”，但是每一对“{}”中都有一个数字，这些数字是从0开始递增的序号，“{0}”表示在该位置要显示从左至右第1个参数的内容，“{1}”表示在该位置要显示从左至右第2个参数的内容，以此类推。所以，在输入参数的时候，参数的顺序要与前面的序号相对应。

第3条：在字符串中我们也是嵌入了3对“{}”，这一次每一对“{}”中都有一个关键字，这些关键字与参数中的关键字相对应。例如，“{month}”表示在该位置要显示关键字参数中“month”后方的值，以此类推。'''

