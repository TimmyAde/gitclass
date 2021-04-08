# import mysql.connector

# mycon = mysql.connector.connect(host='127.0.0.1', user='root', password='', database = "atm_machine")
# # print(mycon)
# mycursor = mycon.cursor()

# import random
# import time
# import sys


# balance = 50000
# currentMoney = 50000
# PIN = ("1234")
# total = (balance)


#                    # ------------------ registration ------------------

# def register():
#         Full_Name = input("Enter your full name: ")
#         Email_Address = input("Enter your email address: ")
#         Phone_Number = input("Enter your phone number: ")
#         Account_Number = "02" +str(random.randrange(10000000, 20000000))
#         print("your account number is ",Account_Number)
#         # Account_no = input("account: ")
#         Pin = input("Create your pin: ")
#         myquery = "INSERT INTO registered_name (Full_Name, Email_Address, Phone_Number, Account_Number, Pin) VALUES(%s, %s, %s, %s, %s)"
#         val = (Full_Name, Email_Address, Phone_Number, Account_Number, Pin)
#         mycursor.execute(myquery, val)
#         mycon.commit()
#         # print(mycursor.rowcount, "record inserted successfully")
#         print("Successfull.....your account as been created")
#         print("your account details is " +Full_Name+", your account number is: "+Account_Number+" and your pin number is: "+Pin)


#                   #------------------- login --------------------

# def login():
#     myquery = "SELECT * FROM registered_name WHERE Account_Number=%s"
#     account = input("Enter your account number: " )
#     mycursor.execute(myquery, (account,))
#     record = mycursor.fetchall()
#     if record:
#         myquery = "SELECT * FROM registered_name WHERE Pin=%s"
#         pin = input("Enter your pin: ")
#         mycursor.execute(myquery, (pin,))
#         record = mycursor.fetchone()
#         if record:
#             print("Dear ",record[1])
#             input("press enter to procced")
#             print("1. Top-up airtime")
#             print("2. Pay your bill")
#             print("3. Deposit")
#             print("4. Withdraw cash")
#             print("5. Transfer money")
#             print("6. check balance")
#             print("7. Change your pin")
#             print("8. Quit")
#             trans = input("Enter your option here: ")
            
#         else:
#             print("you input wrong pin")
#     else:
#         print("your account is not registered with us")
#     # def another():
#     #     print("perform another transaction?\n 1.Perform another          2.End transaction\n 3.")
    


#                         #-------------------- Top-up Airtime -----------------
#     def Top():
#         if trans == "1":
#             pNumber = input("Enter the phone number: ")
#             amt = input("Enter the amount: ")
#             time.sleep(2)
#             print("Successfull")
#             time.sleep(2)
#             print(perform())
#     Top()

#                                 #-------------------- Pay bills --------------------
#     def pay():
#         if trans == "2":
#             print("sorry")
#             print("What you are requesting for is not available yet!")
#             time.sleep(2)
#             print(perform())
#     pay()

#                                 #-------------------- Withdraw cash ------------------
#     def withdraw():
#         if trans == "4":
#             myquery = "SELECT * FROM registered_name WHERE Pin=%s"
#             pin = input("Enter your pin: ")
#             mycursor.execute(myquery, (pin,))
#             record = mycursor.fetchone()
#             if record:
#                 amount = str(input("Enter your amount: "))
#                 myquery = "SELECT * FROM registered_name WHERE Balance = %s"
#                 mycursor.execute(myquery, (amount,))
#                 amt = mycursor.fetchone()
#                 if amount > amt:
#                     print("Insufficent money!")
#                 else:
#                     print("Please wait while your transaction is processing...")
#                     time.sleep(5)
#                     print("transaction successful")
#                     time.sleep(3)
#                     print("please take your cash ")
#                     total = balance - amount
#                     print("your remaining balance is: ",total)
#                     another = input("did you want to perform another transacton? ")
#                     if another == "yes":
#                         print(withdraw())
#                     else:
#                         print("Thank you for banking with us")
#                         time.sleep(3)
#                         print(perform())
#             else:
#                 print("Wrong pin")
        
#     withdraw()


