import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title)
        self.InitUI()

    def InitUI(self):
        # 让其在屏幕中间打开并调整大小展示
        self.SetSize((300, 400))
        self.Center()

        # 创建一个菜单栏
        menuBar = wx.MenuBar()

        # 创建一个菜单1
        fileMunu = wx.Menu()

        # 创建一个菜单项1-1
        newItem = wx.MenuItem(fileMunu, id=wx.ID_NEW, text='new', kind=wx.ITEM_NORMAL)
        fileMunu.Append(newItem)

        # 添加一行线
        fileMunu.AppendSeparator()

        # 创建一个子菜单1-2
        editMenu = wx.Menu()

        # 创建三个子菜单的菜单项1-2-1   1-2-2  1-2-3
        cutItem = wx.MenuItem(editMenu, id=122, text='cut', kind=wx.ITEM_NORMAL)
        copyItem = wx.MenuItem(editMenu, id=121, text='copy', kind=wx.ITEM_NORMAL)
        pasteItem = wx.MenuItem(editMenu, id=123, text='paste', kind=wx.ITEM_NORMAL)
        editMenu.Append(copyItem)
        editMenu.Append(cutItem)
        editMenu.Append(pasteItem)

        # 把子菜单1-2添加到菜单1
        fileMunu.Append(wx.ID_ANY, 'Edit', editMenu)

        # 添加一行线
        fileMunu.AppendSeparator()

        # 添加两个单选框1-3 1-4
        radio1 = wx.MenuItem(fileMunu, id=13, text='one', kind=wx.ITEM_RADIO)
        radio2 = wx.MenuItem(fileMunu, id=14, text='two', kind=wx.ITEM_RADIO)
        fileMunu.Append(radio1)
        fileMunu.Append(radio2)
        # PS.单选框 只在自己区域之间（两行线之间） 相互作用

        # 添加一行线
        fileMunu.AppendSeparator()

        # 添加一个可选中的菜单项1-5
        fileMunu.AppendCheckItem(id=15, item='check')

        exitMenu = wx.Menu()

        self.exit = wx.MenuItem(exitMenu, id=wx.ID_EXIT, text="Quit", kind=wx.ITEM_NORMAL)
        exitMenu.Append(self.exit)

        # 添加一个菜单项1-6并注册快捷键
        # quit = wx.MenuItem(fileMunu, id=wx.ID_EXIT, text='Quit\tCtrl+Q', kind=wx.ITEM_NORMAL)
        # fileMunu.Append(quit)

        # 将菜单添加到菜单栏
        menuBar.Append(fileMunu, title='&File')
        menuBar.Append(exitMenu, title='&Exit')

        # 设置窗口框架的菜单栏
        self.SetMenuBar(menuBar)

        # 绑定事件处理
        self.Bind(wx.EVT_MENU, self.OnHandler, newItem)
        self.Bind(wx.EVT_MENU, self.OnExit, self.exit)

    def OnHandler(self, event):
        print('new')

    def OnExit(self, event):
        self.Close()


if __name__ == "__main__":
    ex = wx.App(False)
    Frame = Mywin(None, 'Menu_Test')  # 可以同时打开两个窗口
    Frame.Show()
    ex.MainLoop()
