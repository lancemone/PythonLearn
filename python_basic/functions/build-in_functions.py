# Python中的内置函数（Built-in Functions）
# Python3中所有的内置函数共68个。具体参考GitHub项目中document分支的文档
# 特别提示：如果参数带有[]，表示可以省略该参数；如果参数带有“=”，表示带有默认值；如果参数带有“*”，表示该参数填入多个。

'''
abs(x)：abs<绝对值函数>；参数x为整数或浮点数（小数），返回值为x的绝对值。

all(iterable)：all<全部>；参数iterable为可迭代对象，如果对象为空值或所有元素为True时，返回值为True。

any(iterable)：any<任何>；参数iterable为可迭代对象，如果对象为空值，返回值为False，任何元素为True时，返回值为True。

ascii(object)：ASCII<American Standard Code for Information Interchange,美国信息互换标准代码>；参数object为对象，与repr()函数相同，返回值为字符串方式表示的可打印对象。当遇到非ASCII码时，就会输出\x，\u或\U等字符来表示。

bin(x)：bin<二进制>；参数x为整数，返回值为二进制字符串，结果是一个有效的Python表达式。如果参数x不是一个Python的int对象，它定义了一个__index__()方法返回一个整数。

class bool([x])：bool<布尔>；返回值为布尔值，True 或 False。参数x通过使用标准的真值检测程序，如果x为假值或省略，则返回False；否则返回True。bool类是int子类，它不能进一步划分子类，并且仅具有False和True实例。

class bytearray([source[, encoding[, errors]]]) ：byte array<字节数组>；返回值为新的字节数组，一个整数值区间为0≤x＜256的可变序列。参数source可以为整数、字符串、可迭代对象，参数encoding为字符串（编码类型），参数errors为字符串。

class bytes([source[, encoding[, errors]]]) ：bytes<字节>；返回值为新的字节对象，一个整数值区间为0≤x＜256的不可变序列。其它与bytearray函数相同。

callable(object)：callable<可调用>；如果object参数是可以调用的对象，返回值为True；否则返回值为False。对象可以调用并不表示调用该对象时一定会成功，但不可调用的对象去调用时一定不会成功。注意，类可以调用（调用类将返回一个新实例）；实例的调用取决于重载是否包含__call__()方法。

chr(i)：chr<Char/Code,字符/编码>返回参数i表示的字符，参数i为Unicode编码序号。例如，CHR（97）返回字符“A”，而CHR（8364）返回字符串的“€”。ord()函数功能与之相反。参数的有效范围是从0到1114111（16进制：0x10FFFF），如果超出此范围则会抛出ValueError（值错误）异常。

classmethod(function)：class，method<类，方法>；为函数返回一个类的方法。类的方法第一个参数需要指明类，就像类中函数，第一个参数是指明类实例。

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1) ：compile<编译>；将源编译成编码或AST（抽象语法树）对象。编码对象可以通过exec()函数或 eval()函数执行。参数source可以是普通的字符串，字节字符串，或AST对象；参数filename是字符串的文件对象；参数mode是用来指定源码的类型；参数flags和dont_inherit是用来控制编译源码时的标志；参数optimize是用来指定编译器进行优化的等级。

class complex([real[, imag]]) ：complex<复数>；返回值为复数，可以通过real + imag*1j 的方式创建，也可以通过字符串或数字转换而成。如果第1个参数是字符串，将被解释为复数，并且不得写入第2个参数；第2个参数不能是字符串；每个参数可以是任何数字类型（包括复数）。如果省略imag参数，则该参数默认值为0，这个函数就相当于int()函数或float()函数。如果省略所有参数，则返回0j。

delattr(object, name)：delattr<delete/attribute，删除/属性>；此函数相对于setattr()函数，用于删除对象的属性。参数object为对象；参数name为字符串，而且必须是对象的属性。例如：delattr(x, ‘foobar’) 等同于del x.foobar。

class dict(**kwarg)/class dict(mapping, **kwarg) /class dict(mapping, **kwarg) ：dict<字典>；此函数用于创建一个新字典。具体参考：http://www.charmpy.com/225.html

dir([object])：dir<目录>；参数object为对象；如果省略参数，返回当前作用域范围内的属性列表；如果输入参数，则试图返回该对象的有效属性列表。

divmod(a, b) ：div<division，除法> ，mod<modulo，模>；参数a和b为数字（非复数），返回值为商和余数组成的元组；如果两个参数均为整数，则采用整数除法，结果等同于（a//b, a % b)。如果任一参数是浮点小数，相当于（math.floor(a/b), a%b)。

enumerate(iterable, start=0) ：enumerate<枚举>；返回值为枚举对象；参数iterable为可迭代对象，例如列表、数组、字典等对象；参数start是枚举的起始值，默认为0。

eval(expression, globals=None, locals=None) ：eval<evaluate，求值>；参数expression为表达式字符串；函数可以动态地执行参数expression的表达式字符串。参数globals是全局命名空间，可以指定执行表达式时的全局作用域的范围；参数locals是局部作用域命名空间，是用来指定执行表达式时访问的局部命名空间。

exec(object[, globals[, locals]])：exec<execute，执行>；该函数支持Python代码的动态执行；参数object为对象，必须是一个字符串或代码对象。如果是字符串，则将字符串解析为一组Python语句，然后执行这些语句（除非出现语法错误）；如果是代码对象，它则只是执行。参数globals为全局命名空间，用来指定执行语句时可以访问的全局命名空间；参数locals为局部命名空间，用来指定执行语句时可以访问的局部作用域的命名空间。注意，此函数没有返回值，即便字符串或代码对象中包含返回值语句，例如return或yield语句。

filter(function, iterable) ：filter<过滤>；参数function为函数，参数iterable为可迭代对象；函数遍历参数iterable所有元素，并将每个元素通过参数function进行判断，判断为true的元素保留，否则跳过，最终返回一个由保留的元素组成的可迭代对象。参数iterable可以是序列，可迭代对象，或者是支持迭代的容器。如果省略参数function，所有元素将不被保留。

class float([x]) ：float<浮动>；参数x为整数或字符串；函数将参数转换为浮点数。

format(value[, format_spec]) ：format<格式>；参数value为值；此函数将参数value通过format_spec的格式来格式化，并根据参数value的类型进行format_spec解释。

class frozenset([iterable]) ：frozen，set<冻结,集合> ；参数iterable为可迭代对象，例如列表、字典、元组等；返回值是一个新的冻结集合对象，可从迭代对象中获取任意元素。frozenset是一个内置的类。冻结集合不可添加或删除任何集合里的元素。

getattr(object, name[, default]) ：getattr<get，attribute/获取，属性>；返回值为指定对象的属性值。参数object为对象；参数name为属性名称，必须是字符串；参数default为默认返回值。如果参数name是参数object的属性名称，返回结果是该属性的值。例如，getattr(x, ‘foobar’) 等同于x.foobar。如果指定的属性不存在，返回值参数default的值，否则抛出属性异常AttributeError。

globals()：返回值为当前全局符号表的字典，并且始终是当前模块的字典（在函数或方法中定义的模块，而不是调用的模块）。通过这个字典，能够查询可访问的模块、函数以及变量。

hasattr(object, name) ：hasattr<has，attribute/包含，属性>；参数object为对象；参数name为属性名称的字符串；如果参数name是对象object的属性名称，则返回值为True；否则，返回值为False。

hash(object) ：hash<hash，哈希>；参数object为对象；返回值为对象object的哈希值。返回的哈希值是一个整数；可用于快速查询字典的键值。如果对象object是数字类型，相同的数字具有相同的哈希值，例如1和1.0的哈希值相同。

help([object])：help<帮助>；参数object为对象；此函数能够调用内置的帮助系统（用于交互模式）。如果省略参数，则会在解释器控制台启动交互式帮助系统。如果参数object是一个字符串，则会查找与之相同的模块，函数，类，方法，关键字的名称，或者是文档标题，并在控制台显示输出帮助页。如果参数object是任何其他类型的对象，则生成该对象的帮助页面。

hex(x)：hex<十六进制>；参数x为整数；此函数能够将一个整数转换为一个前缀为“0x”的小写十六进制字符串。

id(object)：id<identify，标识符>返回值是对象object的标识符。这个标识符是一个整数，在对象object同一生命周期中保持唯一且不会改变。在不重叠的生命周期中，两个对象可以具有相同的标识符。

input([prompt]) ：input<输入>；参数prompt为提示字符串；如果写入参数prompt，则会被标准输出且没有换行，然后，函数会读取输入的内容，将其转换为字符串（并去除结尾换行符），返回结果。

class int(x=0)/class int(x, base=10) ：int<integer，整数>；参数x为数字或字符串，函数将参数x转换为整数，并返回结果。如果省略参数，则返回值为0。对于浮点数，会下取整。参数base为进制，如果写入该参数，则x必须为字符串，例如int(‘1c’,base=16),返回值为28。

isinstance(object, classinfo) ：isinstance<is，instance/是，实例>；参数object为对象；参数classinfo为类型；此函数能够判断参数object对象实例是否是参数classinfo的实例，如果是，返回值为True；否则，返回值为False。

issubclass(cls, classinfo) ：issubclass<is，subclass/是，子类>；参数cls为类；参数classinfo为类型；此函数能够判断参数cls是否是参数classinfo的子类，如果是，返回值为True；否则，返回值为False。

iter(object[, sentinel]) ：iter<iterator ,迭代器>；参数object为对象；参数sentinel为哨兵；第1个参数如何解释，取决于第2个参数；第2个参数省略时，对象必须是一个支持迭代（定义了__iter__()函数）或者序列（定义了__getitem__()函数）的容器，否则，会抛出类型错误TypeError异常。第2个参数写入时，参数object是一个可调用的对象(定义了__next__()函数)，当枚举到的值等于哨兵时，就会抛出停止迭代异常StopIteration。

len(s)：len<length，长度>；返回值为参数s的长度（项的数量）。参数s可以是一个序列（如string、bytes、tuple、list或range）或集合（例如dict、set或frozen set）。

class list([iterable]) ：list<列表>；参数iterable为可迭代对象，此函数返回值是一个列表。

locals()：此函数更新并返回当前系统可用的局部符号表，返回结果是一个字典。

map(function, iterable, …) ：map<>；参数function为函数，参数iterable为可迭代对象；此函数是把参数对象function作为函数，参数iterable对象的每一项作为参数，通过计算输出子迭代对象。如果参数function允许输入多参数，则可以输入多个iterable参数。当有多个iterable参数，运行计算次数以项数量最少的迭代对象为准。

max(iterable, *[, key, default])/max(arg1, arg2, *args[, key]) ：max<最大值>；参数iterable为可迭代对象，参数key为函数，参数default为默认值，参数arg（argument）为数值；此函数能够返回一个迭代对象中最大的项或者多个参数中的最大值；当输入参数key时，会依据key的函数进行计算，对所有计算结果取最大一项；参数default为函数不能返回结果时，返回的的默认值。

memoryview(obj)：memoryview<memory，view/内存，查看>参数obj（object）为对象；此函数能够返回参数obj的内存查看对象。

min(iterable, *[, key, default])/min(arg1, arg2, *args[, key]) ：min<最小值>；此函数能够返回一个迭代对象中最小的项或者多个参数中的最小值；参数部分与max()函数相同。

next(iterator[, default]) ：next<下一个>；参数iterable为可迭代对象；参数default为默认值；此函数的返回值为参数iterable中下一个元素的值。如果输入参数default，当下一个元素不存在时，返回default参数的值，否则抛出停止迭代异常StopIteration。

class object：object<对象>；此函数返回一个新的无特征的对象。object类是Python中所有类的基类，它包含Python中所有实例共有的方法；如果定义一个类时没有指定继承的类，则默认继承object类。这个函数不接受任何参数。

oct(x)：oct<octal，八进制>参数x为整数；此函数能够将一个整数转换为一个八进制字符串，结果是一个有效的Python表达式。如果参数x不是一个Python的int（integer，整数）对象，它必须定义一个返回整数的index()方法。

open(file, mode=’r’, buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) ：open<打开>；此函数能够打开一个文件并返回文件对象。如果文件不能打开，则抛出操作系统异常OSError（Operating System Error）。
参数file是一个类似路径的对象，可以是字符串或数组表示的文件名称，文件名称是要打开文件的路径(绝对路径或者相对路径)。
参数mode是指明打开文件的模式。
‘r’：只读模式打开文件，不可写入，此为参数默认值。
‘w’：写入模式打开文件，并且清空打开的文件。
‘x’：独占模式打开文件，如果文件已经打开，则会打开失败。
‘a’：写入模式打开文件，如果文件存在，则在文件末尾追加内容。
‘b’：二进制模式，例如读取声音、图像文件。
‘t’：文本模式，此为参数默认值。
‘+’：打开文件进行更新，可以读取或写入。
参数buffering为可选参数，用于缓冲区的策略选择。
参数encoding为文件编码，仅适用于文本文件。
参数errors为编解码错误时进行的处理，但不能在二进制模式下使用。
参数newline为文本模式指定下一行的结束符。可以是None，”，\n，\r，\r\n等。
参数closefd用于传入的文件句柄，当退出文件时，不关闭文件句柄。
参数opener用于实现自己定义打开文件方式。

ord(c)：ord<order，次序>；参数c为表示Unicode字符的字符串，返回值为表示该字符的Unicode代码点的整数。例如，ord(‘a’)返回值为整数97，ord(‘€’)(欧元符号)返回值为整数8364。此函数与chr()函数功能相反。

pow(x, y[, z])：pow<power，幂>参数x、y、z均为数值；参数z省略时，函数返回值为x的y次方；参数z输入时，返回值为x的y次方模z后的余数，即pow(x,y) %z；pow(x, y)等同于x**y。

print(*objects, sep=’ ‘, end=’\n’, file=sys.stdout, flush=False)：print<打印>；参数object为对象；参数sep是分隔符，用于对多个输出的参数进行分隔，默认为一个空格；参数end是输出结束时的字符，默认是换行符“\n”；参数file是指定流输出到的文件，默认是系统标准输出sys.stdout；参数flush是立即把内容输出到流文件，不作缓冲。此函数能够将对象输出文本流文件中，以参数sep进行分隔，以参数end为结束符。

class property(fget=None, fset=None, fdel=None, doc=None)：property<属性>；此函数用于设置类成员的属性；参数fget是获取属性值的函数；参数fset是用于设置属性值的函数；参数fdel是删除一个属性值的函数；参数doc是创建属性的文档字符串。

range(stop)/range(start, stop[, step])：range<范围>；range()实际上不是一个函数，而是一个不可变的序列；参数stop是序列的终止数字，仅有此参数时，序列从0开始；参数start是序列的起始数字；参数step是步长，即前后两个数字的差值；这三个参数均为整数。

repr(object)：repr<表示>；参数object为对象；此函数能够返回参数对象object的说明字符串。

reversed(seq)：reversed<反转>；参数seq为序列；此函数返回结果为参数序列seq反向的可迭代对象。

round(number[, ndigits])：round<四舍五入>；参数number为数字；参数ndigits<n,digits/n个,数字>为保留的小数位数；此函数用于对浮点小数进行指定保留位数的四舍五入计算。

class set([iterable])：set<集合>；参数iterable为可迭代对象；此函数能够从可迭代对象生成集合；集合是Python的一个内置类。

setattr(object, name, value)：<set，attribute/设置，属性>；此函数对应函数getattr()；参数object为对象；参数name为属性名称，必须是字符串；参数value为属性的值；此函数能够设置或者增加参数对象object的属性名称（参数name），并设置相应的值（参数value）。

class slice(stop)/class slice(start, stop[, step])：slice<切片>；参数stop为切片范围的终止位置；参数start为切片范围的起始位置；参数step为步长；此函数返回一个切片范围的对象，作为切片操作中的参数。

sorted(iterable[, key][, reverse])：sorted<排序>；参数iterable为可迭代对象；参数key为键的比较函数；参数reverse为布尔值，用于反向排序设置；此函数能够将参数对象iterable进行排序，返回一个新的已排序的列表。

staticmethod(function)：staticmethod<static，method/静态，方法>；参数function为函数；此函数能够返回一个静态函数的对象，主要用作静态函数的修饰符。静态函数可以直接通过类的命名空间调用，而无需将类进行实例化；并且静态函数也可以通过类的实例进行调用。

class str(object=”)/class str(object=b”, encoding=’utf-8′, errors=’strict’)：str<string，字符串>；参数encoding为编码类型；errors为错误处理方式；此函数用于将参数对象object转换为字符串对象。

sum (iterable[, start])：sum<总计>；参数iterable为可迭代对象；参数start为求和的初始值；此函数能够对参数对象iterable进行求和；参数start填入时，会将求和结果再加上参数start的数值。

super([type[, object-or-type]])：super<超级>；参数type为类型；参数object-or-type为对象或类型；此函数返回一个代理类对象，用于访问父类或同级类。

tuple([iterable])：tuple<元组>；参数iterable为可迭代对象；此函数能够从参数对象iterable生成一个元组对象。

class type(object) /class type(name, bases, dict)：type<类型>；参数object为对象；参数name为类的名称；参数bases为基类的元组；参数dict为类中定义的命名空间；此函数只填入一个参数时，返回结果为参数对象object的类型；当填入3个参数时，返回一个新的类型的对象。

vars([object])：vars<variables，变量>；参数object为对象；此函数返回一个包含参数对象object属性与属性值的字典对象，参数object可以是模块、类、实例或者其它对象。如果省略参数，相当于函数locals()。

zip(*iterables)：zip<拉链>；参数iterables为多个可迭代对象；此函数能够从每个可迭代对象中逐一获取元素创建一个新的可迭代对象。如果在参数iterables前添加“*”，则会进行逆向处理，进行分离。

__import__(name, globals=None, locals=None, fromlist=(), level=0)：import<导入>；此函数由导入模块的语句调用，以实现动态地加载模块。参数name为模块名称；参数globals为全局，参数locals为局部，指定这两个参数是用于判定如何在包的上下文中解释名称；参数fromlist为对象或子模块的名称，这些名称应该能够从参数name指定的模块中导入；参数level为级别，指定使用绝对或相对导入，默认值为0，即绝对导入。


'''
