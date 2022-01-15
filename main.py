# -*- coding: utf-8 -*-
# @Time    : 2022/1/15 11:10
# @Author  : Leonard
# @Email   : leoleechn@hotmail.com
# @File    : main.py
# @software: PyCharm

import time
import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/97.0.4692.71 Safari/537.36"}
for i in range(10):
    url = "https://movie.douban.com/top250?start=" + str(i * 25) + "&filter="
    html_response = requests.get(url, headers=header)
    html_response.encoding = "utf-8"

    main_page = BeautifulSoup(html_response.text, "html.parser")
    imgList = main_page.find("ol", class_="grid_view").find_all("img")

    for a in imgList:
        html_imgName = a.get("alt") + ".jpg"
        html_source = a.get("src")
        img_response = requests.get(html_source)
        with open("img/" + html_imgName, mode="wb") as file:
            file.write(img_response.content)
        print(html_imgName + "下载完成")
        time.sleep(1)
print("全部图片下载完成")
