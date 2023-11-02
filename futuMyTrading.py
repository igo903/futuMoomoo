import time
import matplotlib.pyplot as plt
import pandas as pd
from futu import *

############################ 全局变量设置 ############################
FUTUOPEND_ADDRESS = '127.0.0.1'  # Futu OpenD 监听地址
FUTUOPEND_PORT = 11111  # Futu OpenD 监听端口

TRADING_ENVIRONMENT = TrdEnv.SIMULATE  # 交易环境：真实 / 模拟
TRADING_MARKET = TrdMarket.HK  # 交易市场权限，用于筛选对应交易市场权限的账户
TRADING_PWD = '903726'  # 交易密码，用于解锁交易
TRADING_PERIOD = KLType.K_1M  # 信号 K 线周期
TRADING_SECURITY = 'HK.00700'  # 交易标的
FAST_MOVING_AVERAGE = 1  # 均线快线的周期
SLOW_MOVING_AVERAGE = 3  # 均线慢线的周期

quote_context = OpenQuoteContext(host=FUTUOPEND_ADDRESS, port=FUTUOPEND_PORT)  # 行情对象
trade_context = OpenSecTradeContext(filter_trdmarket=TRADING_MARKET, host=FUTUOPEND_ADDRESS, port=FUTUOPEND_PORT, security_firm=SecurityFirm.FUTUSECURITIES)  # 交易对象，根据交易品种修改交易对象类型


ret, data, page_req_key = quote_context.request_history_kline('HK.00700', start='2023-01-01', end='2023-10-31', ktype=KLType.K_DAY)  # 每页5个，请求第一页
df = pd.DataFrame(data)


if ret == RET_OK:
    print(data)
else:
    print('error:', data)
print('All pages are finished!')
quote_context.close() # 结束后记得关闭当条连接，防止连接条数用尽



df['time_key'] = pd.to_datetime(df['time_key'])
df.set_index('time_key', inplace=True)


# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(df.index, df['close'], width=0.8, color='blue')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Tencent Stock Day Chart (2023)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
