import wx

# 创建应用和框架
cal = wx.App()
win = wx.Frame(None, id=-1, title='计算器', size=(400, 370))

# 添加面板
pan = wx.Panel(win)

# 创建控件
1
_btn = wx.Button(pan, label='1', pos=(0, 120), size=(80, 40))
2
_btn = wx.Button(pan, label='2', pos=(0, 120), size=(80, 40))
3
_btn = wx.Button(pan, label='3', pos=(0, 0), size=(80, 40))
4
_btn = wx.Button(pan, label='4', pos=(0, 0), size=(80, 40))
5
_btn = wx.Button(pan, label='5', pos=(0, 0), size=(80, 40))
6
_btn = wx.Button(pan, label='6', pos=(0, 0), size=(80, 40))
7
_btn = wx.Button(pan, label='7', pos=(0, 0), size=(80, 40))
8
_btn = wx.Button(pan, label='8', pos=(0, 0), size=(80, 40))
9
_btn = wx.Button(pan, label='9', pos=(0, 0), size=(80, 40))
0
_btn = wx.Button(pan, label='0', pos=(0, 0), size=(80, 40))
cle_btn = wx.Button(pan, label='C', pos=(0, 0), size=(80, 40))
dot_btn = wx.Button(pan, label='.', pos=(0, 0), size=(80, 40))
sum_btn = wx.Button(pan, label='+', pos=(0, 0), size=(80, 40))
cha_btn = wx.Button(pan, label='-', pos=(0, 0), size=(80, 40))
ji_btn = wx.Button(pan, label='*', pos=(0, 0), size=(80, 40))
chu_btn = wx.Button(pan, label='\\', pos=(0, 0), size=(80, 40))
del_btn = wx.Button(pan, label='Del', pos=(0, 0), size=(80, 40))
res_btn = wx.Button(pan, label='=', pos=(0, 0), size=(80, 40))

win.Show()
cal.MainLoop()
