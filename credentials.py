class Credentials:
    """
    Class that generates new instances of users.
    """
    credentials_list = [] #empty account list

    def __init__(self,credentials_name,user_name,password,email):
        self.credentials_name = credentials_name
        self.user_name = user_name
        self.password = password
        self.email = email    

    def save_credentials(self):

        '''
        save_account method saves account objects into account_list
        '''

        Credentials.credentials_list.append(self)    


    def delete_credentials(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Credentials.credentials_list.remove(self)   


    @classmethod
    def find_by_name(cls,name):
        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                return credentials  


    @classmethod
    def credentials_exist(cls,name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                    return credentials

        return False      


    @classmethod
    def display_credentials(cls):  #check this line later
        '''
        method that returns the account list
        '''
        return cls.credentials_list            
                      