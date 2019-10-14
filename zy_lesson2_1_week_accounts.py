### 作业1：实现一周记账功能
# in: 收入
# out: 支出
# balance: 余额
sa = []
sb = []
sc = {}
weeks = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# get daiy in and out

for i in weeks:
    ina = 0
    while ina == 0:
        a = input("please enter {} <in>: ".format(i))

        try:
            float(a)
            ina = 1
        except:
            print("--enter error,retry!--")
            ina = 0
            
    inb = 0       
    while inb == 0:
        b = input("please enter {} <out>: ".format(i))
   
        try:
            float(b)
            inb = 1
        except:
            print("--enter error,retry!--")
            inb = 0
        
        
    a = float(a)
    b = float(b)
    # daily balance
    c = a-b
    
    ab = "{} balance".format(i)
    sa.append(a)
    sb.append(b)
    sc[ab] = c

# final balance   
final_balance = sum([x for x in sc.values()])

print("")
print("7 days in and out and balance：")
print("")
print("7 days in:", sa)
print("")
print("7 days out:", sb)
print("")
print("daily balance:", sc)
print("")
print("final balance:", final_balance)
