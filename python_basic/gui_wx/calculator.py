import wx

# 创建应用和框架
cal = wx.App()
win = wx.Frame(None, id=-1, title='计算器', size=(400, 300))

# 添加面板
pan = wx.Panel(win)

# 创建控件
one_btn = wx.Button(pan, label='1', pos=(0, 120), size=(80, 40))
two_btn = wx.Button(pan, label='2', pos=(80, 120), size=(80, 40))
three_btn = wx.Button(pan, label='3', pos=(160, 120), size=(80, 40))
four_btn = wx.Button(pan, label='4', pos=(0, 160), size=(80, 40))
five_btn = wx.Button(pan, label='5', pos=(80, 160), size=(80, 40))
six_btn = wx.Button(pan, label='6', pos=(160, 160), size=(80, 40))
seven_btn = wx.Button(pan, label='7', pos=(0, 200), size=(80, 40))
eight_btn = wx.Button(pan, label='8', pos=(80, 200), size=(80, 40))
nine_btn = wx.Button(pan, label='9', pos=(160, 200), size=(80, 40))
zero_btn = wx.Button(pan, label='0', pos=(80, 240), size=(80, 40))
cle_btn = wx.Button(pan, label='C', pos=(0, 240), size=(80, 40))
dot_btn = wx.Button(pan, label='.', pos=(160, 240), size=(80, 40))
sum_btn = wx.Button(pan, label='+', pos=(240, 120), size=(80, 40))
cha_btn = wx.Button(pan, label='-', pos=(240, 160), size=(80, 40))
ji_btn = wx.Button(pan, label='*', pos=(240, 200), size=(80, 40))
chu_btn = wx.Button(pan, label='\\', pos=(240, 240), size=(80, 40))
del_btn = wx.Button(pan, label='Del', pos=(320, 120), size=(80, 40))
res_btn = wx.Button(pan, label='=', pos=(320, 160), size=(80, 120))

win.Show()
cal.MainLoop()
