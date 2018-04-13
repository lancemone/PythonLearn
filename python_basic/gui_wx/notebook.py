import wx


# 创建一个简单的记事本了解一些wx的特性和功能，例如事件(events)和回调(callbacks)


# 创建框架且在框架中包含一个可编辑的文本框(text box)
class MainWindow(wx.Frame):  # 生成一个wx.Frame的子类
    def __init__(self, parent, title):  # 重写wx.Frame的__init__方法
        wx.Frame.__init__(self, parent, title=title, size=(400, 300))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)  # 用wx.TextCtrl 声明一个简单的文本编辑器
        self.CreateStatusBar()  # 创建窗口底部的状态栏

        filemenu = wx.Menu()  # 设置菜单

        filemenu.Append(wx.ID_ABOUT, '关于', '关于程序的信息')  # wx.ID_ABOUT和wx.ID_EXIT是wxWidgets提供的标准ID
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, '退出', '终止应用程序')

        # 创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, '文件')
        self.SetMenuBar(menuBar)

        # 事件处理(event handling)
        # 在Python中，点击菜单，点击按钮，输入文本，鼠标移动等等，都被称为事件event，而对event做出反应，则被称为event handling
        # 使用Bind() 方法，将1个对象Object和1个时间event建立绑定关系
        menuAbout = filemenu.Append(wx.ID_ABOUT, '&About', 'Information about this program')
        menuExit = filemenu.Append(wx.ID_EXIT, 'E&xit', 'Terminate the program')
        # 设置event
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)  # 在__init__中运行过self.Show()后在创建的实例中无需再次运行

    def OnAbout(self, eve):
        # 创建一个带“OK”按钮的对话框，wx.OK是wxWidgets提供的标准ID
        dlg = wx.MessageDialog(self, 'A small text editor', 'About Sample Editor',
                               wx.ID)  # 语法是(self, 内容, 标题, ID).wx.ID可省略
        dlg.ShowModal()  # 显示对话框
        dlg.Destroy()  # 结束之后关闭对话框

    def OnExit(self, eve):
        self.Close(True)  # 关闭整个frame


app = wx.App(False)
frame = MainWindow(None, 'Small Editor')
app.MainLoop()
