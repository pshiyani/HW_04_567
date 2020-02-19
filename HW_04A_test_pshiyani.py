"""
SSW_567
Author: Priyankaben Shiyani
Project Description: Test(Develop with the Perspective of the Tester in mind)
"""

import unittest
from HW_04A_pshiyani import get_data_user

class Test_github(unittest.TestCase):
    ''' for testing HW_04A_pshiyani.py '''
    def test_get_data_user(self):
        check = {
            'hellogitworld': 2,
            'helloworld': 2,
            'Mocks': 2,
            'Project1': 2,
            'threads-of-life': 2
        }
        self.assertEqual(get_data_user('richkempinski'), check)


if __name__ == '__main__':
    print('Running HW_04A_test_pshiyani.py testing suite.')
    unittest.main(exit = False, verbosity=2)





    