high = input("请输入您测量的高压值：")
low = input("请输入您测量的低压值：")
high = int(high)
low = int(low)
if (low > 60 and low < 90) and (high > 90 and high < 140):
    print("您的血压正常，请继续保持健康的生活习惯")
else:
    if low <= 60:
        print("您的低压过低，请注意补充营养。")
    elif high <= 90:
        print("您的高压过低，请加强锻炼，提高心肺功能")
    else:
        print("您的血压已经超标，请尽快就医")






