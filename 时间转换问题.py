蓝桥杯（省赛）小蓝要和朋友合作开发一个时间显示的网站。在服务器上，朋友已经获取了当前的时间，用一个整数表示，值从1970年1月1日 00：00: 00，到当前时刻经过的毫秒数。现在，小蓝要在客户端显示出这个时间。小蓝不用显示出年月日，只需要显示出时分秒即可，毫秒也不用显示，直接舍去即可。

1小时 = 60分钟 = 3600秒
1秒 = 1000毫秒
1毫秒 = 1000微秒
#把这些数值格式化成两位，不足两位自动在第一位补0.使用  f"[hours : 02d]" 方法
解题过程：
n = int(input())
total_seconds = n // 1000
total_seconds %= 86400
hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining //60
seconds = remaining % 60
print(f "{hours:02d} : {minutes : 02d} : {secomds : 02d}")
