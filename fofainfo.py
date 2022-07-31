import linecache
import re
import os.path
import base64
import requests
import json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 关闭请求安全警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print("""\033[1;36m
__________________________________________________________________________________
|   _________     ____________      _________           _______                  |
|  |   ______|    |  ______  |     |   ______|         /       \\                 |
|  |   |_____     |  |    |  |     |   |_____         /    _    \\                |
|  |   ______|    |  |    |  |     |   ______|       /    /_\\    \\               |
|  |   |          |  |    |  |     |   |            /    _____    \\              |
|  |   |          |  |____|  |     |   |           /    /     \\    \\             |
|  |___|          |__________|     |___|          /____/       \\____\\            |
|                                                               V:1.0.0          |
|                                                               by:ice0bear14h   |
|________________________________________________________________________________|
\033[0m""")

filename='fofakey.txt'
# 判断文件是否存在
files = os.path.isfile(filename)
# print(files)
print("\n\033[1;34m[+] 检查配置文件（fofakey.txt）是否存在！！！\033[0m")
# True or False
if files == False :
    # print('配置文件（fofakey.txt）不存在')
    print('\n\033[1;31m[-] 配置文件（fofakey.txt）不存在！！！\033[0m')
    file = open('fofakey.txt', 'w')
    print('\n\033[1;34m[+] 配置文件(fofakey.txt)已在当前目录下创建成功！！！\033[0m')
    # return = '配置文件（fofakey.txt）不存在，请创建'
    # a = '配置文件（fofakey.txt）不存在，请创建'
elif files == True :
    print('\n\033[1;34m[+] 配置文件(fofakey.txt)存在！！！\033[0m')

print("""\n\033[1;34m
【配置文件（fofakey.txt）说明如下：】
【第一行：保存 fofa 账号】
【第二行：保存 fofa API】
\033[0m""")

# 判断内容是否为空
sz = os.path.getsize(filename)
if not sz :
    print('\n\033[1;31m[-] 配置文件（fofakey.txt）内容为空！！！\033[0m')
    emailput = input("\n\033[1;34m输入fofa 账号：\033[0m")
    keyput = input("\n\033[1;34m输入fofa API：\033[0m")
    with open('fofakey.txt','a') as f :
        f.write(str(emailput) + '\n')
        f.write(str(keyput))
    print("\033[1;34mfofa账号为：\033[0m",emailput)
    print("\033[1;34mfofa API为：\033[0m",keyput)
else :
    email = linecache.getline('fofakey.txt', 1)
    key = linecache.getline('fofakey.txt', 2)
    print("\033[1;34mfofa账号为：\033[0m",email)
    print("\033[1;34mfofa API为：\033[0m",key)

# 定义变量，读取文件内容
email = linecache.getline('fofakey.txt', 1)
key = linecache.getline('fofakey.txt', 2)
# print(email)
# print(key)

search = base64.b64encode(input("\n\033[1;34m[+] 输入查询语句：\033[0m").encode('utf-8'))
# 正则
sub = re.sub("[']",'',str(search))
# print(sub)

print("""\n\033[1;34m
【API查询数量说明如下：】
【每页查询数量，默认为100条，最大支持10,000条/页】
【最终数量由实际查询到的数量和结果总数为准！！！】
\033[0m""")
size = int(input("\n\033[1;34m[+] 输入要查询的数量\033[0m") or "100")
print("\033[1;34m 需要查询的数量为：\033[0m",size)
fields = 'host'

fofa = 'https://fofa.info/api/v1/search/all?email=%s&key=%s&qbase64=%s&size=%s&fields=%s' % (email,key,sub[1:],size,fields)
# print(fofa)
reponse = requests.get(fofa)
# print(reponse.text)
# print((reponse.content).decode('utf-8'))
repon = json.loads((reponse.content).decode('utf-8'))
# print(repon)
paqu = len(repon['results'])
print(f"\n\033[1;34m[+] 查询到的数量为:{paqu}\033[0m")

# 当前本地时间
localtime = time.localtime(time.time())
time = time.strftime("%Y%m%d%H%M%S", time.localtime())
# print(time)

filename = str(input("\n\033[1;34m[+] 输入保存文件名称（回车默认当前时间为名）：\033[0m") or time)
# print(filename)

print("\n\033[1;34m[+] 正在抓取状态为200的目标URL..........\033[0m")
for i in range(len(repon['results'])):
    url = repon['results'][i]

    if 'http://' not in url :
        url = 'http://' + url
        # print(url)
        try:
            reponse = requests.get(url,verify=False,timeout=2)
            if reponse.status_code == 200 :
                print('\n\033[1;34m[+]正在写入：\033[0m' , url)
                with open(str(filename) + '.txt', 'a') as f:
                    f.write(str(url) + '\n')
        except:
            pass
    else :
        try :
            reponse = requests.get(url, verify=False, timeout=2)
            if reponse.status_code == 200:
                print('\n\033[1;34m[+]正在写入：\033[0m' , url)
                with open(str(filename) + '.txt', 'a') as f:
                    f.write(str(url) + '\n')
        except:
            pass

filepath = str(filename) + '.txt'

num= 1
for num , line in enumerate(open(filepath, 'r', encoding='utf-8').readlines()):
    num += 1
print('\n\033[1;34m[+] 抓取共计(条):\033[0m', num)
print("\n\033[1;34m[+] 抓取完成，保存文件为\033[0m", filepath)
