import wx

app = wx.App()  # 创建应用
win = wx.Frame(None, title='文本编辑', size=(400, 320))  # 创建框架
win.Show()  # 显示框架
app.MainLoop()  # 运行主程序
