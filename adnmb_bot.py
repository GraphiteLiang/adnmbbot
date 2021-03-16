# 2sr yyds!
from bs4 import BeautifulSoup
import bs4
import re
import requests
# 使用方法：安装python后直接运行本文件，即可爬取《我的室友虽然是个福利姬但是她贼喜欢吃我做的饭》
# 替换base_url为你要爬取的串，按理来说是可以爬取任何串的只看po
# 爬取的文本内容会被保存到和这个脚本同文件夹下的adnmb.txt下
def get_page(x):
    return "page/"+str(x)+".html"

patterns = ["<br>","<br/>",'<div class="h-threads-content">',"<div>","</div>"]
re_pattern = re.compile(r'<font .*</font>')
base_url = "https://adnmb3.com/Forum/po/id/33006693/"# 把串号替换掉即可
# 爬取主楼
url = base_url + get_page(1)
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, "html.parser")
div = soup.find('div',class_="h-threads-item-main").find_all('div',class_="h-threads-content")
for x in div:
        with open("adnmb.txt", "a",encoding="utf-8") as f:
            f.write(str(x).replace("<br/>","\n").replace('<div class="h-threads-content">', ""))
# 爬取原po自己的回复
for i in range(1,36):
    url = base_url + get_page(i)
    print("正在爬取……"+url)
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, "html.parser")
    div = soup.find('div',class_="h-threads-item-replys").find_all('div',class_="h-threads-content")
    for x in div:
        tmp = str(x)
        for p in patterns:
            tmp = tmp.replace(p,"")# 这步和下面的re.sub是用于清洗掉垃圾数据
        tmp = re.sub(re_pattern, "----", tmp)
        with open("adnmb.txt", "a",encoding="utf-8") as f:
            f.write(tmp)
