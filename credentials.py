class Credentials:
    """
    Class that generates new instances of users.
    """
    credentials_list = [] #empty credentials list

    def __init__(self,credentials_name,usr_name,password,email):
        self.credentials_name = credentials_name
        self.usr_name = usr_name
        self.password = password
        self.email = email    

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)    


    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
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
        Method that checks if a credentials exists from the credentials list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.password == name:
                    return credentials

        return False      


    @classmethod
    def display_credentials(cls):  #check this line later
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list            
                      