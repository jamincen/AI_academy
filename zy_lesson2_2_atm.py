### 作业2：实现ATM机功能

#查询余额 check
#存款 deposit
#取款 withdrawal
#退出 quit
cash = 0

def check():
    print("       当前余额$：", cash)

def deposit():
    global cash
    cash_in = (input("      存款金额$："))
    
    # 输入异常处理
    try:
        float(cash_in)
    except ValueError:
        print("        输入有误！")
        return
        
    cash = cash + float(cash_in)

def withdrawal():
    global cash
    cash_out = input("      取款金额$：")

    # 输入异常处理
    try:
        float(cash_out)
    except ValueError:
        print("        输入有误！")
        return
    cash = cash - float(cash_out)

def quitt():
    print("""
        ***************
        欢迎使用，再见！
        ***************
        """)
    
def busy():
    print("""
    1 查询余额
    2 存款
    3 取款
    4 退出
    """)
    
print("""
    ************************
    Welcome to the CJM Bank!
    ************************
    """)

i = 1
while i == 1:
    print("""
        ---------------------
        """)
    busy()
    business = (input("    请选择要办理业务的编号（1、2、3、4）："))

    # 输入异常处理
    try:
        int(business)
    except ValueError:
        business = 0
        
    business = int(business)
    print("""
    ---------------------------------------
        """)
    if business == 1:
        check()
    
    elif business == 2:
        deposit()
    
    elif business == 3:
        withdrawal()
    
    elif business == 4:
        quitt()
        i = 0
    else:
        print("    ***业务编号输入有误，请重新输入！***")


    
    
