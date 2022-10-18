import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TLZ64_0928.csv')
# print(df)

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

print(df)

# 篩選資料
date = df['日期']
net_worth = df['淨值']
index_deviation = df['ID']
index_d_m10 = df['ID(-10%)']
index_d_p10 = df['ID(+10%)']

# 繪圖
# plt.plot(date, net_worth, color='#4473c4', linewidth=1)
# plt.plot(date, index_deviation, color='#ff0000', linewidth=1)
# plt.plot(date, index_d_m10, color='#00bd42', linewidth=2)
# plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2)
# plt.xlabel('date')
# plt.ylabel('Net_worth')
# plt.legend(['Net_worth', 'ID(Index_Deviation)', 'ID(-10%)', 'ID(+10%)'], loc = 'lower right')
# plt.grid(True)

# 顯示圖片
# plt.savefig("02_CSV_read_chart.png")
# plt.show()

plt.subplot(2, 2, 1)
plt.plot(date, net_worth, color='#4473c4', linewidth=1)
plt.plot(date, index_deviation, color='#ff0000', linewidth=1)
plt.plot(date, index_d_m10, color='#00bd42', linewidth=2)
plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2)
plt.xlabel('date')
plt.ylabel('Net_worth')
plt.legend(['Net_worth', 'ID(Index_Deviation)', 'ID(-10%)', 'ID(+10%)'], loc = 'lower right')
plt.grid(True)
plt.title("Test 1", {'fontsize':15})  # 設定圖標題及其文字大小

plt.subplot(2, 2, 2)
plt.plot(date, net_worth, color='#4473c4', linewidth=1)
plt.plot(date, index_deviation, color='#ff0000', linewidth=1)
plt.plot(date, index_d_m10, color='#00bd42', linewidth=2)
plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2)
plt.xlabel('date')
plt.ylabel('Net_worth')
plt.legend(['Net_worth', 'ID(Index_Deviation)', 'ID(-10%)', 'ID(+10%)'], loc = 'lower right')
plt.grid(True)
plt.title("Test 2", {'fontsize':15})  # 設定圖標題及其文字大小

plt.subplot(2, 2, 3)
plt.plot(date, net_worth, color='#4473c4', linewidth=1)
plt.plot(date, index_deviation, color='#ff0000', linewidth=1)
plt.plot(date, index_d_m10, color='#00bd42', linewidth=2)
plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2)
plt.xlabel('date')
plt.ylabel('Net_worth')
plt.legend(['Net_worth', 'ID(Index_Deviation)', 'ID(-10%)', 'ID(+10%)'], loc = 'lower right')
plt.grid(True)
plt.title("Test 3", {'fontsize':15})  # 設定圖標題及其文字大小

plt.subplot(2, 2, 4)
plt.plot(date, net_worth, color='#4473c4', linewidth=1)
plt.plot(date, index_deviation, color='#ff0000', linewidth=1)
plt.plot(date, index_d_m10, color='#00bd42', linewidth=2)
plt.plot(date, index_d_p10, color='#ffbf00', linewidth=2)
plt.xlabel('date')
plt.ylabel('Net_worth')
plt.legend(['Net_worth', 'ID(Index_Deviation)', 'ID(-10%)', 'ID(+10%)'], loc = 'lower right')
plt.grid(True)
plt.title("Test 4", {'fontsize':15})  # 設定圖標題及其文字大小

plt.show()