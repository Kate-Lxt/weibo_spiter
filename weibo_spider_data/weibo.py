#encoding：utf-8
#python: 3.6.8
#编辑器：pycharm

import requests
from bs4 import BeautifulSoup
import csv
import time
import random



def get_content(url):
    # url = "https://s.weibo.com/weibo?q=python&nodup=1"
    headers = {
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        'cache-control':'max-age=0',
        'cookie':'ALF=1651433765; SUB=_2A25PQyR1DeRhGeNJ6VAW-SbMwz2IHXVszEw9rDV8PUJbkNAKLWakkW1NS_y-_2yL88j-CghY60f7T_L957gvbVPI; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhsC07hLOUgwfFojXw5Qb0.5JpX5oz75NHD95QfS0zES0.RehnpWs4Dqcj_i--ci-zRiKnfi--fiKnci-zNi--Ri-iWi-8Fi--fi-82iK.7i--fiK.piK.N; WBStorage=f4f1148c|undefined; _s_tentry=-; Apache=5536111479281.014.1648861255464; SINAGLOBAL=5536111479281.014.1648861255464; ULV=1648861255495:1:1:1:5536111479281.014.1648861255464:',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'sec-fetch-dest':'document',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'none',
        'sec-fetch-user':'?1',
        'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',

    }
    response = requests.get(url,headers=headers,verify=False)#反爬kik
    html = BeautifulSoup(response.content,'lxml')
    conetnt = html.find_all('div',class_="card-wrap") # 这里CALSS 要加下划线      class="wrap"
    for ct in conetnt:
        # print(ct)
        user_info = ct.find_all('a',class_="name")
        if user_info != []:
            #user_name = user_info[0].text# 用户名称
            #user_index = "https:"+ user_info[0]['href'] # 用户主页
           # user_from = str(ct.find('p',class_="from").text).replace(' ','').replace('\n','') # 时间和发布终端设备名称
            weibo_content = str(ct.find('p',class_="txt").text).replace(' ','').replace('\n','') # 微博内容
            #data = [weibo_content,user_name,user_from,user_index]
            data = [weibo_content]
            saveCsv('微博内容_乡村云旅游', data)

def runx():

    n = 0
    for x in range(1,51):

        print(f"正在抓取第{x}页数据")
        n +=1

        url = f"https://s.weibo.com/weibo?q=乡村云旅游&nodup=1&page={x}"
        t = random.randint(2,5)# 随机抽取 2-5之间
        print(f"{t} 秒后开始抓取")
        time.sleep(t)

        if n%5 == 0:
            t = random.randint(5,10) # 随机抽取 5-10之间
            print(f"{t} 秒后继续抓取")
            time.sleep(t) #这里停止上面抽取出来的数值

        get_content(url)


def saveCsv(cgcg,content):
    fp = open(f"{cgcg}.csv",'a+',encoding='utf-8-sig',newline='')
    csv_fp = csv.writer(fp)
    csv_fp.writerow(content)
    fp.close()
    print(f"成功写入：{content}")





if __name__ == '__main__':

    col = ['乡村云旅游','发布者名称','发布时间以及设备','发布者主页']
    saveCsv('微博内容', col)
    runx()