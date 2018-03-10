import logging
import os
from time import sleep

# 刷金币次数
repeat_times = int(input('请输入刷金币次数：'))

# 定义真机分辨率
device_x, device_y = 1920, 1152

# 日志输出
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


# 创建一个动作函数
def tap_screen(x, y):
    """calculate real x, y according to device resolution."""
    base_x, base_y = 1920, 1152
    real_x = int(x / base_x * device_x)
    real_y = int(y / base_y * device_y)
    os.system('adb shell input tap {} {}'.format(real_x, real_y))


# 创建刷金币的函数
def do_maony_work():
    # print('点击陨落的废都')
    tap_screen(490.7, 387.7)
    # print('等待1秒')
    sleep(1)

    # print('点击魔女回忆')
    tap_screen(1123.4, 519.5)
    # print('等待1秒')
    sleep(1)

    # print('点击大师')
    tap_screen(1644.0, 736.4)
    # print('等待2秒')
    sleep(2)

    print('点击下一步')
    tap_screen(1666.0, 1067.0)
    # print('等待3秒')
    sleep(3)

    print('点击闯关')
    tap_screen(1506.1, 991.0)
    # print('等待33秒')
    sleep(33)
    print('加载结束')

    print('点击自动')
    tap_screen(1791.0, 70.9)
    # print('等待32秒')
    sleep(32)

    print('瞎点10次')
    for i in range(10):
        tap_screen(399.7, 599.5)
        sleep(1)

    # print('等待3s')
    sleep(3)

    print('点击屏幕继续')
    tap_screen(980.5, 1052.0)
    print('等待7秒')
    sleep(7)

    print('点击返回')
    tap_screen(1232.4, 1063.0)
    # print('等待5秒')
    sleep(5)


# 创建一个主循环
if __name__ == '__main__':
    for i in range(repeat_times):
        print('round #{}'.format(i + 1))
        do_maony_work()

print('任务结束！')
