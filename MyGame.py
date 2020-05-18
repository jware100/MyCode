import time
import random


answer_A = ["A", "a", "1"]
answer_B = ["B", "b", "2"]
answer_C = ["C", "c", "3"]
answer_D = ["D", "d", "4"]
answer_E = ["E", "e", "5"]
answer_F = ["F", "f", "6"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]




#----------------------------------------Banking-------------------------------------------------------------------#
balance = 0


def withdraw():  # asks for withdrawal amount, withdraws amount from balance, returns the balance amount
    global balance
    counter = 0
    while counter <= 2:
        while counter == 0:
            withdraw = int(input("Enter the amount you want to withdraw: USD "))
            counter = counter + 1
        while ((int(balance) - int(withdraw)) < 0):
            print("Error Amount not available in card.")
            withdraw = int(input("Please enter the amount you want to withdraw again: USD "))
            continue
        while ((float(balance) - float(withdraw)) >= 0):
            balance -= withdraw
            print("Total Amount in bank: USD " + str(balance))
            return (balance)
        counter = counter + 1


def deposit():
    global balance
    counter = 0
    while counter <= 2:
        while counter == 0:
            deposit = int(input("Deposite Amount: $"))
            counter = counter + 1
        while ((int(balance) + int(deposit)) >= 0):
            balance += deposit
            print(" Total Amount in bank : USD " + str(balance))
            return balance
        counter = counter + 1
#----------------------------------------Banking-------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------#

def start():
    print('Welcome to me Python 3.8.2 Game')
    time.sleep(2)
    print('ENJOY')
    time.sleep(4)
    menu()


def bmenu():
    print(' ')
    print('------------------BAccount---------------------')
    print(' ')
    print('Your current balance is: $' + str(balance))
    print(' ')
    print('-----------------------------------------------')

#-----------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------#

def menu():
    print('------------------Menu---------------------')
    print('1. Objectives')
    print('2. Bank Account')
    print('3. Scenerio #1')
    print('-------------------------------------------')
    choice = input('-->')



    if choice in answer_A:
        print('Lets get an understanding of this game')
        time.sleep(2)
        print(' ')
        print('DONT GO BROKE')
        time.sleep(2)
        print(' ')
        menu()

    elif choice in answer_B:
        print('Lets check you bank information')
        time.sleep(2)
        print(' ')
        print('------------------BAccount---------------------')
        print(' ')
        print('Your current balance is: $' + str(balance))
        print(' ')
        print('-----------------------------------------------')

        print('Now that you know your balance lets head back')
        time.sleep(2)
        print(' ')
        menu()

    elif choice in answer_C:
        print('Lets get this game started')
        time.sleep(2)
        print(' ')
        print('With all the money you have it is time to make some choices')
        time.sleep(2)
        print(' ')
        game1()


#-----------------------------------------------------------------------------------------------------------------------#





#----------------------------------------------Scenerio #1-------------------------------------------------------------------------#


