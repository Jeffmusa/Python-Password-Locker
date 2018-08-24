#!/usr/bin/env python3.6
from account import Account

def create_account(account_name,user_name,password,email):
    '''
    Function to create a new account
    '''
    new_account = Account(account_name,user_name,password,email)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()    

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()    


def find_account(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Account.find_by_name(name)    

def check_existing_accounts(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Account.account_exist(name)    

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()  

def main():
    print("Hello Welcome to your Pass Word Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n ca -> Create a new account.\n da -> Display existing accounts.\n fa ->Find created accounts.\n ex ->exit Pass Word Locker. ")
        short_code = input().lower()
        if short_code == 'ca':
            print("New Account")
            print("*"*100)
            print ("Account name:")
            account_name = input()
            print("User name ...")
            u_name = input()
            print("PASS WORD ...")
            
            pwd = input()
            print("Email address ...")
            e_address = input()
            save_accounts(create_account(account_name,u_name,pwd,e_address)) # create and save new account.
            print ('\n')
            print(f"A New {account_name} Account with the user name  {u_name} has been created.")
            print ('\n')
        elif short_code == 'da':
             if display_accounts():
                 print("Here is a list of all your accounts")
                 print('\n')
                 for account in display_accounts():
                     print(f"Account name:{account.account_name}  User name: {account.user_name} Password:{account.password}")
                     print('\n')
             else:
                 print('\n')
                 print("You dont seem to have any accounts saved yet")
                 print('\n')
        elif short_code == 'fa':
                print("Enter the name of the account you want to search for")
                search_account = input()
                if check_existing_accounts(search_account):
                    search_cred = find_account(search_account)
                    print(f" {search_cred.user_name}")
                    print('-' * 20)
                    print(f"PASSWORD.......{search_cred.password}")
                    print(f"Email address.......{search_cred.email}")
                    
                else:
                    print("You don't have an account by that name")
                    
        elif short_code == "ex":
                    print(f"Thanks {user_name} for your time.I hope you enjoyed my service.Bye...")
                    break
        else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()                            