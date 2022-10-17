import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TLZ64_0928.csv')
# print(df)

# 篩選資料
date = df['日期']
net_worth = df['淨值']

# 繪圖
plt.plot(date, net_worth, color='#00bd42', linewidth=2)
plt.xlabel('date')
plt.ylabel('Net_worth')
plt.legend(['Net_worth'], loc = 'lower right')
plt.grid(True)

# 顯示圖片
plt.savefig("02_CSV_read_chart.png")
plt.show()
