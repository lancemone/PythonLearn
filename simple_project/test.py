class Shielding:  # 创建屏蔽类
    def __init__(self):
        self.words = []  # 屏蔽内容列表
        self.symbol = ''  # 屏蔽后显示的符号

    def change(self, sentence):
        string = sentence
        for word in self.words:
            if word in sentence:
                string = string.replace(word, self.symbol * len(word))
        return string


class ShieldingWords(Shielding):
    def __init__(self):
        self.words = ['银行', '账号', '密码']
        self.symbol = '*'


class ShieldingSymbols(Shielding):
    def __init__(self):
        self.words = '#'
        self.symbol = '@'

    def message(self):
        print('禁止在邮箱地址中使用%s,已使用%s代替' % (self.words, self.symbol))


s = Shielding()
print(s.change('你银行的账号和密码是什么？'))
w = ShieldingWords()
print(w.change('你银行的账号和密码是什么？'))
c = ShieldingSymbols()
print(c.change('我的邮箱是4907442#qq.com'))
c.message()
