#made by - steven f - michael Z - Anam Asif
#Date 19/5/2021


#step 1 create a list of pins

bank_stored_pin = [1122, 2211, 1212]
balance = 1000
#step 2 create some user input for the pin
user_input = int(input("enter pin"))
balance_input = int(input("withdrawral amount"))

#step 3 test
# print(bank_stored_pin)
# print(user_input)

#step 4 cross referance user's pin
# for pin in bank_stored_pin:
#     if user_input == pin:
#         print("correct pin")
#         break
#     elif user_input != pin:
#         continue
#this does not work ^

# pin_check_num = bank_stored_pin.count(user_input)
# print(pin_check_num)

# if pin_check_num == 1:
#     print("correct pin")
# else:
#     print("incorrect pin")



    #step 5 put this into a function
# bank_stored_pin = [1122, 2211, 1212, 2121, 1321]

def pin_checker():
    pin_check_num = bank_stored_pin.count(user_input)
    if pin_check_num == 1:
        print("correct pin")
    else:
        print("incorrect pin")


# pin_checker()

#step 6 input a balance
def funds_checker():
    if balance >= balance_input:
        print("you have sufficent funds do you with to proceed")
    else:
        print("insufficent funds")

funds_checker()
#step 7  make it so the balance updates after withdrawal
balance - balance_input