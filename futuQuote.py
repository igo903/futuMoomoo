from futu import *
import pandas as pd
import csv
from matplotlib import pyplot as plt


file_path = 'futuQuote.csv'
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret, data = quote_ctx.get_market_snapshot(['SH.600000', 'HK.00700'])


if ret == RET_OK:
    
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    
    print(data)
    print(data['code'][0])    # 取第一条的股票代码
    print(data['code'].values.tolist())   # 转为 list
else:
    print('error:', data)
quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