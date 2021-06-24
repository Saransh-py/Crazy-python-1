import json
from playsound import playsound
import os
from os import system
import datetime
with open("admins.json", "r") as f:
    global loadsadmin
    loadsadmin = json.load(f)
with open("contact.json", "r") as f:
    global loadsinfo
    loadsinfo = json.load(f)
playsound("bell.wav", True)
shop={
    "pen":40,
    "pencil":20,
    "glass":100,
    "copy":100,
    "book":50,
    "roll":100,
    "scissor":60,
    "clay":100,
    "laptop":50000,
    "printer":20000,
    "wire":50,
    "comb":50,
    "torch":100,
    "ghee":50,
    "camphor":10,
    "oil":100,
    "ink":50,
    "chord":100,
    "remote":200,
    "glass":50,
    "bottle":50,
    "bag":20,
    "sanitizer":50,
    "knife":50,
    "chips":10,
    "min_chips":5,
    "comics":10,
    "books":50,
    }
name={}
global inp
print()
while True:
    print("Hello welcome to python shopping what would you like to have (2 to take admin controls) (3 to clear the screen) (4 to view the list) (5 to view your list)")
    inp = input(": ")
    print()
    if inp == "2":
            playsound("bell.wav")
            admininput = input("Your id : ")
            if admininput in loadsadmin:
                admininput2 = input("Your pass : ")
                if admininput2 == loadsadmin[admininput]:
                    playsound('bell.wav')
                    while True:
                        perms = print("Whom contact do you wana look at (1 to close)")
                        adminsinput3 = input(": ")
                        if adminsinput3 == "1":
                            break
                        elif adminsinput3 in loadsinfo.keys():
                            got = loadsinfo[adminsinput3]
                            print("Found :", adminsinput3," :", got)
                            playsound('bell.wav')
                        else:
                            print("Not found")
                            playsound('error.wav')
                            pass
                else:
                    playsound('error.wav')
                    print()
                    print("wrong password")
                    print()
                    continue
            else:
                playsound('error.wav')
                print()
                print(f"No id named \"{admininput}\" was found")
                print()
                continue
    elif inp == "5":
        if len(name) == 0:
            print("Your cart is empty")
        else:
            for x in name:
              print(f"{x},")
        print()
        pass
    elif inp == "4":
        for x, y in shop.items():
          print(x,"=", f"₹{y}")
        print()
        continue
    elif inp == "3":
        system('cls')
        playsound('bell.wav')
        continue
    elif inp in shop.keys():
        print("This item was added to your list sir", "(",inp,":",shop[inp],")")
        name[inp] = int(shop[inp])
        print()
        playsound('bell.wav')
    else:
        print("Item not found or wrong input")
        playsound('error.wav')
        print()
        continue
    inp2=input("Would you like to buy more or i sholud print a bill (y/n) (2 to clear the cart): ")
    if inp2 == "y" or inp2 == "Y":
        if len(name) == 0:
            print()
            print("You cannot take a empty bill")
            print()
            continue
        inp3=input("Your name please : ")
        inp4=input("Your Contact Number Please : ")
        with open("contact.json", "r") as f:
            g = json.load(f)
        g[inp3] = {}
        g[inp3] = inp4
        with open("contact.json", "w") as f:
            json.dump(g, f)
        print(name)
        result = sum(name.values())
        print("Total : ", result)
        x = datetime.datetime.now()
        print(x.strftime("Date = %Y | %B | %d"))
        playsound('bell.wav')
        name.clear()
    elif inp2 == "n" or inp2 == "N":
        print()
        print("Canceled")
        print()
        playsound('bell.wav')
    elif inp2 == "2":
        if len(name) > 0:
            print()
            inp6 = input("Are u sure [y, n] : ")
            if inp6 == "Y" or inp6 == "y":
                print()
                print("Cleared")
                name.clear()
                playsound("bell.wav")
                print()
            else:
                print()
                playsound("error.wav")
        else:
            print()
            print("Nothing in your cart")
            print()
    else:
        print()
        print("Wrong input take care next time")
        playsound('error.wav')
        print()
