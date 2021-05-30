import unittest
from user import User


class test_user(unittest.TestCase):

    def test_createUser(self):
        self.user = User("kiptoo", "1234") 
        self.assertEqual(self.user.username, "kiptoo")

    # def test_CreateUser(self):
    #     self.result = User("kiptoo", "rotich")
    #     self.assertEqual(self.result.username , "kiptoo")

if __name__ ==  '__main__':
    unittest.main()


