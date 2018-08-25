import unittest # Importing the unittest module
from credentials import Credentials # Importing the account class


class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("Jeff","Musa","123456","jeff@m.com") # create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credentials_name,"Jeff")
        self.assertEqual(self.new_credentials.user_name,"Musa")
        self.assertEqual(self.new_credentials.password,"123456")
        self.assertEqual(self.new_credentials.email,"jeff@m.com")
    
if __name__ == '__main__':
    unittest.main()    