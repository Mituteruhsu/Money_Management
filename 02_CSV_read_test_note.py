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