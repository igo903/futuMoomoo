from futu import *
import pandas as pd
import csv
from matplotlib import pyplot as plt


file_path = 'Ticker.csv'
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)


class TickerTest(TickerHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(TickerTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("TickerTest: error, msg: %s" % data)
            return RET_ERROR, data
        print("TickerTest ", data) # TickerTest 自己的处理逻辑
        return RET_OK, data

handler = TickerTest()
quote_ctx.set_handler(handler)  # 设置实时逐笔推送回调

ret, data = quote_ctx.subscribe(['HK.00700'], [SubType.TICKER]) # 订阅逐笔类型，OpenD 开始持续收到服务器的推送
if ret == RET_OK:
    print(data)
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
else:
    print('error:', data)
time.sleep(15)  # 设置脚本接收 OpenD 的推送持续时间为15秒    




# ret_sub, err_message = quote_ctx.subscribe(['HK.00700'], [SubType.TICKER], subscribe_push=False)
# # 先订阅逐笔类型。订阅成功后 OpenD 将持续收到服务器的推送，False 代表暂时不需要推送给脚本

# if ret_sub == RET_OK:  # 订阅成功
#     ret, data = quote_ctx.get_rt_ticker('HK.00700', 10000)  # 获取港股00700最近2个逐笔
#     if ret == RET_OK:
#         print(data)
#         print(data['turnover'][0])   # 取第一条的成交金额
#         print(data['turnover'].values.tolist())   # 转为 list
#         df = pd.DataFrame(data)
#         df.to_csv(file_path, index=False)
#     else:
#         print('error:', data)
# else:
#     print('subscription failed', err_message)
    
    
    




quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