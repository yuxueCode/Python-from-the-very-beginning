# 函数的使用技巧-2
# 1. 序列传参
def calc(a, b, c):
    return (a + b) * c


l = [1, 5, 10]
print(calc(*l))


# 2. 字典传参
def health_check(name, age, height, weight, hr, hbp, lbp, glu):
    print(name)
    print(height)
    print(hr)
    print("您的健康状况良好")


param = {"name": "张三", "height": 178, "age": 32, "weight": 85.6, "hr": 70, "hbp": 120, "lbp": 80, "glu": 4.3}
health_check(**param)

# 3. 返回值包含多个数据
def get_detail_info():
    dict1 = {
        "employee" : [
            {"name":"张三", "salary":1800},
            {"name":"李四", "salary":2000}
        ],
        "device" : [
            {"id" : "8837120" , "title" : "XX笔记本"},
            {"id" : "3839011" , "title" : "XX台式机"}
        ],
        "asset" :[{},{}],
        "project" :[{},{}]
    }
    return dict1
print(get_detail_info())
d = get_detail_info()
sal = d.get("employee")[0].get("salary")
print(sal)