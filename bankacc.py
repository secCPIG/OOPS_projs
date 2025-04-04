import pandas as pd
import random
import csv
class account:
    def __init__(self,name:str,acc_number:str):
        self.__name=name
        self.__acc_number=acc_number

    def name(self):
        return self.__name
    def acc_number(self):
        return self.__acc_number
    def get_details_pandas():
        dt=pd.read_csv("bankdetail.csv")
        print(dt)

    def __repr__(self):
        return f"Account Name: {self.__name}\nAccount Number: {self.__acc_number}"
detail1=account("Aavash Chhetri","107001")
class  bank():
    info=[]
    @staticmethod
    def createacc():
        y=["107002","107003","107004","107005","107006"]
        x=random.choice(y)
        new_data={"name": input("enter your name"),"acc_number": x,"balance": int(input("enter initial deposit amount: "))}
        df=pd.DataFrame([new_data])
        df.to_csv("bankdetail.csv", mode='a', index=False, header=False)#to_csv in pandas is used to export dataframe to the csv file
    @staticmethod
    def deposit_and_withdrawl():
        account_name=input("enter account name: ")
        df=pd.read_csv("bankdetail.csv")
        found=False
        service=input("enter service(deposit/withdrawl): ")
        for i,row in df.iterrows():
            if row["account name"]==account_name:
                if service=="deposit":
                    after_deposit=int(input("enter deposit amount: "))
                    df.at[i,"current balance"] += after_deposit #at[index/row,column/heading name]>>update balance
                elif service=="withdrawl":
                    after_withdrawl=int(input("enter withdrawl amount: "))
                    df.at[i,"current balance"] -= after_withdrawl
                    if after_withdrawl > df.at[i, "current balance"]: 
                        print("insufficient amount!!")
                else:
                    print("invalid service")
                found=True
                break
        if found:
            print("Account was found")
            if service=="deposit":
                print("deposit successful\n")
                print("current balance: ",df.at[i,"current balance"])
            elif service=="withdrawl":
                print("withdrawl successful\n")
                print("current balance: ",df.at[i,"current balance"])
            else:
                print("cannot proceed due to invalid service")
            df.to_csv("bankdetail.csv",index=False)
        else:
            print("""error finding account!!
                   plz recheck your account name""")
        
what_to_do=input("""Welcome to Aavash Development Bank\n
                     How can we help you??(services: create account,check details,deposit/withdrawl)""")

if what_to_do=="create account":
    bank.createacc()
elif what_to_do=="check details":
    account.get_details_pandas()
elif what_to_do=="deposit/withdrawal":
    bank.deposit_and_withdrawl()
else:
    print("INVALID SERVICE PROVIDED")    


