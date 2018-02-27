def get_birthday(id, get_age=True):  # 定义函数名称并设定参数,get_age为关键字参数,默认值为False
    if get_age:  # 对参数进行判断
        return 2018 - int(id[6:10])
    else:
        year = id[6:10]
        month = id[10:12]
        day = id[12:14]
        return year, month, day


bir = get_birthday('181281199812142412', True)
bir1 = get_birthday('181281199812142412', False)
bir2 = get_birthday('123718237912461123')
print(bir)
print(bir1)
print(bir2)
