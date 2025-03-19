输入文件中有多个测试数据，每个测试数据占一行，为3个整数y、m、d。输入文件最后一行为3个0，代表输入结束。

输出描述:
对每个测试数据，输出占一行，为一个数值，代表该日期是当年的第几天。

样例输入
2016 3 1
0 0 0

copy

样例输出
61


while True:
  year = input().strip()
  if year == "0 0 0":
    break
  
  years, month, day = map(int, year.split())
  
  days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_month[1] = 29

  years_num = sum(days_month[:month - 1] + day
  print(years_nums)
