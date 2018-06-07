import os


# 创建一个能够遍历当前目录下所有含有特定关键字的目录和文件并返回相对路径

# 定义一个方法
def search_file(dir, key_word):
    if key_word in dir:  # 判断路径中是否包含关键字
        print(os.path.relpath(dir))
    if os.path.isfile(dir):  # 判断路径是否为文件，若为文件则停止遍历
        return

    for dire in os.listdir(dir):  # 遍历目录下的子目录
        search_file(os.path.join(dir, dire), key_word)


pwd = os.path.abspath('..')
search_file(pwd, 'basic')
