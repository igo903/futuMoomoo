import pandas as pd
import csv
from matplotlib import pyplot as plt

from futu import *


# df = pd.DataFrame(bid_frame_table)
# df.to_csv(file_path, index=False)

file_path = 'brokers.csv'


quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret_sub, err_message = quote_ctx.subscribe(['HK.03690'], [SubType.BROKER], subscribe_push=False)
# 先订阅经纪队列类型。订阅成功后 OpenD 将持续收到服务器的推送，False 代表暂时不需要推送给脚本
if ret_sub == RET_OK:   # 订阅成功
    ret, bid_frame_table, ask_frame_table = quote_ctx.get_broker_queue('HK.03690')   # 获取一次经纪队列数据
    if ret == RET_OK:
        print(bid_frame_table)
        df = pd.DataFrame(bid_frame_table)
        df.to_csv(file_path, index=False)
    else:
        print('error:', bid_frame_table)
else:
    print('subscription failed')
quote_ctx.close()   # 关闭当条连接，OpenD 会在1分钟后自动取消相应股票相应类型的订阅


   
    

