import html
def avg(first, *rest):  # 使用一个*参数让一个函数接受任意数量的位置参数
    return (first + sum(rest)) / (1 + len(rest))  # rest是由所有其他位置参数组成的元组。然后我们在代码中把它当成了一个序列来进行后续的计算。


print(avg(1, 2))  # 1.5
print(avg(1, 2, 3, 4))  # 2.5


def make_element(name, value, **attrs):
    keyvals = ['%s = "%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element


print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))
