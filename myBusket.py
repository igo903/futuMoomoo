from futu import *
import pandas as pd
import csv
from matplotlib import pyplot as plt
import datetime
import xlsxwriter


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
kline_data = []
quote_ctx = OpenQuoteContext(host = host, port = port)
ret, data = quote_ctx.get_user_security("paperTrade")

if ret == RET_OK:
    myBusket = data['code'].values.tolist()
    
else:
    print('error:', data)
    
all_stock_data = pd.DataFrame()
writer = pd.ExcelWriter('stock_data.xlsx', engine='xlsxwriter')

for symbol in myBusket:
    ret, data, page_req_key = quote_ctx.request_history_kline(
        code=symbol,
        start = start_date_str,  # 修改开始日期
        end = end_date_str,    # 修改结束日期
        ktype=KLType.K_DAY,
        autype=AuType.QFQ
    )
    
    if ret == RET_OK:
        
        # 将获取的历史K线数据添加到DataFrame中
        stock_data = pd.DataFrame(data)
        stock_data['symbol'] = symbol  # 添加股票代码列
        all_stock_data = pd.concat([all_stock_data, stock_data], ignore_index = True)
        
        stock_data.to_excel(writer, sheet_name = symbol, index = False) 

        
        print('ooooooooop')

    else:
        print(f"请求历史K线数据失败 for {symbol}: {ret}, {data}")
        

# 关闭连接
quote_ctx.close()


writer._save()
writer.close()

# 将数据输出到CSV文件
output_csv_path = 'selected_stock_data.csv'
all_stock_data.to_csv(output_csv_path, index=False)
print(f"数据已保存到 {output_csv_path}")