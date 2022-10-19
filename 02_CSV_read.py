import pandas as pd
import matplotlib.pyplot as plt

class market_index:
    def index_deviation(df):
        del df['漲跌幅(%)'] #刪除列
        # 移動平均線
        # 分別計算30天與72天的移動平均線，求多列的平均值
        df['MA_30'] = df['淨值'].rolling(30, min_periods=1).mean()
        df['MA_72'] = df['淨值'].rolling(72, min_periods=1).mean()
        df['ID'] = df[['MA_30', 'MA_72']].mean(axis=1)
        # 計算ID上下%
        df['ID(-10%)'] = df['ID']-df['ID']*(10/100)
        df['ID(+10%)'] = df['ID']+df['ID']*(10/100)
        # 計算ID-淨值分離%
        df['ID-淨值分離%'] = (df['淨值']-df['ID'])/df['ID']
        df['ID-MA_30分離%'] = (df['淨值']-df['MA_30'])/df['MA_30']
        df['ID-淨值分離%'] = df['ID-淨值分離%'].apply(lambda x: format(x, '.2%'))     # 修改成%
        df['ID-MA_30分離%'] = df['ID-MA_30分離%'].apply(lambda x: format(x, '.2%'))   # 修改成%
        return df
    
    
    
    def image(df):
        # 篩選資料
        date = df.index
        net_worth = df['淨值']
        index_deviation = df['ID']
        index_d_m10 = df['ID(-10%)']
        index_d_p10 = df['ID(+10%)']
        # 繪圖
        return (
            plt.plot(date, net_worth, color='#4473c4', linewidth=1),
            plt.plot(date, index_deviation, color='#ff0000', linewidth=1),
            plt.plot(date, index_d_m10, color='#00bd42', linewidth=2),
            plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2),
            plt.xlabel('date'),
            plt.ylabel('Net worth'),
            plt.legend(['Net worth', 'ID', 'ID(-10%)', 'ID(+10%)'], bbox_to_anchor=(0.9, 0.5, 0.3, 0.2), loc = 'right'),
            plt.grid(True)
        )
        

df = pd.read_csv('TLZ64_0928.csv')
df['日期'] = pd.to_datetime(df['日期'])
dr = market_index.index_deviation(df)
df = df.set_index('日期')
df_2022 = df['2022']
df_1month = df.head(30)
df_3month = df.head(90)

# print('=============2022=============')
# print(df_2022)
# print(df_2022.index)
# print('=============1 month=============')
# print(df_1month)
# print(df_1month.index)
# print('=============3 month=============')
# print(df_3month)

# print(df)
# df2022 = market_index.index_deviation(df_2022)
# df1month = market_index.index_deviation(df_1month)
# df3month = market_index.index_deviation(df_3month)
# print('=============2022=============')
# print(df2022)
# print('=============1 month=============')
# print(df1month)
# print('=============3 month=============')
# print(df3month)


# market_index.image(dfid)
# plt.show()
# print(df.std())
plt.figure(figsize=(18,10))
plt.subplot(2, 2, 1)
market_index.image(df_2022)
plt.title("2022", {'fontsize':15})       # 設定圖標題及其文字大小
plt.xticks(rotation = 45, fontsize = 10) # 設定 x 軸顯示角度與文字大小

plt.subplot(2, 2, 2)
market_index.image(df_1month)
plt.title("1 month", {'fontsize':15})    # 設定圖標題及其文字大小
plt.xticks(rotation = 45, fontsize = 10) # 設定 x 軸顯示角度與文字大小

plt.subplot(2, 2, 3)
market_index.image(df_3month)
plt.title("3 month", {'fontsize':15})    # 設定圖標題及其文字大小
plt.xticks(rotation = 45, fontsize = 10) # 設定 x 軸顯示角度與文字大小

# x = MultipleLocator(10)
# y = MultipleLocator(15)
# ax = plt.gca()
# ax.xaxis.set_majour_locator(MultipleLocator(10))
# ax.yaxis.set_majour_locator(y)
# plt.get_current_fig_manager().window.state('zoomed') # 將圖放到最大
plt.subplots_adjust(
    left=0.07,
    bottom=0.1,
    right=0.9,
    top=0.95,
    wspace=0.32,
    hspace=0.35
    )
    
# # 顯示圖片

plt.savefig("02_CSV_read_chart.png")


plt.show()

# plt.subplot(2, 2, 1)
# plt.plot(date, net_worth, color='#4473c4', linewidth=1)
# plt.plot(date, index_deviation, color='#ff0000', linewidth=1)
# plt.plot(date, index_d_m10, color='#00bd42', linewidth=2)
# plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2)
# plt.xlabel('date')
# plt.ylabel('Net_worth')
# plt.legend(['Net_worth', 'ID(Index_Deviation)', 'ID(-10%)', 'ID(+10%)'], loc = 'lower right')
# plt.grid(True)
# plt.title("Test 1", {'fontsize':15})  # 設定圖標題及其文字大小

# plt.subplot(2, 2, 2)
# plt.plot(date, net_worth, color='#4473c4', linewidth=1)
# plt.plot(date, index_deviation, color='#ff0000', linewidth=1)
# plt.plot(date, index_d_m10, color='#00bd42', linewidth=2)
# plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2)
# plt.xlabel('date')
# plt.ylabel('Net_worth')
# plt.legend(['Net_worth', 'ID(Index_Deviation)', 'ID(-10%)', 'ID(+10%)'], loc = 'lower right')
# plt.grid(True)
# plt.title("Test 2", {'fontsize':15})  # 設定圖標題及其文字大小

# plt.subplot(2, 2, 3)
# plt.plot(date, net_worth, color='#4473c4', linewidth=1)
# plt.plot(date, index_deviation, color='#ff0000', linewidth=1)
# plt.plot(date, index_d_m10, color='#00bd42', linewidth=2)
# plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2)
# plt.xlabel('date')
# plt.ylabel('Net_worth')
# plt.legend(['Net_worth', 'ID(Index_Deviation)', 'ID(-10%)', 'ID(+10%)'], loc = 'lower right')
# plt.grid(True)
# plt.title("Test 3", {'fontsize':15})  # 設定圖標題及其文字大小

# plt.subplot(2, 2, 4)
# plt.plot(date, net_worth, color='#4473c4', linewidth=1)
# plt.plot(date, index_deviation, color='#ff0000', linewidth=1)
# plt.plot(date, index_d_m10, color='#00bd42', linewidth=2)
# plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2)
# plt.xlabel('date')
# plt.ylabel('Net_worth')
# plt.legend(['Net_worth', 'ID(Index_Deviation)', 'ID(-10%)', 'ID(+10%)'], loc = 'lower right')
# plt.grid(True)
# plt.title("Test 4", {'fontsize':15})  # 設定圖標題及其文字大小

# plt.show()