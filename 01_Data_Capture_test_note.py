# import pandas as pd
# import requests as rq
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# from lxml import etree

# # # 自動化記錄模式
# # # # python -m playwright codegen "https://docs.google.com/forms/d/e/1FAIpQLScowkYbZ9aVeCT5lYTDiuoTf12PnnpgrGT6i8OxBaVHvn3YIA/viewform"

# ua = UserAgent()
# # print(ua.random)
# # print('--------↑↑↑↑↑ Test random headers ↑↑↑↑↑--------')
# user_agent = ua.random    # 隨機產生headers
# # print(user_agent)
# url = 'https://tbb.moneydj.com/w/wb/wb05.djhtm?a=PIZD3-82D1'
# headers = {
#     'user-agent':'user_agent',
#     # 'Referer': url,
#     # 'cookie': 'Cookie: pzqXflQLz5wTSg580T=1ATgIAgbnGDfrtgLIWzveVHzQ_95PLGeSjv96_6bO07zH.SmF9_dlJJCJoPaXo1Mp1oEsXdgSGkno.PvhLayXQhzXF_sVfyNotpRnbtAvnPXKQ03rSJvGRm0rVeA6IeOkdu8AAcfwuWyKCi4UAjdA1854Z3oI9QnrsyJ8Y.L.eXd7HuwtupbsV20yho94cSLSGWCnzy7B.9neggOfmkbk7CHvINWZsLeUQtoT2VUHuivWLmQ0FWX22yAQV9FqN87IsIs2wLZGJmo2krKIdYird9FxntIbzn9IP7ERffKvdpoIfmksi.N.z8WSMTsOdIEhWMyCRgNcZuHCiy48hFVJcyGqPeVTt5hojAzLCzu6w5Zxp_jaXe3e3dwNNW2OS8LBGm7; pzqXflQLz5wTSg580S=AfI1EXDGOVwNfZCmkRg8dkcKyjHWYeB1dnCtjKw8Ulrw0QgZvchLCTUltHE9FCMk; JSESSIONID=jquGMDInFp3yapPMVkfEz59U.node1; TS01795d98=014dc385f0c22da0655a560f844acf883f11ae4b34236a3d2c1509dbff04912fff935ccf25095e1a2444977938a9960ae0e01d784b; LFR_SESSION_STATE_20159=1665585713242; COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=zh_TW',
#     # 'Accept': 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     # 'Accept-Language': 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#     # 'Accept-Encoding': 'Accept-Encoding: gzip, deflate, br',
#     # 'Connection': 'Connection: keep-alive',
#     # 'Upgrade-Insecure-Requests': 'Upgrade-Insecure-Requests: 1',
#     # 'Sec-Fetch-Dest': 'Sec-Fetch-Dest: document',
#     # 'Sec-Fetch-Mode': 'Sec-Fetch-Mode: navigate',
#     # 'Sec-Fetch-Site': 'Sec-Fetch-Site: none',
#     # 'Sec-Fetch-User': 'Sec-Fetch-User: ?1'
#     }  # 隨機產生headers
# r = rq.get(url,headers=headers).text  # 將隨機產生的headers加入Get請求中
# # print(r.text)
# soup = BeautifulSoup(r, 'lxml')
# # print(soup)
# soup_table = pd.read_html(r)
# # print(soup_table)

# table_0 = soup_table[1]

# # table_0.columns = ['除息日','狀態', '息值或比例', '年化配息率(%)', '幣別']
# print('====↓↓↓↓↓↓↓↓↓↓↓====')
# # print(table_0.columns)

# df = pd.DataFrame(table_0)
 
# df.columns = ['除息日','狀態', '息值或比例', '年化配息率(%)', '幣別']  # 自訂欄位名稱
# df = df.groupby("除息日").first()  # 以名稱來進行群組

# print(df)



# import requests
# from datetime import time
# import random

# for page in range(1, 11):
#     requests.get('https://tbb.moneydj.com/w/wb/wb05.djhtm?a=PIZD3-82D1')
#     # 隨機暫停 1~5 秒
#     time.sleep(random.uniform(1, 5))

# ===========================================

# pd.read_html(html_string)[0].head()


# import requests
# from bs4 import BeautifulSoup
# response = requests.get(
#     "https://www.tbb.com.tw/web/guest/exchange_rate#p_App3107_WAR_TBBContentUtilsportlet:~:text=4.3150-,4.5210,-%E6%9C%AC%E8%A1%A8%E8%B3%87%E6%96%99")
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())  #輸出排版後的HTML內容




# from requests_html import HTMLSession
# session = HTMLSession()

# r = session.get('https://www.tbb.com.tw/web/guest/exchange_rate')
# r.html.render()
# print(r.html.render())
# print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ r.html.html ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
# print(r.html.html)
# print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ r.html.links ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
# print(r.html.links)
# print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ r.text ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
# print(r.text)
# print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ r.html.text ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
# print(r.html.text)


# r.encoding = 'UTF-8'
# # print(r.status_code)
# rco = r.content
# print(r.text)
# print(r.status_code)
# try:
#     if r.status_code == 200:
#         print(r.text)
# except:
#     print('none')
    


# soupresp = BeautifulSoup(r.text, 'lxml')

# print(htmlresp.text) #列出文字
# print(soupresp) #列出編碼
# print(htmlresp.status_code) #列出 HTTP 狀態碼
# print(htmlresp.headers) #列出 HTTP Response Headers
# print(htmlresp.headers['Content-Type']) #印出 Header 中的 Content-Type
# print(f'Type: {type(htmlresp.text)}')
# print(f'Len: {len(htmlresp.text)}')
# print(soupresp)

# headers = {
#     # 假装自己是瀏覽器
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
#     # 把Cookie塞進来
#     'Cookie': 'eda38d470a662ef3606390ac3b84b86f9; Hm_lvt_f1d3b035c559e31c390733e79e080736=1553503899; biihu__user_login=omvZVatKKSlcXbJGmXXew9BmqediJ4lzNoYGzLQjTR%2Fjw1wOz3o4lIacanmcNncX1PsRne5tXpE9r1sqrkdhAYQrugGVfaBICYp8BAQ7yBKnMpAwicq7pZgQ2pg38ZzFyEZVUvOvFHYj3cChZFEWqQ%3D%3D; Hm_lpvt_f1d3b035c559e31c390733e79e080736=1553505597',
# }

# import requests
# from requests.exceptions import RequestException
# from datetime import time
# import random
# import time
# import json

# def main():
#     url = 'https://www.tbb.com.tw/web/guest/exchange_rate'
#     html = get_one_page(url)
#     print(html)

# def get_one_page(url):
#     headers = {"user-agent": "Mizilla/5.0", "Referer": "https://www.tbb.com.tw/web/guest/exchange_rate", "cookie": "pzqXflQLz5wTSg580T=1CWKlCrENDdHF7rDljVxbnCkoQwAyiRsjW8t7QiEg1YkVJE.rckpI.03KfM8Tf.Tt05bEEDKjD_QQJMxAixUT_nkTOniW0LWu.cjTBdTjblY1QGy9lBMDOrj1GHmPT5HHuNrsNDTW5nC5akDCT2BuhPL4jOuOBlGaTvsVjLqcUU7Ma56SFmPdBSDT5YH3qvQjK5fgFvKGhphAn75Eek99MNcJR9scYawFEXmnGevFJGleMfG61zYE1f9txKvg9FZwypS7rf1KUIO.zQKYSxMQ6MeegqBl7jHBYS4lyRgh4G0dIglf2puwGoVuF5oX1ACswlBFXM1iwbkC1qLDqjju_H8kZOAlX2hB_C4bXeZAQLY8_.oDBlgiQA2jTKY1XMTNEAA; pzqXflQLz5wTSg580S=AfI1EXDGOVwNfZCmkRg8dkcKyjHWYeB1dnCtjKw8Ulrw0QgZvchLCTUltHE9FCMk; JSESSIONID=YPUhbfTRa+4WYM86-uqlbvUU.node1; TS01795d98=014dc385f06183f25fddef36ce927aa168df73fad9b25593194dd0575959062d1628fdbcb1f31a3b27ab3ffeea16ac3066e3d97d01; LFR_SESSION_STATE_20159=1665559145442; COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=zh_TW"}
#     for page in range(1, 11):
#         response = requests.get(url, headers=headers)
#         time.sleep(random.uniform(1, 5))
#     # try:
#     #     if response.status_code == 200:
#         return json.loads(response.text)
#     #     return None
#     # except RequestException:
#     #     return None