def game1():
    print("""Lets face the Facts.... Your Broke.
    You need food, clothes, car, and a place to live. A job at this moment is a must.
    Head over to your local internet Cafe and see what jobs are available""")
    time.sleep(2)
    print(' ')
    print('-----------------Jobs Hiring---------------------')
    print('1. McDonalds -  9.25/hr')
    print('2. Car Wash - 7.25/hr')
    print('3. Mail Postsman - 11/hr')
    print('4. Grocery Clerk - 9/hr')
    print('5. Cashier - 12/hr')
    print('6. Back')
    print('-------------------------------------------------')
    choice = input('Job #: ')
    if choice in answer_A:
        print('Welcome to McDonalds')
        print(' ')
        time.sleep(2)
        print('Your schedule will be M-F 9am to 5pm with a hourly wage of $9.25')
        print(' ')
        time.sleep(2)
        print('If you accept this job now we will offer a $250 sign on bonus')
        choice2 = input('Do you accept?: ')
        print(' ')
        time.sleep(2)
        if choice2 in yes:
            print('You have recieved $250')
            deposit()
            print(' ')
            time.sleep(1)
            print('Awesome. Payments will be weekly. Every Monday. See you tomorrow!')
            print(' ')
            time.sleep(2)
            bank = input('Check your Bank Balance?: ')
            if bank in yes:
                bmenu()
                time.sleep(2)
                game1p2()
            else:
                print('Lets continue')
                game1p2()
        else:
            print('Hate to see you go!')
            game1()

    elif choice in answer_B:
        print('Welcome to Express Car Wash!')
        print(' ')
        time.sleep(2)
        print('Your schedule will be M-F 9am to 5pm with a hourly wage of $7.25')
        print(' ')
        time.sleep(2)
        print('If you accept this job now we will offer a $400 sign on bonus')
        choice2 = input('Do you accept?: ')
        print(' ')
        time.sleep(2)
        if choice2 in yes:
            print('You have recieved $400')
            deposit()
            print(' ')
            time.sleep(1)
            print('Awesome. Payments will be weekly. Every Monday. See you tomorrow!')
            print(' ')
            time.sleep(2)
            bank = input('Check your Bank Balance?: ')
            if bank in yes:
                bmenu()
                time.sleep(2)
                game1p2()
            else:
                print('Lets continue')
                game1p2()
        else:
            print('Hate to see you go!')
            game1()

    elif choice in answer_C:
        print('Welcome to the City Post Office!')
        print(' ')
        time.sleep(2)
        print('Your schedule will be M-F 9am to 5pm with a hourly wage of $11')
        print(' ')
        time.sleep(2)
        print('If you accept this job now we will offer a $100 sign on bonus')
        choice2 = input('Do you accept?: ')
        print(' ')
        time.sleep(2)
        if choice2 in yes:
            print('You have recieved $100')
            deposit()
            print(' ')
            time.sleep(1)
            print('Awesome. Payments will be weekly. Every Monday. See you tomorrow!')
            print(' ')
            time.sleep(2)
            bank = input('Check your Bank Balance?: ')
            if bank in yes:
                bmenu()
                time.sleep(2)
                game1p2()
            else:
                print('Lets continue')
                game1p2()
        else:
            print('Hate to see you go!')
            game1()

    elif choice in answer_D:
        print('Welcome to Krogers!')
        print(' ')
        time.sleep(2)
        print('Your schedule will be M-F 9am to 5pm with a hourly wage of $9')
        print(' ')
        time.sleep(2)
        print('If you accept this job now we will offer a $75 sign on bonus')
        choice2 = input('Do you accept?: ')
        print(' ')
        time.sleep(2)
        if choice2 in yes:
            print('You have recieved $75')
            deposit()
            print(' ')
            time.sleep(1)
            print('Awesome. Payments will be weekly. Every Monday. See you tomorrow!')
            print(' ')
            time.sleep(2)
            bank = input('Check your Bank Balance?: ')
            if bank in yes:
                bmenu()
                time.sleep(2)
                game1p2()
            else:
                print('Lets continue')
                game1p2()
        else:
            print('Hate to see you go!')
            game1()

    elif choice in answer_E:
        print('Welcome to Walmart!')
        print(' ')
        time.sleep(2)
        print('Your schedule will be M-F 9am to 5pm with a hourly wage of $9')
        print(' ')
        time.sleep(2)
        print('If you accept this job now we will offer a $600 sign on bonus')
        choice2 = input('Do you accept?: ')
        print(' ')
        time.sleep(2)
        if choice2 in yes:
            print('You have recieved $600')
            deposit()
            print(' ')
            time.sleep(1)
            print('Awesome. Payments will be weekly. Every Monday. See you tomorrow!')
            print(' ')
            time.sleep(2)
            bank = input('Check your Bank Balance?: ')
            if bank in yes:
                bmenu()
                time.sleep(2)
                game1p2()
            else:
                print('Lets continue')
                time.sleep(2)
                game1p2()
        else:
            print('Hate to see you go!')
            game1()

    elif choice in answer_F:
        menu()

#-------------------------------------------End of Game1p1--------------------------------------------------------#


