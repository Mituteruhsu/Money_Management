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
            plt.legend(['Net worth', 'ID', 'ID(-10%)', 'ID(+10%)'], bbox_to_anchor=(0.9, 0.5, 0.3, 0.2), loc = 'right'),  # bbox 會將標籤設在圖外
            plt.grid(True)
        )
        
df = pd.read_csv('TLZ64_0928.csv')
df['日期'] = pd.to_datetime(df['日期'])
dr = market_index.index_deviation(df)
df = df.set_index('日期')
df_2022 = df['2022']
df_1month = df.head(30)
df_3month = df.head(90)

plt.figure(figsize=(18,10))  # 設定圖像大小

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

# 修改視窗顯示大小及格式
plt.get_current_fig_manager().window.state('zoomed') # 將視窗放到最大
plt.subplots_adjust(
    left=0.07,
    bottom=0.1,
    right=0.9,
    top=0.95,
    wspace=0.32,
    hspace=0.35
    )
    
# # 儲存/顯示圖片
# plt.savefig("02_CSV_read_chart.png")
plt.show()