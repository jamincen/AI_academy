### 作业1：实现一周记账功能
# in,out,balance
sa = []
sb = []
sc = {}
weeks = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# get daiy in and out
for i in weeks:
    a = input("please enter {} 'in': ".format(i))
    b = input("please enter {} 'out': ".format(i))
    
    if a == "":
        a = 0
        print("---enter nothing---")
    if b == "":
        b = 0
        print("---enter nothing---")
        
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
