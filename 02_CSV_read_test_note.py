from operator import index
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TLZ64_0928.csv')
# print(df)

# # 篩選資料
# date = df['日期']
# net_worth = df['淨值']

# # 繪圖
# plt.plot(date, net_worth)
# plt.xlabel('date')
# plt.ylabel('Net_worth')
# plt.legend(['Net_worth'], loc = 'lower right')
# plt.grid(True)

# # 顯示圖片
# plt.show()

# =================================================
# 轉成list的方式讀取

# dftolist = df.values.tolist() #整個轉為list
# dftolist1 = list(df.iloc[:, 0]) #取第二行轉為list
# dftolist2 = list(df.iloc[:, 1]) #取第二行轉為list
# dftolistdate = list(df.loc[:, '日期']) #取欄位名稱date的行為轉成list

# print(type(dftolist), dftolist)
# print(type(dftolist1), dftolist1)
# print(type(dftolist2), dftolist2)
# print(type(dftolistdate), dftolistdate)

# plt.plot(dftolist1, dftolist2)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('Date to oprice')
# plt.legend(['Net_worth'], loc = 'lower right')
# plt.show()

# ======================================================
# result = df.loc[x, y].head(10)
# result.set_index('日期', inplace=True)
 
# chart = result.plot(title='日期淨值',  #圖表標題
#                     xlabel='日期',  #x軸說明文字
#                     ylabel='淨值',  #y軸說明文字
#                     legend=True,  # 是否顯示圖例
#                     figsize=(10, 5))  # 圖表大小
# plt.show()



# rows = (df['年別'] == 2019) & (df['縣市別'] == '臺北市')
# columns = ['細分', '1月', '2月', '3月']
# result = df.loc[rows, columns].head(10)
# result.set_index('細分', inplace=True)
 
# chart = result.plot(title='2019年臺北市各景點旅客人數',  #圖表標題
#                     xlabel='細分(景點名稱)',  #x軸說明文字
#                     ylabel='人數',  #y軸說明文字
#                     legend=True,  # 是否顯示圖例
#                     figsize=(10, 5))  # 圖表大小
# plt.show()

# ===================================================
# 日期轉換
# datetime = pd.to_datetime(df['日期'])
# print(datetime)

# time_start = '2022-10-01'
# time_end = '2022-10-11'

# time1 = pd.to_datetime(time_start)
# time2 = pd.to_datetime(time_end)
# delta_time = time2-time1

# delta_time_days = delta_time.days

# print(delta_time_days)

# ====================================================
# 設日期為index
# df = df.set_index('日期')
# print(df.head(2))
# print(df.tail(2))
# print(df.shape)

# ===============================================
# 固定時間間隔求均值得方法 (移動平均)
# 若index是時間序列，就不用轉換datetime；但是如果時間序列存在表格中的某一列，則可將之設為index
# df = df.set_index('日期')
# group = df.groupby(['日期', '淨值'])
# f = pd.DataFrame(group['淨值'].sum().rolling(5, min_periods=1).mean())

# print(f)

# ===============================================
# 刪除列的方式
# del df['漲跌幅(%)'] #可刪除列
# df.drop(columns='漲跌幅(%)')
# df.pop('漲跌幅(%)')

# 移動平均線
# 我們分別計算7天,15天與30天的移動平均線
# df['MA_7'] = <- 會直接新增列
# df['MA_7'] = df['淨值'].rolling(7, min_periods=1).mean()
# df['MA_15'] = df['淨值'].rolling(15, min_periods=1).mean()
# df['MA_30'] = df['淨值'].rolling(30, min_periods=1).mean()

# print(df)
# df.to_csv('TLZ64_0928_MA.csv', index=False)

# =====================================================
# 1. 載入套件。

import numpy as np                # 資料處理套件
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
# 2. 載入資料。

TRA = pd.read_csv("passenger number of TRA(105-106).csv")
TRA.head(3)    # 顯示前3筆資料

# 3. 資料操作。
# 由於原資料的載客數單位為人次，為利視覺化結果簡潔，將載客數改為百萬計

pr = [None] * len(TRA["passenger"])       # 建立一個空列表，數量為載客數欄位資料的數量

# 以for迴圈逐一將載客數資料自左向右取5個字元
for i in range(len(TRA["passenger"])):     
    pr[i] = TRA["passenger"][i][:5]

# 以for迴圈逐一將載客數資料中的","替換成"."
for i in range(len(pr)):
    pr[i] = pr[i].replace(",", ".")
    
# 將原資料替換掉，並重新命名欄位名稱  
TRA["passenger"] = pr
TRA.rename(columns = {"passenger" : "passenger(million)"}, inplace = True)


# 4. 開始畫圖。

year = str(np.unique(TRA["year"]))   # 將年份資料單獨取出
year = year.split(" ")               # 以空白字元分隔年分資料

# 畫第一張圖，位於左上角
# 其中pd.DataFrame(資料,dtype=np.float)為將載客數字串類別更改為float類別
# 其中TRA[TRA.station == "Taipei"]["passenger(million)"]為擷取出台北站資料，再擷取出載客數欄位資料
plt.subplot(2, 2, 1)                 # plt.subplot(列數, 行數, 圖形編號)設定第一張圖位置
plt.plot(year, pd.DataFrame(TRA[TRA.station == "Taipei"]["passenger(million)"],dtype=np.float)
        ,"r")                         # plt.plot(x軸資料, y軸資料, 線顏色)
plt.title("Taipei", {'fontsize':15})  # 設定圖標題及其文字大小

# 畫第二張圖，位於右上角
plt.subplot(2, 2, 2)
plt.plot(year, pd.DataFrame(TRA[TRA.station == "Taoyuan"]["passenger(million)"],dtype=np.float)
        ,"g--")
plt.title("Taoyuan", {'fontsize':15})

# 畫第三張圖，位於左下角
plt.subplot(2, 2, 3)
plt.plot(year, pd.DataFrame(TRA[TRA.station == "Zhongli"]["passenger(million)"],dtype=np.float)
        ,"b-.")
plt.title("Zhongli", {'fontsize':15})

# 畫第四張圖，位於右下角
plt.subplot(2, 2, 4)
plt.plot(year, pd.DataFrame(TRA[TRA.station == "Tainan"]["passenger(million)"],dtype=np.float)
        ,"m:")
plt.title("Tainan", {'fontsize':15})        
        

# 儲存圖檔
plt.savefig("Passengers of the top 4 TRA station.jpg",   # 儲存圖檔
            bbox_inches='tight',               # 去除座標軸占用的空間
            pad_inches=0.0)                    # 去除所有白邊
plt.close()      # 關閉圖表      