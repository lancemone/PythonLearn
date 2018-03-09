def synthesis():
    count = int(input('请放入宝石:'))
    while True:
        if count < 3:
            count += int(input('宝石太少，请在放入一些宝石：'))
        else:
            break

    def execute():
        result = count // 3  # 调用外部变量进行整除运算
        print('您放入了%s颗宝石，合成了%s颗高级宝石' % (count, result))

    return execute()


exe = synthesis()
print('------------------开始合成------------------')
exe  # 执行闭包内容
