import re
import requests


url = 'http://img2.woyaogexing.com/2017/07/25/9f57552dc2bc69c3!600x600.jp'

html = requests.get(url).text
pic_url = re.findall('"data-objurl":".*=",', html, re.S)

i = 0
for each in pic_url:
    print(each)
    try:
        pic = requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print('[错误] 当前图片无法加载')
        continue
string = 'pictures\\' + str(i) + '.jpg'
fp = open(string, 'wb')
fp.write(pic.content)
fp.colse
i += 1
