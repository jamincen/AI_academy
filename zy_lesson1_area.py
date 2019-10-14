# 计算圆面积

# 获取用户输入的数据
r = float(input('请输入圆的半径： '))
# 圆面积,结果保留4位小数
s = 3.14*r**2
print("半径是%s的圆的面积为： %.4f" % (r, s))

#s = round(3.14*r**2, 4)
#ss = lambda r:round(3.14*r**2, 4) 

#print("半径是{}的圆的面积为： {}".format(r, s))
#print("半径是{}的圆的面积为： {}".format(r, ss(r)))
