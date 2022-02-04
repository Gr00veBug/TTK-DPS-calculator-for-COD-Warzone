import time
from datetime import date
import sys

def advdpscalc():
    gunname = input("Please type in the name of the gun.\n")
    gundamhead = input("Please type in the damage value of a head shot.\n")
    gubdamheadint = int(gundamhead)
    gundamchest =  input("Please type in the damage value of a chest shot.\n")
    gundamchestint = int(gundamchest)
    gundamstom = input("Please type in the damage value of a stomach shot.\n")
    gundamstomint = int(gundamstom)
    gundamextrem = input("Please type in the damage value of a limb shot.\n")
    gundamextremint = int(gundamextrem)
    fire = input(""" Will you be using incendiary ammo?
    1. Yes
    2. No
      """)
    fireint = int(fire)
    if fireint == 1:
        print("ok adding fire damage")
        firedam = 12.4
    else:
        print("Ok no fire damage")
        firedam = 0.00
    gunrpm = input("Please type in the gun's rpm.\n")
    gunromint = int(gunrpm)
    p = 0
    v = 100
    headp = input("What percentage of shots would you like to go to the head? DONT USE % just write 25 for 25%\n")
    headpint = int(headp)
    p += headpint
    v -= headpint
    if p > 100:
        print("You have added a number that exceeded to the total of 100% I will make it 25% automatically...\n")
        p -= headpint
        v += headpint
        p += 25
        v -= 25
        time.sleep(3)
    else:
        pass
    strv = str(v)
    chestp = input("You have " + strv + "% left to distribute what percentage of shots would you like to go to the chest?\n")
    chestpint = int(chestp)
    p += chestpint
    v -= chestpint
    strv =str(v)

    if p > 100:
        print("You have added a number that exceeded to the total of 100% I will make it 25% automatically...\n")
        p -= chestpint
        v += chestpint
        p += 25
        v -= 25

        time.sleep(3)
    else:
        pass
    strv = str(v)
    stomp = input("You have " + strv + "% left to distribute What percentage of shots would you like to go to the stomach?\n")
    stompint = int(stomp)
    p += stompint
    v -= stompint
    if p > 100:
        print("You have added a number that exceeded to the total of 100% I will make it 25% automatically...\n")
        p -= stompint
        v += stompint
        p += 25
        v -= 25
        time.sleep(3)
    else:
        pass
    strv = str(v)
    extremp = v
    print("You have " + strv + "% left which will automatically go towards extremities...\n")
    time.sleep(3)
    headp2 = (headpint / 100)
    stomp2 = (stompint / 100)
    chestp2 = (chestpint / 100)
    extemp2 = (extremp / 100)
    rpmround = round(gunromint,2)
    sps = rpmround // 60
    headdam = (sps * headp2) * gubdamheadint
    chestdam = (sps * chestp2) * gundamchestint
    stomdam = (sps * stomp2) * gundamstomint
    extremdam = (sps * extemp2) * gundamextremint
    dps = (headdam + chestdam + stomdam + extremdam + firedam)
    dpsround = round(dps,3)
    strdps = str(dpsround)
    daymade = date.today()

    gunstats = (gunname + " DPS: " + strdps + " Date Created " + str(daymade.day) + "/" + str(daymade.month) + "/" + str(daymade.year))
    with open('advweaponlist.txt', 'a') as f:
        f.write(gunstats)
        f.write("\n")
    print(gunstats + "\n")
    time.sleep(2)
    print("Info sent to your gunlist! migrating back to the main menu\n")
    time.sleep(3)
    menu()






def ttkcalc():
    gunname = input("Please Type in the name of the gun.\n")
    gundam = input("Please type in the damage of the gun\n")
    gunrpm = input("Please type in the rounds per minute for the gun.\n")
    gundamint = float(gundam)
    gunrpmint = float(gunrpm)
    ttk1 = (250 / gundamint) / (gunrpmint / 60)
    ttkround = round(ttk1,3)
    ttkstr = str(ttkround)
    daymade = date.today()
    gundetails = str(gunname) + " TTK: " + str(ttkstr) + " seconds Date Created: " + str(daymade.day) + "/" + str(daymade.month) + "/" + str(daymade.year)
    gunlist = (gundetails)
    with open('weaponlist.txt', 'a') as f:
        f.write(gunlist)
        f.write("\n")
    print(gundetails)
    time.sleep(5)
    menu()
def weaponlist():
    list = open('weaponlist.txt')
    listcontents = list.read()
    print(listcontents)
    time.sleep(3)
    menu()
def  advweaponlist():
    list = open('advweaponlist.txt')
    listcontents = list.read()
    print(listcontents)
    time.sleep(3)
    menu()


def menu():
    print("""
      _______ _______ _  __   _____      _        _              _____       ___   ___            ____              
     |__   __|__   __| |/ /  / ____|    | |      | |            / ____|     / _ \ / _ \          |  _ \             
        | |     | |  | ' /  | |     __ _| | ___  | |__  _   _  | |  __ _ __| | | | | | |_   _____| |_) |_   _  __ _ 
        | |     | |  |  <   | |    / _` | |/ __| | '_ \| | | | | | |_ | '__| | | | | | \ \ / / _ \  _ <| | | |/ _` |
        | |     | |  | . \  | |___| (_| | | (__  | |_) | |_| | | |__| | |  | |_| | |_| |\ V /  __/ |_) | |_| | (_| |
        |_|     |_|  |_|\_\  \_____\__,_|_|\___| |_.__/ \__, |  \_____|_|   \___/ \___/  \_/ \___|____/ \__,_|\__, |
                                                         __/ |                                                 __/ |
                                                        |___/                                                 |___/ 

    """)
    time.sleep(1)
    menuchoice = input("""    Please choose an option
    
    1. TTK Calculator
    2. List TTK weapons
    3. Advanced DPS Calculator
    4. List DPS Weapns
    5. Close\n""")
    menuchoiceint = int(menuchoice)
    if menuchoiceint == 1:
        ttkcalc()
    elif menuchoiceint == 2:
        weaponlist()
    elif menuchoiceint == 5:
        print("Thank you for using TTK calculator!")
        time.sleep(2)
        sys.exit(0)
    elif menuchoiceint == 3:
        advdpscalc()
    elif menuchoiceint == 4:
        advweaponlist()

    else:
        print("Wrong option, restarting now")
        time.sleep(3)
        menu()

menu()