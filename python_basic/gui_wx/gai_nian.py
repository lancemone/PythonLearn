# Python的GUI库有很多，这里我只介绍wxPython这个库（很有名气的一个库）
# wxPython库中的方法命名都是首字母大写的格式，这和python的习惯不一致
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

# 创建一个有界面显示的文本框
# 1、创建应用
app = wx.App()  # 对App类实例化。wx.App：每个wx应用程序都必须有一个wx.App实例。为了确保GUI平台和wxWidgets已经完全初始化，所有创建UI对象的过程都应该放在wx.App实例化之后。

# 2、添加框架
# wx.Frame：框架是一个窗口，其大小和位置可以(通常)由用户更改。它通常有粗边框和标题栏，并且可以选择包含菜单栏、工具栏和状态栏。框架可以包含任何不是框架或对话框的窗口
win = wx.Frame(None, title='文本编辑', size=(400, 320))  # 对Frame进行实例化。在对Frame类进行实例化时，可以设定一些参数
'''在对Frame类进行实例化时，可以设定一些参数
Frame(parent, id=ID_ANY, title=””, pos=DefaultPosition,size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameStr)
*parent：父窗口。一般情况下是None。如果不是None，当前窗口的父窗口被最小化并恢复时，当前窗口将被最小化。
*id：窗口的标识符。它的值可以为-1，表示默认值。
*title：窗口的标题。它的值是一个字符串。
*pos：窗口的位置。参数值DefaultPosition表示默认位置，可以输入包含x轴与y轴坐标数值的元组。
*size：窗口的尺寸。参数值DefaultSize表示默认尺寸，可以输入包含宽度与高度数值的元组。
*style：窗口的样式。具体设置参考官方文档wx.Frame类描述中的Window Styles部分【点此查看】。例如，创建一个不可以调整尺寸的窗口，该参数的设置为：使用默认样式并且（&）不包含（~）更改边框尺寸和（|）最大化按钮
# style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX )
*name：窗口的名称。值为字符串；该参数用于将名称与项目关联起来，允许应用程序用户为单个窗口设置主题资源值。'''

# 3、添加面板。可以使用wx.Panel类，Panel是放置控件的窗口
# 虽然，我们可以在窗口中直接添加控件，但是，这样并不便于管理。当一个窗口中，划分了不同的功能（一个功能可能是多个控件组成），有些功能需要能够单独的显示或隐藏时，实现起来会非常复杂。解决这样的问题，我们可以使用wx.Panel类
# 默认情况下，面板的尺寸和父窗口一致，颜色和对话框相同；如果想更改可以用面板对象调用相关的Set方法。
pan = wx.Panel(win)  # 添加面板，实例化Panel方法。
pan.SetBackgroundColour('#666666')  # 设置面板背景色
'''在实例化一个Panel时，我们同样可以设定一些参数。

Panel(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,style=TAB_TRAVERSAL, name=PanelNameStr)

parent：父窗口。
id：面板的标识符。
pos：窗口的位置。参数值DefaultPosition表示默认位置，可以输入包含x轴与y轴坐标数值的元组。
size：窗口的尺寸。参数值DefaultSize表示默认尺寸，可以输入包含宽度与高度数值的元组。
style：面板的样式。具体设置参考官方文档wx.Panel类描述中的Window Styles部分。
name：面板的名称。参数值为字符串。'''

# 4、添加控件
'''这些控件的参数大同小异，一般包含以下参数：

parent：父窗口。
id：控件的标识符。
label/value：控件上默认的文本或值。
pos：控件在父窗口中的位置。
size：控件的尺寸。
style：控件的样式。
validator：控件的验证器。
name：控件的名称。
'''
file_btn = wx.FilePickerCtrl(pan, pos=(5, 5))  # 文件选择控件：FilePickerCtrl
# FilePickerCtrl控件默认的文字为Browse（浏览），如果想改成中文，不能直接调用SetLabel()方法.原因就是这个控件由两个控件（TextCtrl和PickerCtrl）组成，如果设置选择控件（PickerCtrl）的文本，必须先获取选择控件。
file_btn.GetPickerCtrl().SetLabel('选择')
open_btn = wx.Button(pan, label='打开', pos=(215, 5), size=(80, 30))  # 按钮：Button
save_btn = wx.Button(pan, label='保存', pos=(300, 5), size=(80, 30))
# TextCtrl控件默认是单行文本输入框，如果想能够多行输入并且带有滚动条，需要设置style参数。
cont_ipt = wx.TextCtrl(pan, pos=(5, 40), size=(375, 240),
                       style=wx.TE_MULTILINE | wx.HSCROLL)  # 文本控件：TextCtrl.wx.TE_MULTILINE：文本允许多行（自动允许垂直滚动);wx.HSCROLL：允许水平滚动

