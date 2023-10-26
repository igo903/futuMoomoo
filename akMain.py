import akshare as ak

macro_bank_usa_interest_rate_df = ak.macro_bank_usa_interest_rate()
# print(macro_bank_usa_interest_rate_df)


option_finance_board_df = ak.option_finance_board(symbol="中证1000股指期权", end_month="2312")
print(option_finance_board_df)