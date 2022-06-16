import pickle
import os
yn = input("are you using our app for first time?(y,n) :")
if yn == "y":
    money = input("Deposit Money :")
    print(f"you have {money} dollars on acc")
    yesorno = input("do you want to get money out ? (yes,no) :")
    if yesorno == "yes" :
        getout = input("how much money you want to get out? :")
        money = int(money) - int(getout)
        pickle.dump(money, open("info.dat","wb"))
        print(f"you have {money} dollars on acc")
    else :
        print("ending Porgram...")
        pickle.dump(money, open("info.dat","wb"))
elif yn == "n":
    money = pickle.load(open("info.dat","rb"))
    print(f" you have {money} dollars on acc")
    addornot = input("Do you want to add or not? : ")
    if addornot == "add":
        add = input("Input money :")
        money = int(money) + int(add)
        pickle.dump(money, open("info.dat","wb"))
        print(f"now you have {money} dollars on acc")
    elif addornot == "not":
        getout = input("how much money you want to get out? :")
        money = int(money) - int(getout)
        pickle.dump(money, open("info.dat","wb"))
        print(f" you have {money} dollars on acc")
    else :
        print(f"Error argument {addornot} is undefined")
else :
    print(f"Invalid Option {yn} : is undefined")