# 完成这个界面的过程很复杂，每个控件我们都需要指定位置；并且，还存在一个问题，就是改变窗口尺寸的时候，控件不能够跟随着改变尺寸。
# 如果想布局更加容易，而且能达到控件尺寸自动适应窗口尺寸的效果，我们可以使用sizer（尺寸器）。wx.BoxSizer类，能够帮助我们创建尺寸器对象。
# 可以把尺寸器理解为一个控件容器，尺寸器中的控件可以水平摆放或者垂直摆放，并且尺寸器可以嵌套。
# 如果使用尺寸器，需要先划分.hbox中包含3个控件：文件选择/打开按钮/保存按钮,而vbox中，包含hbox和文本控件
hbox = wx.BoxSizer()  # 尺寸器实例化（默认水平）
hbox.Add(file_btn, proportion=0, flag=wx.EXPAND)  # 添加控件到尺寸器
hbox.Add(open_btn, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(save_btn, proportion=0, flag=wx.LEFT, border=5)
vbox = wx.BoxSizer(wx.VERTICAL)  # 尺寸器实例化（垂直）
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(cont_ipt, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
pan.SetSizer(vbox)  # 为窗口设置尺寸器。SetSizer(sizer)：将设置好布局的尺寸器添加到窗口。

'''Add (sizer, proportion=0, flag=0, border=0)：此方法能够将子尺寸器（或控件）添加到尺寸器。

sizer：尺寸器或控件。

proportion：参数值为0或者1；值为1时，尺寸器或控件尺寸将随窗口尺寸发生变化；值为0时，为固定尺寸。

flag：影响尺寸器行为的标志；参数为整数或值为整数的常量。flag这个参数，它的值可以为多个，值之间需要使用管道符“|”分隔。
wx.EXPAND：指定尺寸器或控件是否被扩展以填充分配给它的空间。
wx.LEFT/wx.RIGHT/wx.BOTTOM/wx.ALL：指定边界宽度将应用到的尺寸器的哪一边。

border：边距；值为整数。'''


# 5、添加函数
def open_filr(event):
    file_path = file_btn.GetPath()  # 从文件选择器控件获取文件路径.通过Get方法能够获取到控件中的路径以及值
    with open(file_path) as file:  # 打开文件
        cont_ipt.SetValue(file.read())  # 读取文件内容这只到文本控件的值


def save_file(event):
    file_path = file_btn.GetPath()
    with open(file_path, 'w') as file:
        file.write(cont_ipt.GetValue())


'''控件的Get方法还有很多，在这里没有办法一一介绍。

比较常用的一些方法：
GetPath()：获取路径。
GetValue()：获取控件的值。
GetLabel()：获取控件的标签文本。
GetName()：获取控件的名称。
GetId()：获取控件的ID。
GetSize()：获取控件的尺寸。
GetPosition()：获取控件的位置'''

# 6、函数与控件绑定(事件)
open_btn.Bind(wx.EVT_BUTTON, open_filr)
save_btn.Bind(wx.EVT_BUTTON, save_file)

# 7、显示框架
win.Show()  # Show(show=True)：用于显示隐藏窗口。不填入参数或参数为True时，显示窗口；参数为False时，隐藏窗口。

# 8、运行主程序
app.MainLoop()  # MainLoop()：循环执行GUI主程序

'''Python文件有以下几种类型：

py：源代码文件。由 py.exe 运行，也可以通过命令行终端运行。
pyw：图形界面程序源代码文件。由pyw.exe运行，和py运行的区别在于不会显示命令行窗口。不过，还是建议大家在编程过程中，先将源代码命名为py文件，当程序出现错误时，能够在命令行窗口看到相关信息。
pyc：py文件经过编译后产生的文件，无法直接看到源代码。因为已经经过编译，运行速度比py文件更快。
pyo：py文件优化编译后产生的文件，无法直接看到源代码。可以在命令行窗口，通过 “python -O 源代码文件”将源代码文件编译为pyo 文件。
pyd：这类文件不是用 python 编写成的，一般是其他语言编写的 python 扩展模块。'''

'''在 frame 里面，你可以使用若干个 wxWindow 子类来充实 frame 的内容，常用的元素有以下几种：

wx.MenuBar, 在 frame 的顶部填加菜单栏
wx.StatusBar, 在 frame 的底部填加状态栏，显示状态信息
wx.ToolBar, 在 frame 中添加工具栏
wx.Control 的子类，它们代表用户接口的widgets (例如显示数据 and/or 处理用户输入的可见元素). 常见的wx.Control 对象包括 wx.Button, wx.StaticText, wx.TextCtrl 和 wx.ComboBox.
wx.Panel, 它是容纳各种wx.Control 对象的容器。把wx.Control 对象放入wx.Panel, 用户就可以操作它们。'''
