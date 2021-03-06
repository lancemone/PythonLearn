# 正则表达式 （Regular Expression）是对字符串操作的一种逻辑公式，用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，用来表达对字符串的一种过滤逻辑。

'''正则表达式的特点：
具有很强的灵活性、逻辑性和功能性；
可以快速通过非常简单的方式达到字符串的复杂控制；
对于初学者比较晦涩难懂。'''

'''
一、匹配单个字符
\d：匹配单个数字
\D：匹配单个非数字
\w：匹配单个字母或数字或下划线
\W：匹配单个字母或数字或下划线以外的字符
\s：匹配单个不可见字符，例如：\w\s\-\s\d匹配a – 3。（匹配的是空格）
\S：匹配单个可见字符
.：匹配任意一个字符，例如\w.\d匹配a~3。
\.：匹配字符“.”


二、匹配多个字符
*：匹配任意数量字符


三、匹配范围
[xyz]：匹配xyz中任意一个字符
[^xyz]：匹配非xyz的字符
[x|y]：匹配其中任意一个字符
(xxx|yyy)：匹配其中任意一个字符串
[a-z]：匹配a-z的范围
[^a-z]：匹配a-z以外的范围


匹配数量
?：0-1个前方子表达式。例如\w?\d匹配a3和3。
+：数量大于0个前方子表达式。例如：/s+ 表示至少一个空格。
{n}：前方子表达式数量为n次。
{n,}：前方子表达式数量至少为n次。
{n,m}：前方子表达式数量至少为n次，最多为m次。


五、匹配首尾字符
^：匹配字符串起始单个字符，后方紧随首个字符或表达式。
$：匹配字符串末尾单个字符，前方紧随末尾字符或表达式。
\b：匹配单词边界，即字符串末尾字符串。例如：er\b匹配player。
\B：匹配非单词边界，即字符串末尾之前的字符串。例如：er\B匹配error。


六、特殊匹配

\：转义字符
\f：匹配一个换页符
\n：匹配一个换行符
\r：匹配一个回车符
\t：匹配一个制表符
\v：匹配一个垂直制表符


七、零宽度断言

零宽度断言是一种零宽度的匹配，它匹配到的内容不会保存到匹配结果中去，最终匹配结果只是一个位置。
它的作用是给指定位置添加一个限定条件，用来规定此位置之前或者之后的字符必须满足限定条件才能使正则中的字表达式匹配成功。

(?!表达式)：向后匹配一个字符，如果不是表达式对应的字符，则匹配成功。
(?=表达式)：向后匹配一个字符，如果是表达式对应的字符，则匹配成功。
(?<=表达式)：向前匹配一个字符，如果是表达式对应的字符，则匹配成功。
(?<!表达式)：向前匹配一个字符，如果不是表达式对应的字符，则匹配成功。
如果想获取到零宽度断言匹配成功的字符，需要在断言后方填写表示单个字符的表达式，例如：(?!,).表示字符不是“,”则获取。


等价字符：

?等价于匹配长度{0,1}
*等价于匹配长度{0,}
+等价于匹配长度{1,}
\d等价于[0-9]
\D等价于[^0-9]
\w等价于[A-Za-z_0-9]
\W等价于[^A-Za-z_0-9]


常用运算符与表达式： 

^：字符串开始
$：字符串结尾
()：域段/组（group），能够将匹配表达式的字符临时保存，并通过函数group(args)获取。
[]：包含,默认是一个字符长度
[^]：不包含,默认是一个字符长度
{n,m}：匹配长度
.：任何单个字符
|：或
\：转义
[A-Z]：26个大写字母
[a-z]：26个小写字母
[0-9]：0至9数字
[A-Za-z0-9]：26个大写字母、26个小写字母和0至9数字
,：分割，例如：[A,H,T,W] 包含字母A或H或T或W；[a,h,t,w] 包含字母a或h或t或w；[0,3,6,8] 包含数字0或3或6或8。


一般来说，通过给定一个正则表达式和一个字符串，我们可以达到以下目的：
判断给定的字符串是否符合正则表达式的过滤逻辑（即匹配）；
通过正则表达式，从给定的字符串中获取特定部分。

'''

# 通过正则表达式验证手机号码(首字符为1；第二位字符为3，4，5，7，8之一；其余九位为数字；号码长度为11位)

import re  # 导入正则表达式模块


def check_phone(phone):
    regular = '^1[3, 4, 5, 7, 8]\d(9)$'  # 定义正则表达式
    if re.match(regular, phone):  # 调用正则匹配函数进行匹配,在对正则表达式和字符串进行匹配的时候，\
        # 需要使用re模块中的match(pattern, string[, flags=0])函数, 参数pattern是正则表达式；参数string是字符串；参数flags是标志（忽略大小写或全局匹配等）。
        print('手机号格式正确')
    else:
        print('手机号格式错误')


check_phone('15111111111')  # 调用函数，显示输出结果为：手机号码格式正确！
check_phone('25111111111')  # 调用函数，显示输出结果为：手机号码格式错误！
check_phone('12111111111')  # 调用函数，显示输出结果为：手机号码格式错误！
check_phone('1511111111')  # 调用函数，显示输出结果为：手机号码格式错误！
check_phone('151111111111')  # 调用函数，显示输出结果为：手机号码格式错误！
check_phone('15a11111111')  # 调用函数，显示输出结果为：手机号码格式错误！


# 通过正则表达式获取身份证号码中出生日期
def get_birthday(card_id):  # 定义检查身份证号码的函数
    regular = '^\d{6}(\d{4})(\d{2})(\d{2})\d{3}[\d|X]$'  # 定义正则表达式并指定域段
    result = re.match(regular, card_id)  # 将匹配结果保存到变量
    if result:  # 如果匹配结果不为None
        return result.group(1, 2, 3)  # 获取匹配结果中的指定域段并返回结果


print(get_birthday('11011219990109633X'))  # 调用函数，显示输出结果为：('1999', '01', '09')

# 预编译
# 函数compile(pattern, flags)可以对正则表达式进行预编译并保存到变量中，通过变量调用match(string[, pos[, endpos]])函数即可进行匹配
regular = r'\d{3}'  # 创建正则表达式
c = re.compile(regular)  # 预编译正则表达式
print(c.match('adc123', 3))  # 显示输出结果为：<_sre.SRE_Match object; span=(3, 6), match='123'>
# 当进行预编译处理后，和指定字符串的匹配可以不是从起始位置开始，而是可以指定匹配的区间。


# 贪婪模式
# 贪婪模式会在整个表达式匹配成功的前提下，尽可能多的匹配，而非贪婪模式会在整个表达式匹配成功的前提下，尽可能少的匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())  # 结果为('102300', '') # 贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())  # 结果为('1023', '00') # 非贪婪匹配
# 第一个正则表达式中\d+为贪婪匹配，会导致0*无法匹配00。
# 第二个正则表达式中\d+?为非贪婪匹配， 0*不受影响可以正常匹配00。
# 贪婪模式的量词叫匹配优先量词，在这些匹配优先量词的后方后加上“?”，即变成非贪婪模式，叫做忽略优先量词

