weight = input("请输入您的体重(kg):")
height = input("请输入您的身高(m):")
#体重/身高的平方，pow(4,2) = 16
bmi = int(weight) / pow(float(height),2)
print(bmi)

if bmi <= 18.4:
    print("评测结果:偏瘦")
elif bmi > 18.4 and bmi <= 23.9:
    print("评测结果:正常")
elif bmi > 23.9 and bmi <= 27.9:
    print("评测结果:过重")
else:
    print("评测结果:肥胖")
