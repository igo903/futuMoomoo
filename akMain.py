import akshare as ak
import pandas as pd
import csv
from matplotlib import pyplot as plt

file_path = 'Chinesebrokers.csv'
zz_path = 'zz1000.csv'
zz_index ='zzindex.csv'


stock_us_daily_df = ak.stock_us_daily(symbol="SPY", adjust="")
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000852", period="daily", start_date="20170301", end_date='20210907', adjust="")
stock_qsjy_em_df = ak.stock_qsjy_em(date="20200430")
index_stock_cons_weight_csindex_df = ak.index_stock_cons_weight_csindex(symbol="000852")




zz = pd.DataFrame(index_stock_cons_weight_csindex_df)
zz.to_csv(zz_path, index=False)

df = pd.DataFrame(stock_qsjy_em_df)
df.to_csv(file_path, index=False)




# print(stock_qsjy_em_df)
print(index_stock_cons_weight_csindex_df)
print(stock_us_daily_df)
