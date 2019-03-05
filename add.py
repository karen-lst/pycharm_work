# 实现用户输入两个数字，计算两个数的和并打印出来

# num1 = input("请输入第一个数字：")
# num2 = input("请输入第二个数字：")
# sum = float(num1) + float(num2)
# # print(sun)
# print('数字 {0} 和 数字 {1} 的相加结果是：{2}'.format(num1, num2, sum))

# 实现用户输入一个数，计算这个数的平方根

# num1 = float(input("请输入一个数："))
# num2 = num1 ** 0.5
# print("{0} 的平方根是{1}".format(num1,num2))

# 实现解二元一次方程 ax**2 + bx + c = 0

# import cmath

# a = float(input("请输入a："))
# b = float(input("请输入b："))
# c = float(input("请输入c："))
#
# d = (b**2) - (4 * a * c)
# sol1 = (-b - cmath.sqrt(d)) / (a * 2)
# sol2 = (b + cmath.sqrt(d)) / (a * 2)
# print('結果為{}、{}'.format(sol1,sol2))

# 计算三角形的面积

# a = float(input("请输入三角形的第一条边长："))
# b = float(input("请输入三角形的第二条边长："))
# c = float(input("请输入三角形的第三条边长："))
# d = (a+b+c)/2
# s = (d*(d-a)*(d-b)*(d-c)) ** 0.5
# print("该三角形的面积是：%0.2f" %s)

# 如何生成一个随机数

# import random
#
# print(random.randint(0,9))

# 摄氏温度转换为华氏温度
#
# celsius = float(input("请输入摄氏温度："))
# fahrenheit = (celsius * 1.8) + 32
# print("%0.1f 摄氏温度对应的华氏温度为 %0.1f" % (celsius, fahrenheit))

# 升级版，带符号的温度转换

# s = input("请输入带符号的温度值：")
# if s[-1] in ['C','c']:
#     f = 1.8*eval(s[0:-1]) + 32
#     print("%0.1f 摄氏度转换华氏度为：%0.1f" %(eval(s[0:-1]), f))
# elif s[-1] in ['F', 'f']:
#     c = (eval(s[0:-1]) - 32) / 1.8
#     print("%0.1f 华氏度转换摄氏度为：%0.1f" %(eval(s[0:-1]), c))
# else:
#     print("输入格式有误")

# 交换变量

# x = float(input("请输入x的值："))
# y = float(input("请输入y的值："))
# # z = x
# # x = y
# # y = z
# x,y = y,x
# print("x的值为：%0.1f，y的值为：%0.1f" %(x, y))

# 判断数字是正数、负数、还是0

# while True:
#     try:
#         number = float(input("请输入一个数字："))
#         if number == 0:
#             print(" 0")
#         elif number < 0:
#             print("负数")
#         else:
#             print("正数")
#         break
#     except ValueError:
#         print("输入无效，请输入数字")

# def is_number(s):
#     try:
#         # print('是数字：%0.1f' %float(s))
#         float(s)
#         return True
#     except ValueError:
#         # print('不是数字')
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#
#     return False
#
# print(is_number(4))
# print(is_number(-3.14))
# print(is_number('e'))
# print(is_number('四'))
# print(is_number('五'))
# print(is_number('๒๒'))
# print(is_number('٥٥٥'))

# 判断奇数、偶数

# def my_number(n):
#     try:
#         if n%2 == 0:
#             return '偶数'
#         else:
#             return '奇数'
#     except TypeError:
#         return '输入无效'
#
#
# print(my_number('dsa'))
# print(my_number(4))
# print(my_number(5))

# number = int(input('请输入一个数：'))
# if number % 2 == 0:
#     print('{}是偶数'.format(number))
# else:
#     print('{}是奇数'.format(number))

# 判断一个年份是否是闰年
#
# try:
#     year = input('年份：')
#     if (year[-1:-3] == '00') and (int(year) % 400 == 0) :
#         print('{}是闰年'.format(year))
#     elif (int(year) % 4) == 0:
#         print('{}是闰年'.format(year))
#     else:
#         print('{}不是闰年'.format(year))
# except:
#     print('输入的年份无效')

# import calendar
# print(calendar.isleap(2000))
# print(calendar.isleap(2011))

# 取最大值

# print(max(11, 2, 3, -4, 0))
# print(max([1, 3, 5]))
# print(max((1, 3)))
# print(max('a', 's', 'f'))

# 质数判断

# num = int(input('数字：'))
# i = 2
# while i<number:
#     if number % i ==0:
#         print('{}不是质数'.format(number))
#         break
#     i +=1
# print('{}是质数'.format(number))

# 输出指定范围的质数

# n = int(input("区间最小值："))
# m = int(input("区间最大值："))
#
# for num in range(n,m+1):
#     if num >1:
#         for i in range(2,num):
#             if num%i == 0:
#                 break
#         else:
#             print(num)

# 阶乘

# num = int(input('数字：'))
# s =1
# if num < 0:
#     print('负数没有阶乘')
# else:
#     for i in range(1,num+1):
#         s = s*i
#     print(s)

# 九九乘法表
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(j,i,i*j),end='')
#     print()

# 斐波那契数列

# n = int(input('你要多少个数字：'))
# count=0
# a,b=0,1
# while count < n:
#     print(a,end=',')
#     a,b=b,a+b
#     count += 1

# 阿姆斯特朗数
#
# num = input("数字：")
# c = len(num)
# s = 0
# for i in num:
#     s += int(i) ** c
# if s == int(num):
#     print(num,'是一个阿姆斯特朗数')
# else:
#     print(s)

# 指定范围内的阿姆斯特朗数
#
# lower = int(input("最小值："))
# upper = int(input("最大值："))
#
# for i in range(lower,upper):
#     s = 0
#     c = len(str(i))
#     for j in str(i):
#         s += int(j) ** c
#     if s == i:
#         print(i)

# 十进制、二进制、八进制、十六进制互相转换
#
# dec = int(input("number:"))
#
# print('十进制：',dec)
# print('二进制：',bin(dec))
# print('八进制：',oct(dec))
# print('十六进制：',hex(dec))

# ASCII 码与字符互相转换

# c = input("字符：")
# a = int(input("ASCII："))
#
# print('ASCII:',ord(c))
# print('字符',chr(a))