# 异常处理


# 零除异常
def get_error():
    print(1 / 0)


get_error()
'''
异常信息
Traceback (most recent call last): # 回溯（最近一次命令）
  File "D:/MyProject/case.py", line 5, in <module> # 文件"所在路径"，位于第2行，模块内
    get_error() # 出错的函数名称
  File "D:/MyProject/case.py", line 3, in get_error # 文件"所在路径"，位于第3行，get_error方法中
    print(1 / 0) # 出错的语句
ZeroDivisionError: division by zero # 0除错误：除数为0'''

# 内置异常
'''BaseException  # 所有异常的超类
 +-- SystemExit # 解释器退出错误
 +-- KeyboardInterrupt # 键盘中断执行错误
 +-- GeneratorExit # 生成器错误
 +-- Exception # 所有标准异常的超类
      +-- StopIteration # 停止迭代错误
      +-- StopAsyncIteration # 停止异步迭代错误
      +-- ArithmeticError # 计算错误
      |    +-- FloatingPointError # 浮点计算错误
      |    +-- OverflowError # 数值溢出错误
      |    +-- ZeroDivisionError  # 零除错误
      +-- AssertionError  # 断言失败错误
      +-- AttributeError # 特性错误
      +-- BufferError # 缓冲错误
      +-- EOFError # EOF标记错误
      +-- ImportError # 导入错误
           +-- ModuleNotFoundError # 模块不存在错误
      +-- LookupError # 查询错误
      |    +-- IndexError # 索引错误
      |    +-- KeyError # 键错误
      +-- MemoryError # 内存错误
      +-- NameError # 标识符错误
      |    +-- UnboundLocalError # 未绑定局部变量错误
      +-- OSError # 操作系统错误
      |    +-- BlockingIOError # 阻塞输入输出错误
      |    +-- ChildProcessError # 子进程错误
      |    +-- ConnectionError # 连接错误
      |    |    +-- BrokenPipeError # 管道中断错误
      |    |    +-- ConnectionAbortedError # 连接失败错误
      |    |    +-- ConnectionRefusedError # 连接拒绝错误
      |    |    +-- ConnectionResetError # 连接重置错误
      |    +-- FileExistsError # 文件已存在的错误
      |    +-- FileNotFoundError # 文件未发现的错误
      |    +-- InterruptedError # 中断错误
      |    +-- IsADirectoryError # 目标为目录的错误
      |    +-- NotADirectoryError # 目录不存在的错误
      |    +-- PermissionError # 许可错误
      |    +-- ProcessLookupError # 进程查询错误
      |    +-- TimeoutError # 超时错误
      +-- ReferenceError # 引用错误
      +-- RuntimeError # 运行时错误
      |    +-- NotImplementedError # 未执行错误
      |    +-- RecursionError # 递归错误
      +-- SyntaxError # 语法错误
      |    +-- IndentationError # 缩进错误
      |         +-- TabError # Tab错误
      +-- SystemError # 系统错误
      +-- TypeError # 类型错误
      +-- ValueError # 值错误
      |    +-- UnicodeError # Unicode相关错误
      |         +-- UnicodeDecodeError # Unicode解码错误
      |         +-- UnicodeEncodeError # Unicode编码错误
      |         +-- UnicodeTranslateError # Unicode转换错误
      +-- Warning # 警告的超类
           +-- DeprecationWarning # 关于弃用功能的警告
           +-- PendingDeprecationWarning # 关于功能将被弃用的警告
           +-- RuntimeWarning # 关于可疑运行时行为的警告
           +-- SyntaxWarning # 关于可疑语法的警告
           +-- UserWarning # 关于由用户代码生成的警告
           +-- FutureWarning # 关于构造将在语义上有改变的警告
           +-- ImportWarning # 关于模块导入中可能出现错误的警告
           +-- UnicodeWarning # 关于Unicode的警告
           +-- BytesWarning # 关于字节和字节数组的警告
           +-- ResourceWarning # 关于资源使用的警告'''

# 自定义异常信息：引发异常：raise 语句
num1 = input('被除数')
num2 = input('除数')
if int(num2) == 0:
    raise ZeroDivisionError('除数不能为0')
# 捕捉异常：try/except 语句
while True:
    try:
        num11 = input('被除数')
        num22 = input('除数')
        print('result', num11 / num22)
    except ZeroDivisionError:
        print('除数不能为0')
        break
    except ValueError:
        print('数值错误：必须输入数字！')
    # 可以通过except语句捕捉多个异常，然后进行相同的处理
    # except (ZeroDivisionError, ValueError):
    # print('错误提示：请输入正确的数值！')
    # break
    # except (ZeroDivisionError, ValueError):
    # raise
    # 不让程序终止，也显示异常信息.可以把捕捉到的异常通过as关键字存入变量，然后显示输出这个变量。
    # except (ZeroDivisionError, ValueError) as recode:
    #   print(recode)
    # 有的时候，我们不知道都会发生什么异常，可以在except语句后方什么都不添加。
    # except:
    #   print('unknow error')
    # 用标准异常的超类帮我们获取所有的异常
    except Exception as e:
        print(e)

# 一旦输入错误，我们提示用户，并且重新获取输入，直到输入正确，给出计算结果
while True:
    try:
        num1 = int(input('请输入被除数：'))
        num2 = int(input('请输入除数：'))
        print('计算结果为：', num1 / num2)
    except Exception as e:
        print(e)
    else:
        break

# 异常收尾：finally语句：不管程序有没有正确执行，我们都想提示用户当前程序进行了一次计算。
count = 0
while True:
    try:
        num1 = int(input('请输入被除数：'))
        num2 = int(input('请输入除数：'))
        print('计算结果为：', num1 / num2)

    except Exception as e:
        print(e)
    else:
        break
    finally:
        count += 1
        print('第%d次计算完毕！' % count)
