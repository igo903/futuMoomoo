from futu import *
import pandas as pd
import csv
from matplotlib import pyplot as plt
import datetime


file_path = 'selfQuote.csv'
host = '127.0.0.1'  # Futu Open API的IP地址
port = 11111  # Futu Open API的端口号

# 获取当前日期
now = datetime.datetime.now()

# 计算查询的起始日期
start_date = now - datetime.timedelta(days = 100)

# 转换日期格式为字符串
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = now.strftime('%Y-%m-%d')

myBusket = ''
quote_ctx = OpenQuoteContext(host = host, port = port)

ret, selfQuote = quote_ctx.get_user_security("paperTrade")

if ret == RET_OK:
    print(selfQuote)
    if selfQuote.shape[0] > 0:  # 如果自选股列表不为空
        print(selfQuote['code'][0])    # 取第一条的股票代码
        # print(selfQuote['code'].values.tolist())   # 转为 list
        myBusket = selfQuote['code'].values.tolist()
        
else:
    print('error:', selfQuote)

print(myBusket)


for symbol in myBusket:
    ret, data, page_req_key = quote_ctx.request_history_kline(
        code = symbol,
        start = start_date_str,
        end = end_date_str,
        ktype = KLType.K_DAY,
        autype = AuType.QFQ
    )

    if ret == RET_OK:
        # 处理获取的历史K线数据
        print(f"历史K线数据 for {symbol}:")
        print(data)
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        
        
    else:
        print(f"请求历史K线数据失败 for {symbol}: {ret}, {data}")









ret, data, page_req_key = quote_ctx.request_history_kline('HK.00700', start = start_date_str, end = end_date_str, max_count=100)  # 每页5个，请求第一页
if ret == RET_OK:
    print(111)
    
    
    # df = pd.DataFrame(data)
    # df.to_csv(file_path, index=False)
    # print(data['code'][0])    # 取第一条的股票代码
    # print(data['close'].values.tolist())   # 第一页收盘价转为 list
else:
    print('error:', data)
while page_req_key != None:  # 请求后面的所有结果
    print('*************************************')
    ret, data, page_req_key = quote_ctx.request_history_kline('HK.00700', start = start_date_str, end = end_date_str, max_count=100, page_req_key=page_req_key) # 请求翻页后的数据
    if ret == RET_OK:
        print(111)
        
    else:
        print('error:', data)
print('All pages are finished!')
quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