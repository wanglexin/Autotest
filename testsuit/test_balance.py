
def Age(x):
    while x <= 5:
        print("你的年龄是"+str(x)+"岁,建议保证睡眠12小时以上")
        break
    while 5 < x <= 12:
        print("你的年龄是"+str(x)+"岁,建议保证睡眠9到12小时")
        break
    while 12 < x <= 17:
        print("你的年龄是"+str(x)+"岁,建议保证睡眠8到10小时")
        break
    while 18 < x <= 70:
        print("你的年龄是"+str(x)+"岁,建议保证睡眠7到8小时")
        break
    while x >= 71:
        print("你的年龄是"+str(x)+"岁,建议保证睡眠5.5到7小时")
        break

def personAge():
    x = 20
    Age(x)

personAge()