def game1p2():
    time.sleep(2)
    print(' ')
    print("""Now that the job issue is out of the way, we need transportation.
    We clearly dont have enough money to get the fanciest car, but somthing will do.
    Lets head over to the Kia Dealership to see what they have. """)
    time.sleep(2)
    print(' ')
    print('Welcome to KIA check out our used low mileage vehicle section!')
    time.sleep(2)
    print(' ')
    print('-----------------Cars---------------------------')
    print('1. optima - $50/mon')
    print('2. Sportage - $75/mon')
    print('3. Rio - $80/mon')
    print('4. Forte - $95/mon')
    print('-------------------------------------------------')
    choice = input('Car #: ')
    if choice in answer_A:
        print('You chose the optima for $50/mon...a DP of $50 is due today')
        time.sleep(2)
        buy = input('Do you want to purchase this car?: ')
        if buy in yes:
            print(' ')
            withdraw()
            print(' ')
            print('Thank you for you purchase! enjoy your new car.  ')
            print(' ')
            bstate = input('Check your Balance?: ')
            if bstate in yes:
                bmenu()
                time.sleep(2)
                print(' ')
                game1p3()
            elif bstate in no:
                time.sleep(2)
                game1p3()
        else:
            print('Lets take another look')
            time.sleep(2)
            game1p2()

    if choice in answer_B:
        print('You chose the optima for $75/mon...a DP of $75 is due today')
        time.sleep(2)
        buy = input('Do you want to purchase this car?: ')
        if buy in yes:
            print(' ')
            withdraw()
            print(' ')
            print('Thank you for you purchase! enjoy your new car.  ')
            print(' ')
            bstate = input('Check your Balance?: ')
            if bstate in yes:
                bmenu()
                time.sleep(2)
                print(' ')
                game1p3()
            elif bstate in no:
                time.sleep(2)
                game1p3()
        else:
            print('Lets take another look')
            time.sleep(2)
            game1p2()

    if choice in answer_C:
        print('You chose the optima for $80/mon...a DP of $80 is due today')
        time.sleep(2)
        buy = input('Do you want to purchase this car?: ')
        if buy in yes:
            print(' ')
            withdraw()
            print(' ')
            print('Thank you for you purchase! enjoy your new car.  ')
            print(' ')
            bstate = input('Check your Balance?: ')
            if bstate in yes:
                bmenu()
                time.sleep(2)
                print(' ')
                game1p3()
            elif bstate in no:
                time.sleep(2)
                game1p3()
        else:
            print('Lets take another look')
            time.sleep(2)
            game1p2()

    if choice in answer_D:
        print('You chose the optima for $95/mon...a DP of $95 is due today')
        time.sleep(2)
        buy = input('Do you want to purchase this car?: ')
        if buy in yes:
            print(' ')
            withdraw()
            print(' ')
            print('Thank you for you purchase! enjoy your new car.  ')
            print(' ')
            bstate = input('Check your Balance?: ')
            if bstate in yes:
                bmenu()
                time.sleep(2)
                print(' ')
                game1p3()
            elif bstate in no:
                time.sleep(2)
                game1p3()


        else:
            print('Lets take another look')
            time.sleep(2)
            game1p2()
#-------------------------------------------End of Game1p2--------------------------------------------------------#




