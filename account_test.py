import unittest # Importing the unittest module
from account import Account # Importing the account class


class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_account = Account("Jeff","Musa","123456","jeff@m.com") # create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"Jeff")
        self.assertEqual(self.new_account.last_name,"Musa")
        self.assertEqual(self.new_account.password,"123456")
        self.assertEqual(self.new_account.email,"jeff@m.com")
    

if __name__ == '__main__':
    unittest.main()