#                         #-------------------- Transfer money -----------------
#     def Transfer():
#         if trans == "5":
#             print("1. To Same Bank")
#             print("2. To Other Bank")
#             option = input("Input your option here: ")
#             if option == ("1"):
#                 Recipt = input("Enter the Account Number: ")
#                 if Recipt == Account_Number:
#                     print("1. Saving")
#                     print("2. Current")
#                     types = input("Enter here: ")
#                     if types == ("1"):
#                         money = input("Enter the amount: ")
#                         if money > str(balance):
#                             print("      Sorry")
#                             print("Insufficent money")
#                             time.sleep(2)
#                         else:
#                             pin = input("Enter your PIN to perform the process: ")
#                             if pin == Pin:
#                                 print("you are trying to transfer "+money+" to "+Full_Name, Recipt)
#                                 input("press enter key to comfirm")
#                                 time.sleep(2)
#                                 print("you have successfully transfer "+money+ " to "+ Recipt)
#                                 # total = (money - str(balance))
#                                 # print(total)
#                             else:
#                                 print("you input wrong pin")
#                     elif types == ("2"):
#                         money = input("Enter the amount: ")
#                         print("you are trying to transfer "+money+" to "+Recipt)
#                         input("press enter key to comfirm")
#                         # money -= 50000
#                         # print(balance)
#                 else:
#                     print("This account number is not registered with us")
#                     print("Please crosscheck and try again")
#             elif option == ("2"):
#                 print("choose the other bank")
#                 print("1. Access Bank                   2. Eco Bank")
#                 print("3. First Bank                    4. Intercontinental Bank")
#                 print("5. MCB Bank                      6. Sky Bank")
#                 print("7. Polarize Bank                 7. UBA Bank")
#                 print("8. Union Bank                    9. Zenith Bank")
#                 otherBank = input("please enter your option: ")
#     Transfer()


#                         #-------------------- Check balance ------------------
#     def checkbalance():
#         if trans == "6":
#             print("your balance is "+str(total))
#             recipt = input("did you want recipt for this? ")
#             if recipt == "yes":
#                 time.sleep(2)
#                 print("take your recipt...")
#                 print("Thank you...")
#                 time.sleep(2)
#                 print(perform())
#             else:
#                 print("Thank you...")
#                 time.sleep(2)
#                 print(perform())
#     checkbalance()


#                         #-------------------- changepin ------------------------

#     def Changepin():
#         if trans == "7":
#             old = input("Input your old pin: ")
#             if old == pin:
#                 new = input("Input your new pin: ")
#                 confirm = input("Confirm your pin: ")
#                 if new == confirm:
#                     print("Pin changed")
#                 else:
#                     print("Your confirm pin does not march with new pin")
#             else:
#                 print("Incorrect pin")
#     Changepin()

#     def Quit():
#         if trans == "8":
#             sys.exit()
#             print(perform())
#         else:
#             print("Invalid input")
#             print(login())
#     Quit()    


#          # ----------------- 1st process ------------------

# def perform():
#     print("Welcome To World ATM Machine")
#     print("""Which operation did you want to perform?\n 1.Register\n 2.Login\n 3.Quit""")
#     reg = input("Enter your option here: ")
#     if reg == '1':
#         register()
#     elif reg == '2':
#         login()
#     elif reg == '3':
#         print("Thank you")
#         sys.exit()
#     else:
#         print(perform())
# perform()


import mysql.connector

mycon = mysql.connector.connect(host='127.0.0.1', user='root', password='', database = "atm_machine")
# print(mycon)
mycursor = mycon.cursor()

import random
import time
import sys


balance = 50000
currentMoney = 50000
PIN = ("1234")
total = (balance)


                   # ------------------ registration ------------------

def register():
        fName = input("Enter your full name: ")
        email = input("Enter your email address: ")
        phoneNO = input("Enter your phone number: ")
        acctNO = "02" +str(random.randrange(10000000, 20000000))
        print("your account number is ",acctNO)
        pin = input("Create your pin: ")
        myquery = "INSERT INTO registered_name (Full_Name, Email_Address, Phone_Number, Account_Number, Pin) VALUES(%s, %s, %s, %s, %s)"
        val = (fName, email, phoneNO, acctNO, pin)
        mycursor.execute(myquery, val)
        mycon.commit()
        print("Successfull.....your account as been created")
        print("your account details is " +fName+", your account number is: "+acctNO+" and your pin number is: "+pin)
        time.sleep(2)
        print(perform())

                  #------------------- login --------------------

