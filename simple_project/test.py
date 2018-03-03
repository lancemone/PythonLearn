def creat_name_lst(name_lst, *names):
    print(type(names))  # 显示输出参数names的数据类型，结果为：<class 'tuple'>
    if names is not None:
        for name in names:
            name_lst.append(name)


lst = []
creat_name_lst(lst, 1, 2, 3, 4, 5, 6)
print(lst)