def game1p3():
    print("""Job- checked
            car - checked
    Looks like we need to find a place to live. Lets hit the phone booth and Call around""")
    time.sleep(2)
    print(' ')
    print('After a few calls here is what the options are: ')
    print(' ')
    print('-----------------Living Options---------------------------')
    print('1. St. Andrews Apts - $200/mon')
    print('2. Pinewood Apts - $180/mon')
    print('3. Kings Apts - $150/mon')
    print('4. Grandmothers - $90/mon')
    print('-------------------------------------------------')
    choice = input('Living Option #: ')
    if choice in answer_A:
        print('St Andrews, nice choice. only half of the rent is due today.')
        buy = input('Is this what you want?: ')
        if buy in yes:
            print(' ')
            withdraw()
            print(' ')
            print('Let me know when your ready to move in!')
            print(' ')
            bstate = input('Check your Balance?: ')
            if bstate in yes:
                bmenu()
                time.sleep(2)
                print(' ')
                Workweek()

        else:
            print('Lets take another look')
            time.sleep(2)
            game1p3()

    elif choice in answer_B:
        print('Pinewood, nice choice. only half of the rent is due today.')
        buy = input('Is this what you want?: ')
        if buy in yes:
            print(' ')
            withdraw()
            print(' ')
            print('Let me know when your ready to move in!')
            print(' ')
            bstate = input('Check your Balance?: ')
            if bstate in yes:
                bmenu()
                time.sleep(2)
                print(' ')
                Workweek()



        else:
            print('Lets take another look')
            time.sleep(2)
            game1p3()

    elif choice in answer_C:
        print('Kings, nice choice. only half of the rent is due today.')
        buy = input('Is this what you want?: ')
        if buy in yes:
            print(' ')
            withdraw()
            print(' ')
            print('Let me know when your ready to move in!')
            print(' ')
            bstate = input('Check your Balance?: ')
            if bstate in yes:
                bmenu()
                time.sleep(2)
                print(' ')
                Workweek()

        else:
            print('Lets take another look')
            time.sleep(2)
            game1p3()

    elif choice in answer_D:
        print('Grandmothers, Nothing wrong with going home. Still only half of the rent is due today.')
        buy = input('Is this what you want?: ')
        if buy in yes:
            print(' ')
            withdraw()
            print(' ')
            print('Let me know when your ready to move in!')
            print(' ')
            bstate = input('Check your Balance?: ')
            if bstate in yes:
                bmenu()
                time.sleep(2)
                print(' ')
                Workweek()

        else:
            print('Lets take another look')
            time.sleep(2)
            game1p3()


#----------------------------------------------Game1p3 END-------------------------------------------------------------------------#

def Workweek():
    print("""Its been a long week of errands after errands but looks like you have to go to work today.
    bright side. you will get your check after!""")

    print('Monday - 8hrs')
    print(' ')
    time.sleep(2)
    print('Tuesday - 8hrs')
    print(' ')
    time.sleep(2)
    print('Wednesday - 8hrs')
    print(' ')
    time.sleep(2)
    print('Thursday - 8hrs')
    print(' ')
    time.sleep(2)
    print('Friday - 8hrs')
    print(' ')
    time.sleep(2)


    print('One long week of work 40 hrs!.... Its PAYDAY')
    print(' ')
    time.sleep(2)
    print(' ')
    pay()
    time.sleep(2)
    print(' ')
    rent()
    time.sleep(2)
    print(' ')
    pay()
    time.sleep(2)
    print(' ')
    rent()
    time.sleep(2)
    print(' ')















#-------------------------------------------------PayDay----------------------------------------------------------------------#
def pay():
    print('ITS PAYDAY')
    print('Please select the job you chose earlier')
    print(' ')
    time.sleep(2)
    print(' ')
    print('--------------------------------------')
    print('1. McDonalds -  9.25/hr')
    print('2. Car Wash - 7.25/hr')
    print('3. Mail Postsman - 11/hr')
    print('4. Grocery Clerk - 9/hr')
    print('5. Cashier - 12/hr')
    print('--------------------------------------')
    pay = input('Job #: ')
    if pay in answer_A:
        earn = 9.25*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        print('Paychecks are always nice!')
        time.sleep(2)
        print(' ')

    elif pay in answer_B:
        earn = 7.25*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        print('Paychecks are always nice!')
        time.sleep(2)
        print(' ')

    elif pay in answer_C:
        earn = 11.0*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        print('Paychecks are always nice!')
        time.sleep(2)
        print(' ')

    elif pay in answer_D:
        earn = 9.0*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        print('Paychecks are always nice!')
        time.sleep(2)
        print(' ')

    elif pay in answer_E:
        earn = 12.0*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        print('Paychecks are always nice!')
        time.sleep(2)
        print(' ')



