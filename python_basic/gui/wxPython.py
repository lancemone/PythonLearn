# Python的GUI库有很多，这里我只介绍wxPython这个库（很有名气的一个库）
import wx

'''创建一个简单的图形界面应用程序，有几个必须的步骤。

创建应用
添加框架
添加面板
添加控件
添加函数
绑定控件函数
显示框架
运行主程序'''

# 显示一个应用程序的图形界面
app = wx.App()  # 创建应用
win = wx.Frame(None, title='文本编辑', size=(400, 320))  # 创建框架
win.Show()  # 显示框架
app.MainLoop()  # 运行主程序
