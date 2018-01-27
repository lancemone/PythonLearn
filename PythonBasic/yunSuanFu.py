#运算符及使用说明


# 1、 +  两个对象相加
print(3+5)
print("我爱你"+"ლ(′◉❥◉｀ლ)")

# 2、-  得到负数或者两数相减
print(-5.3,'\n', 5-3)

# 3、 *   两数相乘或者返回一个重复若干次的字符串
print(3*5, '\n', 'ha'*3)

# 4、**   返回x的y次幂
print(3**4)

# 5、 / 除  // 取整除，返回商的整数部分    % 取模，返回余数
print(8/3, 8//3, 8%3)

'''
# 6、按位运算,按位运算就把数字转换为机器语言——二进制的数字来运算的一种运算形式.Python中的按位运算符有：左移运算符（<<），右移运算符（>>）,按位与（&），按位或（|），按位翻转（～）。这些运算符中只有按位翻转运算符是单目运算符，其他的都是双目运算符。
#    <<  左移，把一个数的比特向左移一定数目（每个数在内存中都表示为比特或二进制数字，即0和1）。2 << 2得到8。——2按比特表示为10
#    >>  右移，把一个数的比特向右移一定数目。11 >> 1得到5。——11按比特表示为1011，向右移动1比特后得到101，即十进制的5。
#    &   按位与，3&5  解法：3的二进制补码是 11,  5的是101, 3&5也就是011&101,先看百位(其实不是百位,这样做只是便于理解) 一个0一个1,根据(1&1=1，1&0=0，0&0=0，0&1=0)可知百位应该是1,同样十位上的数字1&0=0,个位上的数字1&1=1,因此最后的结果是1.
#    |   按位或
#    ^   按位异或，方法:  对位相加,特别要注意的是不进位.
#    ~   按位翻转，将二进制数+1之后乘以-1,x的按位翻转是-(x+1) .   '''
print(2 << 2, 11 >> 1)

'''
 # 7、布尔符号
 # not 布尔“非”,如果x为True，返回False。如果x为False，它返回True。
 # and 布尔“与”,如果x为False，x and y返回False，否则它返回y的计算值。
 # or 布尔“或”,如果x是True，它返回True，否则它返回y的计算值。
'''

#8、 表达式
length = 5
breadth = 10
area = length * breadth
print('The area is', area)