# if __name__ == '__main__':
#     main()

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.tbb.com.tw/web/guest/exchange_rate")
#     print(page.title)
#     browser.close()

# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# browser = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
# url = 'https://www.tbb.com.tw/exchange_rate#accesskey-c'
# browser.get(url)
# # print(browser.page_source)
# # browser.find_elements(by=By.ID, value='ratequery1')
# # pd.read_html(browser.page_source)[0].head()
# # element_xpath = '/html/body/div[1]/div[1]/div[8]/div[2]/div/div/div/div/div/div/div/div/div[2]'
# # target_table = browser.find_element(by=By.XPATH, value=element_xpath)

# fetch_string = '''fetch("https://www.tbb.com.tw/c/portal/render_portlet?p_l_id=21736&p_p_id=App3107_WAR_TBBContentUtilsportlet&p_p_lifecycle=0&p_t_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_pos=0&p_p_col_count=1&p_p_isolated=1&currentURL=%2Fexchange_rate&IIhfvu=1nHi_TEsEczhlseIv02XZutVQA3yjvWSrVBz6ecEZTLwOBLjn3gKnZviwCNwwYTeHsfbtAFydnsNDq.LZKqh65K2Pi.bpdP3EPqdbVfVnODD1ID6KxqeLKw_9BiU_AFw1l9urNNbgcdJMcw2G1Kouv8CPODX8RWXxsdqyCnDm3BnfJUXmBgH_knymPnlYCEtMOOu1NakCO7ZmwmJFJ9gZsudp.8XoZfv6Sj8HF.74DR5dGzq.aRHkELfyIsafJqOe9rVSoqmtdhz6oR9xlXNCE0UrFA4NpfCfBVboxM2yb51G5ttolUtR6a9ZUskXEAa09VA_ClTY35Lc3U8lMwi6qfe4uamlrGRIFsk5F202HUpFiFhHZM.kZpbXId2Wu9n06Zw2wTZPO_BOobSqYefzHVY_hj1c_oND7iV", {
#   "headers": {
#     "accept": "text/html, */*",
#     "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#     "content-type": "text/plain;charset=UTF-8",
#     "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "x-requested-with": "XMLHttpRequest"
#   },
#   "referrer": "https://www.tbb.com.tw/exchange_rate",
#   "referrerPolicy": "same-origin",
#   "body": "",
#   "method": "POST",
#   "mode": "cors",
#   "credentials": "include"
# });'''
# browser.execute_script(fetch_string)

# # html_string = target_table.get_attribute('outerHTML')
# # pd.read_html(browser.page_source)[0].head()


# browser.close()

# ===============================
# puppeteer
# import asyncio
# from pyppeteer import launch
# from bs4 import BeautifulSoup

# async def main():
#     # 開啟瀏覽器程序
#     browser = await launch()
#     # 用瀏覽器連到 x 網站
#     page = await browser.newPage()
#     await page.goto('https://tbb.moneydj.com/w/wb/wb05.djhtm?a=PIZD3-82D1')    

#     html_doc = await page.content()
#     soup = BeautifulSoup(html_doc, 'lxml')
    
#     await browser.close()

#     print(soup)

# asyncio.run(main())

# ===============================
# # request-html
# from requests_html import HTMLSession
# from bs4 import BeautifulSoup

# session = HTMLSession()
# r = session.get('https://www.tbb.com.tw/web/guest/exchange_rate') 

# r.html.render()
# soup = BeautifulSoup(r.text, 'lxml')
# print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
# print(soup)
# =======================================
# pandas.DataFrame.to_csv() 函式語法
# pandas.DataFrame.to_csv(path_or_buf= None,
#                  sep= ",",
#                  na_rep= "",
#                  float_format= None,
#                  columns= None,
#                  header= True,
#                  index= True,
#                  index_label= None,
#                  mode= "w",
#                  encoding= None,
#                  compression= "infer",
#                  quoting= None,
#                  quotechar= '""',
#                  line_terminator= None,
#                  chunksize= None,
#                  date_format= None,
#                  doublequote= True,
#                  escapechar= None,
#                  decimal= ".")

#====================================