def login():
    myquery = "SELECT * FROM registered_name WHERE Account_Number=%s"
    accountNO = input("Enter your account number: " )
    mycursor.execute(myquery, (accountNO,))
    record = mycursor.fetchall()
    if record:
        myquery = "SELECT * FROM registered_name WHERE Account_Number=%s AND Pin=%s"
        pin = input("Enter your pin: ")
        mycursor.execute(myquery, (accountNO, pin,))
        record = mycursor.fetchone()
        if record:
            print("Dear ",record[1])
            input("press enter to procced")
            def make():
                print("1. Top-up airtime")
                print("2. Pay your bill")
                print("3. Deposit")
                print("4. Withdraw cash")
                print("5. Transfer money")
                print("6. check balance")
                print("7. Change your pin")
                print("8. Quit")
                trans = input("Enter your option here: ")

#---------------------- Another trans ----------------------

                def another():
                    print("perform another transaction?\n 1.Perform another          2.End transaction")
                    anoda = input("Enter your opion: ")
                    if anoda == "1":
                        print(make())
                    elif anoda == "2":
                        print("Thank you")
                        sys.exit()
                    else:
                        print("Wrong input")
                        print(another())
        

                #-------------------- Top-up Airtime -----------------

                def Top():
                    if trans == "1":
                        myquery = "SELECT Balance =%s FROM registered_name WHERE Account_Number=%s"
                        amt = input("Enter the amount: ")
                        pNumber = input("Enter the phone number: ")
                        mycursor.execute(myquery, amt, accountNO)
                        balance = mycursor.fetchone()
                        if amt > balance:
                            print("Insufficient Fund")
                        else:
                            newBalance = amt - balance
                            myquery = "UPDATE registered_name SET Balance =%s  WHERE Account_Number=%s"
                            balance = (newBalance, accountNO)
                            mycon.commit()
                            time.sleep(2)
                            print("Successfull")
                            time.sleep(2)
                            print(another())
                Top()
            #     newBalance = self.balance[0] - amount[self.userInput]
            # query = "UPDATE atm SET Account_Balance= %s WHERE Account_no=%s"
            # account = (newBalance, self.acct_no)
            # self.mycursor.execute(query, account)
            # self.mycon.commit()
            # print("Please take your cash of" +str(amount[self.userInput]))

                #-------------------- Pay bills --------------------
                def pay():
                    if trans == "2":
                        print("sorry")
                        print("What you are requesting for is not available yet!")
                        time.sleep(2)
                        print(another())
                pay()


                #----------------------- Deposit ---------------------
                def Deposit():
                    if trans == "3":
                        userInput = input("Enter your deposit amount: ")
                        myquery = "SELECT Balance FROM registered_name WHERE Account_Number=%s"
                        mycursor.execute(myquery, (accountNO,))
                        balance = mycursor.fetchone()
                        newBalance = userInput + balance
                        myquery = "UPDATE registered_name SET Balance= %s WHERE Account_Number=%s"
                        account = (newBalance, accountNO)
                        mycursor.execute(myquery, account)
                        mycon.commit()
                        print(userInput," deposited successfully")
                        print(another())
                Deposit()

                #-------------------- Withdraw cash ------------------
                def withdraw():
                    if trans == "4":
                        myquery = "SELECT Pin=%s FROM registered_name WHERE Account_Number=%s"
                        pin = input("Enter your pin: ")
                        mycursor.execute(myquery, (pin, accountNO))
                        record = mycursor.fetchone()
                        if record:
                            amount = input("Enter your amount: ")
                            myquery = "SELECT Balance FROM registered_name WHERE  Account_Number= %s"
                            mycursor.execute(myquery, (amount,))
                            balance = mycursor.fetchone()
                            if amount > balance:
                                print("Insufficent money!")
                            else:
                                newBalance = balance - amount
                                myquery = "UPDATE registered_name SET Balance= %s WHERE Account_Number=%s"
                                acct = (newBalance, accountNO)
                                mycursor.execute(myquery, acct)
                                mycon.commit()
                                print("Please wait while your transaction is processing...")
                                time.sleep(5)
                                print("transaction successful")
                                time.sleep(3)
                                print("please take your cash ")
                                # total = balance - amount
                                print("your remaining balance is: ")
                                another = input("did you want to perform another transacton? ")
                                if another == "yes":
                                    print(withdraw())
                                else:
                                    print("Thank you for banking with us")
                                    sys.exit()
                        else:
                            print("Wrong pin")
                    
                withdraw()


                    #-------------------- Transfer money -----------------
                def Transfer():
                    if trans == "5":
                        print("1. To Same Bank\n2. To Other Bank")
                        option = input("Input your option here: ")
                        if option == "1":
                            Recipt = input("Enter the Reciptent Account Number: ")
                            myquery = "SELECT * FROM registered_name WHERE Account_Number=%s"
                            mycursor.execute(myquery, (Recipt,))
                            reciptAcc = mycursor.fetchall()
                            if reciptAcc:
                                print(reciptAcc[0][1])
                                print("1. Saving")
                                print("2. Current")
                                accTypes = input("Enter here: ")
                                if accTypes == "1":
                                    money = input("Enter the amount: ")
                                    if money > str(balance):
                                        print("      Sorry")
                                        print("Insufficent money")
                                        time.sleep(2)
                                        print(another())
                                    else:
                                        pin = input("Enter your PIN to perform the process: ")                           
                                        myquery = "SELECT * FROM registered_name WHERE Pin=%s"
                                        mycursor.execute(myquery, (pin,))
                                        record = mycursor.fetchone()
                                        if record:
                                            print("you are trying to transfer #"+money+" to "+reciptAcc[0][1])
                                            cont = input("press 1 to continue\npress 2 to cancel: ")
                                            if cont == "1":
                                                time.sleep(2)
                                                print("you have successfully transfer #"+money+ " to "+ reciptAcc[0][1])
                                                time.sleep(3)
                                                print(another())
                                            elif cont == "2":
                                                print("Transaction  cancelled")
                                                time.sleep(2)
                                                print(perform())
                                        else:
                                            print("you input wrong pin")
                                            print(perform())
                                elif accTypes == "2":
                                    money = input("Enter the amount: ")
                                    print("you are trying to transfer "+money+" to "+Recipt)
                                    # input("press enter key to comfirm")
                                    # money -= 50000
                                    # print(balance)
                                    # print(another())
                                else:
                                    print("Wrong input")
                                    print(Transfer())
                            else:
                                print("This account number is not registered with us")
                                print("Please crosscheck and try again")
                                print(make())
                        elif option == "2":
                            print("choose the other bank")
                            print("1. Access Bank                   2. Eco Bank")
                            print("3. First Bank                    4. Intercontinental Bank")
                            print("5. MCB Bank                      6. Sky Bank")
                            print("7. Polarize Bank                 7. UBA Bank")
                            print("8. Union Bank                    9. Zenith Bank")
                            otherBank = input("please enter your option: ")
                        else:
                            print("Wrong input")
                            print(Transfer())
                Transfer()


                    #-------------------- Check balance ------------------
                def checkbalance():
                    if trans == "6":
                        myquery = "SELECT * registered_name WHERE Account_Number='account' AND Balance=%s"
                        mycursor.execute(myquery)
                        checkbalance = mycursor.fetchone()
                        print("your balance is ",checkbalance)
                        recipt = input("did you want recipt for this? ")
                        if recipt == "yes":
                            time.sleep(2)
                            print("take your recipt...")
                            print("Thank you...")
                            time.sleep(2)
                            print(another())
                        else:
                            print("Thank you...")
                            sys.exit()
                checkbalance()


                    #-------------------- changepin ------------------------

                def Changepin():
                    if trans == "7":
                        old = input("Input your old pin: ")
                        myquery = "UPDATE registered_name SET Pin = %s WHERE Account_Number=%s"
                        mycursor.execute(myquery, (old,))
                        reciptAcc = mycursor.fetchone()
                        if old:
                            new = input("Input your new pin: ")
                            confirm = input("Confirm your pin: ")
                            if new == confirm:
                                print("Pin changed")
                            else:
                                print("Your confirm pin does not march with new pin")
                                print(Changepin())
                        else:
                            print("Incorrect pin")
                            print(login())
                Changepin()
                    #------------------------- Quit ----------------------------
                def Quit():
                    if trans == "8":
                        print("Thank you")
                        sys.exit()
                Quit()
            make()
        else:
            print("you input wrong pin")
    else:
        print("your account is not registered with us")
    
    
             # ----------------- 1st process ------------------

def perform():
    print("Welcome To World ATM Machine")
    print("""Which operation did you want to perform?\n 1.Register\n 2.Login\n 3.Quit""")
    reg = input("Enter your option here: ")
    if reg == '1':
        register()
    elif reg == '2':
        login()
    elif reg == '3':
        print("Thank you")
        sys.exit()
    else:
        print(perform())
perform()