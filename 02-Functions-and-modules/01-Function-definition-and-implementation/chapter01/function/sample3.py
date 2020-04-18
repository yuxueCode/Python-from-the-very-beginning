# 函数的返回值
# 参数是函数的输入数据,而返回值则是函数的输出结果.
# return 不是必须的,但是return语句执行后,函数将中断执行
def calc_exchange_rate(amt , source , target):
    if source == "CNY" and target =="USD":
        #6.7516 : 1
        result = amt / 6.7516
        # print(result)

        print("汇率计算成功")
        return result

r = calc_exchange_rate(100 , "EUR" , "USD")
print(r)