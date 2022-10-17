import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TLZ64_0928.csv')
# print(df)

del df['漲跌幅(%)'] #刪除列

# 移動平均線
# 分別計算30天與72天的移動平均線，求多列的平均值
df['MA_32'] = df['淨值'].rolling(32, min_periods=1).mean()
df['MA_72'] = df['淨值'].rolling(72, min_periods=1).mean()
df['ID'] = df[['MA_32', 'MA_72']].mean(axis=1)

print(df)

# # 篩選資料
# date = df['日期']
# net_worth = df['淨值']

# # # 繪圖
# # plt.plot(date, net_worth, color='#00bd42', linewidth=2)
# # plt.xlabel('date')
# # plt.ylabel('Net_worth')
# # plt.legend(['Net_worth'], loc = 'lower right')
# # plt.grid(True)

# # # 顯示圖片
# # plt.savefig("02_CSV_read_chart.png")
# # plt.show()

# datetime = pd.to_datetime(df['日期'])
# print(datetime)