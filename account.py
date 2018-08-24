class Account:
    """
    Class that generates new instances of users.
    """
    account_list = [] #empty account list

    def __init__(self,first_name,last_name,password,email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    