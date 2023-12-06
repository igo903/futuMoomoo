import pandas as pd
import csv
from matplotlib import pyplot as plt

from futu import *

history_file = 'history.csv'

trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.history_order_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # 如果订单列表不为空
        print(data['order_id'][0])  # 获取持仓第一个订单号
        print(data['order_id'].values.tolist())  # 转为 list
        
        df = pd.DataFrame(data)
        df.to_csv(history_file, index=False)
        
        
else:
    print('history_order_list_query error: ', data)
trd_ctx.close()