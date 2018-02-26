d2 = {'yue': ['月', '约', '悦'], 'ri': '日', 'yi': 1}  # 创建字典
d3 = dict(小楼='xiaolou', 小美='beautiful')  # 通过可变参数创建对象

d3['小明'] = 'xiaoming'  # 添加新元素到字典
print(d3)
d3['小楼'] = 'xiaol'  # 修改已存在键对应值
print(d3)
d3['小樱'] = 'xiao', 'ying'  # 添加值为元组的新元素到字典
print(d3)
print(d3.setdefault('小楼', 'xiaolou'))  # 字典中存在相应的键，则返回该键对应的值
print(d3.setdefault('小井', 'xiaojing'))
d3.update(樱井='yingjing', 明步='mingbu')  # 通过可变参数添加多个元素
print(d3)
d3.update((('樱井', '好白'), ('明步', '好大')))  # 通过元组添加多个元素
print(d3)
d3.update([('樱井', '好白'), ('明步', '好大')])  # 通过列表添加多个元素
print(d3)
d3.update({'樱井': '好白', '明步': '好大'})  # 通过字典添加多个元素
print(d3)
d3.update(d2)  # 合并字典元素
print(d3)
del d3['樱井']  # 删除元素
print(d3)
print(d3.pop('小楼'))
print(d3.pop('樱井', '好爽'))  # 显示输出结果为：好爽
print(d3)
