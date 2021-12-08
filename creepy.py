import tushare as ts

ts.set_token('616765b12bb62b2d60245b00186aa9ac186c8234fe8d59b2787deb95')
pro = ts.pro_api()

df = ts.pro_bar(ts_code='000001.SZ', adj='qfq')
# df = pro.query('daily', ts_code='000001.SZ')
# a = ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')

print(type(df))
print(df)
df.to_csv("00001.csv")
