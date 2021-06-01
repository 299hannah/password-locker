import unittest
from user import Credentials
import pyperclip
from user import User

class TestClass(unittest.TestCase):

    def setUp(self):
        '''
        method to run each test
        '''
        self.user = User("Hannah", "123")

    def test_init(self):
        '''
        check proper user initialization
        '''
        self.assertEqual(self.user.username, "Hannah")
        self.assertEqual(self.user.password, "123")

    def tearDown(self):
        '''
        method to clean up after each test
        '''

        User.userList = []

    def test_save_multiple_users(self):
        '''
        method to test multiple saved users
        '''
        self.user.saveUser()
        test_user = User("Ian", "456")  # new contact
        test_user.saveUser()

        self.assertEqual(len(User.userList), 2)

    def test_delete_user(self):
        """
        delete users
        """
        self.user.saveUser()
        test_user = User("Ian", "456")  # new contact
        test_user.saveUser()

        self.user.deleteUser()
        self.assertEqual(len(User.userList), 1)

    def test_display_users(self):
        """
        method to test if users are correctly displayed
        """
        self.assertEqual(User.displayUser(), User.userList)


class TestCredentials(unittest.TestCase):

    def setUp(self):
        """
        define the constructor
        """
        self.cred = Credentials("Instagram", "inst", "12345")

    def tearDown(parameter_list):
        """
        clear up during each test
        """
        pass

    def test_init(self):
        """
        make sure the constructor is well initialized
        """
        self.assertEqual(self.cred.account, "Instagram")
        self.assertEqual(self.cred.username, "inst")
        self.assertEqual(self.cred.password, "12345")

    def test_save_multiples_cred(self):
        """
        test for multiple credentials
        """
        self.cred.save_details()
        test_cred = Credentials("Instagram", "insta", 123456)  # new contact
        test_cred.save_details()

        self.assertEqual(len(Credentials.credentials_list), 3)

    def test_delete(self):
        """
        test if the credential can be deleted
        
        """
        self.cred.save_details()
        test_cred = Credentials("Instagram", "insta", 123456)  # new contact
        test_cred.save_details()

        self.cred.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def  test_find_credential(self):
        """
        search a credential 
        """
        self.cred.find_credential()
        test_cred = Credentials("Instagram", "insta", 123456)  # new contact
        test_cred.find_credential()

        found = Credentials.find_credential("Instagram")
        self.assertEqual(found.account, test_cred.account)

    def test_display(self):
        """
        method to test if credentials can be displayed
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


if __name__ == "__main__":
    unittest.main()