#-------------------------------------------------PayDay END----------------------------------------------------------------------#
def carnote():
    print(' ')
    print('Its time to pay that car note!')
    print(' ')
    time.sleep(2)
    print('Please select the Car option you chose earlier')
    print('-----------------Cars---------------------------')
    print('1. optima - $50/mon')
    print('2. Sportage - $75/mon')
    print('3. Rio - $80/mon')
    print('4. Forte - $95/mon')
    print('-------------------------------------------------')
    choice = input('Car #: ')
    if choice in answer_A:
        earn = 50
        print('OK!')
        time.sleep(2)
        print(' ')
        print('You about to pay '+ str(earn) + ' this month for your car note.')
        time.sleep(2)
        print(' ')
        choice2 = input('Do you have enough to pay the car note?: ')
        if choice2 in yes:
            withdraw()
            print(' ')
            print('Note is payed!')
            time.sleep(2)
            print(' ')
            print('Review Bank account below:')
            print(' ')
            time.sleep(2)
            bmenu()
            print(' ')
            game1p4()
        elif choice2 in no:
            print('Back to work we go !')
            Workweek()
            print(' ')
            carnote()
    if choice in answer_B:
        earn = 75
        print('OK!')
        time.sleep(2)
        print(' ')
        print('You about to pay '+ str(earn) + ' this month for your car note.')
        time.sleep(2)
        print(' ')
        choice2 = input('Do you have enough to pay the car note?: ')
        if choice2 in yes:
            withdraw()
            print(' ')
            print('Note is payed!')
            time.sleep(2)
            print(' ')
            print('Review Bank account below:')
            print(' ')
            time.sleep(2)
            bmenu()
            print(' ')
            game1p4()
        elif choice2 in no:
            print('Back to work we go !')
            Workweek()
            print(' ')
            carnote()
    if choice in answer_C:
        earn = 80
        print('OK!')
        time.sleep(2)
        print(' ')
        print('You about to pay '+ str(earn) + ' this month for your car note.')
        time.sleep(2)
        print(' ')
        choice2 = input('Do you have enough to pay the car note?: ')
        if choice2 in yes:
            withdraw()
            print(' ')
            print('Note is payed!')
            time.sleep(2)
            print(' ')
            print('Review Bank account below:')
            print(' ')
            time.sleep(2)
            bmenu()
            print(' ')
            game1p4()
        elif choice2 in no:
            print('Back to work we go !')
            Workweek()
            print(' ')
            carnote()
    if choice in answer_D:
        earn = 95
        print('OK!')
        time.sleep(2)
        print(' ')
        print('You about to pay '+ str(earn) + ' this month for your car note.')
        time.sleep(2)
        print(' ')
        choice2 = input('Do you have enough to pay the car note?: ')
        if choice2 in yes:
            withdraw()
            print(' ')
            print('Note is payed!')
            time.sleep(2)
            print(' ')
            print('Review Bank account below:')
            print(' ')
            time.sleep(2)
            bmenu()
            print(' ')
            game1p4()
        elif choice2 in no:
            print('Back to work we go !')
            Workweek()
            print(' ')
            carnote()




#-------------------------------------------------Rent Start----------------------------------------------------------------------#


