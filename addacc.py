import pandas as pd
import random
y=["107002","107003","107004","107005","107006"]
x=random.choice(y)
def addacc():
    new_data={"name": input("enter your name"),"acc_number": x}
    df=pd.DataFrame([new_data])
    df.to_csv("bankdetail.csv", mode='a', index=False, header=False)#to_csv in pandas is used to export
    print("\n",df)