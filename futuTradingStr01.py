
from futu import *
import datetime
import matplotlib.pyplot as plt
import pandas as pd


# 初始化FutuOpenD客户端
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

# 设置初始资产
initial_capital = 1000000

# 设置交易参数
buy_threshold = 310  # 买入阈值
sell_threshold = 320  # 卖出阈值
max_buy_quantity = 300  # 最大买入数量

# 设置交易记录列表
trade_records = []

# 获取股票代码
code = 'HK.00700'  # 腾讯股票代码

# 初始化资产和股票数量
capital = initial_capital
stock_quantity = 0

start_date = datetime.datetime(2023, 8, 1)
end_date = datetime.datetime(2023, 11, 1)
delta = datetime.timedelta(days=1)

print("指定日期:", delta)


# 遍历交易日期
while start_date <= end_date:
    # 获取当日股票价格
    ret, data, page_req_key = quote_ctx.request_history_kline(code, start=start_date.strftime('%Y-%m-%d'),
                                                              end = start_date.strftime('%Y-%m-%d'), ktype='K_DAY',
                                                              max_count=1)
    if ret == RET_OK:
        if data.empty:
            # 如果当日没有数据，则跳过
            start_date += delta
            continue

        # 获取当日收盘价
        close_price = data['close'].values[0]

        # 判断是否买入股票
        if close_price < buy_threshold:
            # 计算买入数量
            buy_quantity = min(max_buy_quantity, int(capital / close_price))
            if buy_quantity > 0:
                # 更新资产和股票数量
                capital -= buy_quantity * close_price
                stock_quantity += buy_quantity
                trade_records.append((start_date.strftime('%Y-%m-%d'), '买入', close_price, buy_quantity))
        # 判断是否卖出股票
        elif close_price > sell_threshold and stock_quantity > 0:
            # 更新资产和股票数量
            capital += stock_quantity * close_price
            trade_records.append((start_date.strftime('%Y-%m-%d'), '卖出', close_price, stock_quantity))
            stock_quantity = 0

    # 增加一天
    start_date += delta

# 关闭FutuOpenD客户端
quote_ctx.close()

# 输出交易记录
print('交易记录：')
for record in trade_records:
    print(record)

# 计算期末资产和期末资产收益率
end_capital = capital + stock_quantity * close_price
end_return_rate = (end_capital - initial_capital) / initial_capital * 100

# 输出期末资产和期末资产收益率
print('期末资产：', end_capital)
print('期末资产收益率：', end_return_rate, '%')