def rent():
    print("""Well after a glorious payday, it time to pay rent""")
    print(' ')
    time.sleep(2)
    print('Please select the Living option you chose earlier')
    print(' ')
    time.sleep(2)
    print('-----------------Living Options---------------------------')
    print('1. St. Andrews Apts - $200/mon')
    print('2. Pinewood Apts - $180/mon')
    print('3. Kings Apts - $150/mon')
    print('4. Grandmothers - $90/mon')
    print('-------------------------------------------------')
    choice = input('Living Option #: ')
    if choice in answer_A:
        earn = 200
        print('OK!')
        time.sleep(2)
        print(' ')
        print('You about to pay '+ str(earn) + ' this month for rent.')
        time.sleep(2)
        print(' ')
        choice2 = input('Do you have enough to pay rent?: ')
        if choice2 in yes:
            withdraw()
            print(' ')
            print('Rent is payed!')
            time.sleep(2)
            print(' ')
            print('Review Bank account below:')
            print(' ')
            time.sleep(2)
            bmenu()
            print(' ')
            carnote()
        elif choice2 in no:
            print('Back to work we go !')
            Workweek()
            print(' ')
            rent()


    elif choice in answer_B:
        earn = 180
        print('OK!')
        time.sleep(2)
        print(' ')
        print('You about to pay '+ str(earn) + ' this month for rent.')
        time.sleep(2)
        print(' ')
        choice2 = input('Do you have enough to pay rent?: ')
        if choice2 in yes:
            withdraw()
            print(' ')
            print('Rent is payed!')
            time.sleep(2)
            print(' ')
            print('Review Bank account below:')
            print(' ')
            time.sleep(2)
            bmenu()
            print(' ')
            carnote()
        elif choice2 in no:
            print('Back to work we go !')
            Workweek()
            print(' ')
            rent()




    elif choice in answer_C:
        earn = 150
        print('OK!')
        time.sleep(2)
        print(' ')
        print('You about to pay '+ str(earn) + ' this month for rent.')
        time.sleep(2)
        print(' ')
        choice2 = input('Do you have enough to pay rent?: ')
        if choice2 in yes:
            withdraw()
            print(' ')
            print('Rent is payed!')
            time.sleep(2)
            print(' ')
            print('Review Bank account below:')
            print(' ')
            time.sleep(2)
            bmenu()
            print(' ')
            carnote()
        elif choice2 in no:
            print('Back to work we go !')
            Workweek()
            print(' ')
            rent()



    elif choice in answer_D:
        earn = 90
        print('OK!')
        time.sleep(2)
        print(' ')
        print('You about to pay '+ str(earn) + ' this month for rent.')
        time.sleep(2)
        print(' ')
        choice2 = input('Do you have enough to pay rent?: ')
        if choice2 in yes:
            withdraw()
            print(' ')
            print('Rent is payed!')
            time.sleep(2)
            print(' ')
            print('Review Bank account below:')
            print(' ')
            time.sleep(2)
            bmenu()
            print(' ')
            carnote()
        elif choice2 in no:
            print('Back to work we go !')
            Workweek()
            print(' ')
            rent()

    else:
        print('Lets take another look')
        time.sleep(2)
        rent()








#-------------------------------------------------Rent END----------------------------------------------------------------------#
def work():
    print('Please select the job you chose earlier')
    print(' ')
    time.sleep(2)
    print(' ')
    print('--------------------------------------')
    print('1. McDonalds -  9.25/hr')
    print('2. Car Wash - 7.25/hr')
    print('3. Mail Postsman - 11/hr')
    print('4. Grocery Clerk - 9/hr')
    print('5. Cashier - 12/hr')
    print('--------------------------------------')
    pay = input('Job #: ')
    if pay in answer_A:
        earn = 9.25*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        time.sleep(2)
        game1p4()
    if pay in answer_B:
        earn = 7.25*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        time.sleep(2)
        game1p4()
    if pay in answer_C:
        earn = 11.0*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        time.sleep(2)
        game1p4()
    if pay in answer_D:
        earn = 9*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        time.sleep(2)
        game1p4()
    if pay in answer_E:
        earn = 12.0*40
        print('You earned '+ str(earn) + ' this week from work.')
        time.sleep(2)
        print(' ')
        deposit()
        print(' ')
        time.sleep(2)
        print('Review Bank account below:')
        print(' ')
        time.sleep(2)
        bmenu()
        print(' ')
        time.sleep(2)
        game1p4()






#-------------------------------------------------Game1p4 Start----------------------------------------------------------------------#

def game1p4():

    time.sleep(2)
    print(' ')
    print("""You and your friends all go to the casino.
    all your bills are payed and you want to gamble. You are sure if you have enough
    so you can either go back to work and postpone the trip or are you ready to go?""")
    time.sleep(2)
    print(' ')
    bmenu()
    time.sleep(2)
    print(' ')
    pick = input('Do you have enough?: ')
    if pick in yes:
        print('time to Gamble!')
        time.sleep(2)
        print(' ')
        casino()

    elif pick in no:
        print('OK lets get more money')
        work()
        time.sleep(2)
        print(' ')
        bmenu()
        time.sleep(2)
        print(' ')
        more = input('Is this enough?: ')
        if more in yes:
            casino()
        else:
            work()
            time.sleep(2)
            print(' ')
            game1p4()
