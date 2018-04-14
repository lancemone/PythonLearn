import os
import wx


# 创建一个简单的记事本了解一些wx的特性和功能，例如事件(events)和回调(callbacks)
# https://blog.csdn.net/chenghit/article/details/50421090


# 创建框架且在框架中包含一个可编辑的文本框(text box)
class MainWindow(wx.Frame):  # 生成一个wx.Frame的子类
    def __init__(self, parent, title):  # 重写wx.Frame的__init__方法
        wx.Frame.__init__(self, parent, title=title, size=(400, 300))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)  # 用wx.TextCtrl 声明一个简单的文本编辑器
        self.CreateStatusBar()  # 创建窗口底部的状态栏

        filemenu = wx.Menu()  # 设置菜单

        # filemenu.Append(wx.ID_ABOUT, '关于', '关于程序的信息')  # wx.ID_ABOUT和wx.ID_EXIT是wxWidgets提供的标准ID
        # filemenu.AppendSeparator()
        # filemenu.Append(wx.ID_EXIT, '退出', '终止应用程序')

        # 创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, '文件')
        self.SetMenuBar(menuBar)


        # 事件处理(event handling)
        # 在Python中，点击菜单，点击按钮，输入文本，鼠标移动等等，都被称为事件event，而对event做出反应，则被称为event handling
        # 使用Bind() 方法，将1个对象Object和1个时间event建立绑定关系
        menuOpen = filemenu.Append(wx.ID_OPEN, 'Open', '打开文件')
        menuAbout = filemenu.Append(wx.ID_ABOUT, '&About', '关于')
        menuExit = filemenu.Append(wx.ID_EXIT, 'E&xit', '退出')
        # 设置event
        # wx.EVT_MENU 指代“选择菜单中的项目”这个事件。所有的事件都是wx.Event 的子类。
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)  # 当用户点击about项目，self.OnAbout就会被执行
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)








        self.Show(True)  # 在__init__中运行过self.Show()后在创建的实例中无需再次运行

    def OnAbout(self, event):  # 声明OnAbout方法，否则执行self.Bind会提示错误。
        # 这里的eve参数是wx.Event 的子类的一个实例。当event发生的时候，method就会被执行。默认情况下，这个method会处理event，并且当callback完成之后，event也会停止
        # 在一些结构化的事件处理器event handlers中，我们可以使用event.Skip() 来跳过一个event
        # 创建一个带“OK”按钮的对话框，wx.OK是wxWidgets提供的标准ID
        dlg = wx.MessageDialog(self, 'A small text editor', 'About Sample Editor',
                               wx.OK)  # 语法是(self, 内容, 标题, ID).wx.ID可省略
        dlg.ShowModal()  # 显示对话框
        dlg.Destroy()  # 结束之后关闭对话框

    def OnExit(self, event):
        self.Close(True)  # 关闭整个frame

    # 对话（Dialogs）实现文本编辑器的打开或保存文档功能
    # 一般对话由底层平台提供，这样你的应用程序看上去就像是一个原生程序。在本例中，对话由 MainWindow 的 OnOpen 方法来实施
    '''首先，我们通过调用适当的构造函数来创建对话
       然后，我们调用ShowModal 打开对话框 - “Modal” 的意思是，在用户点击 OK 或 Cancel 之前，不能做任何的操作。
       ShowModal 的返回值是一个被点击按钮的 ID, 如果用户点击了 OK 按钮，程序就读取文件'''

    def OnOpen(self, event):
        'open a file'
        self.dirname = ''
        dlg = wx.FileDialog(self, 'choose a file', self.dirname, '', '*.*', wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()




app = wx.App(False)
frame = MainWindow(None, 'Small Editor')
app.MainLoop()
