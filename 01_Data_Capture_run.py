import imp
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from lxml import etree
import csv

ua = UserAgent().random     # 隨機產生headers
url = 'https://tbb.moneydj.com/w/wb/wb02_TLZ64-0928_7_0_0.djhtm'
headers = {'user-agent':ua}
r = rq.get(url,headers=headers)  # 將隨機產生的headers加入Get請求中
soup_table = (pd.read_html(r.text))[2]
print(soup_table)

soup_table.to_csv('TLZ64_0928.csv', index=False, header=False)  # 存成csv檔案