#--------------------------------------------Game1p4 END-------------------------------------------------------#

def casino():

    print("Welcome to the Grand America Casino")
    time.sleep(2)
    print(' ')
    print('-----------------Games---------------------------')
    print('1. slots - $5')
    print('2. Dice - $10')
    print('3. Black-jack - $7')
    print('4. Texas Holdem - $3')
    print('-------------------------------------------------')
    game = input('Which game #: ')
    if game in answer_A:
        count = random.randint(-5,5)
        print('Slots')
        time.sleep(2)
        print(' ')
        withdraw()
        time.sleep(2)
        print(' ')
        print('Lets go!')
        print(' ')
        print('You pulled the lever and won/loss $'+ str(count))
        time.sleep(2)
        print(' ')
        print('Lets deposit what you just made')
        time.sleep(2)
        print(' ')
        deposit()
        time.sleep(2)
        print(' ')

        again = input('Do you want to play again?: ')
        if again in yes:
            bmenu()
            time.sleep(2)
            print(' ')
            casino()
        else:
            print('I hope you experience here at the Grand America Hotel was Great! see you later!')
            time.sleep(2)
            print(' ')
            pagain = input('Do you want to play the game again?: ')
            if pagain in answer_A:
                start()
            else:
                exit()




    elif game in answer_B:
        count = random.randint(-5,15)
        print('Dice Game')
        time.sleep(2)
        print(' ')
        withdraw()
        time.sleep(2)
        print(' ')
        print('Lets go!')
        print(' ')
        print('You throw the dice and won/loss $'+ str(count))
        time.sleep(2)
        print(' ')
        print('Lets deposit what you just made')
        time.sleep(2)
        print(' ')
        deposit()
        time.sleep(2)
        print(' ')

        again = input('Do you want to play again?: ')
        if again in yes:
            bmenu()
            time.sleep(2)
            print(' ')
            casino()
        else:
            print('I hope you experience here at the Grand America Hotel was Great! see you later!')
            time.sleep(2)
            print(' ')
            pagain = input('Do you want to play the game again?: ')
            if pagain in answer_A:
                start()
            else:
                exit()



    elif game in answer_C:
        count = random.randint(-10,25)
        print('Black-jack')
        time.sleep(2)
        print(' ')
        withdraw()
        time.sleep(2)
        print(' ')
        print('Lets go!')
        print(' ')
        print('You show your hand and won/loss $'+ str(count))
        time.sleep(2)
        print(' ')
        print('Lets deposit what you just made')
        time.sleep(2)
        print(' ')
        deposit()
        time.sleep(2)
        print(' ')

        again = input('Do you want to play again?: ')
        if again in yes:
            bmenu()
            time.sleep(2)
            print(' ')
            casino()
        else:
            print('I hope you experience here at the Grand America Hotel was Great! see you later!')
            time.sleep(2)
            print(' ')
            pagain = input('Do you want to play the game again?: ')
            if pagain in answer_A:
                start()
            else:
                exit()



    elif game in answer_D:
        count = random.randint(-25,50)
        print('Texas Holdem')
        time.sleep(2)
        print(' ')
        withdraw()
        time.sleep(2)
        print(' ')
        print('Lets go!')
        print(' ')
        print('You show your hand and won/loss $'+ str(count))
        time.sleep(2)
        print(' ')
        print('Lets deposit what you just made')
        time.sleep(2)
        print(' ')
        deposit()
        time.sleep(2)
        print(' ')

        again = input('Do you want to play again?: ')
        if again in yes:
            bmenu()
            time.sleep(2)
            print(' ')
            casino()
        else:
            print('I hope you experience here at the Grand America Hotel was Great! see you later!')
            time.sleep(2)
            print(' ')
            pagain = input('Do you want to play the game again?: ')
            if pagain in answer_A:
                start()
            else:
                exit()










start()

