"""
SSW_567
Author: Priyankaben Shiyani
Project Description: Test(Develop with the Perspective of the Tester in mind)
"""

import unittest
from unittest import mock
from HW_04A_pshiyani import get_user_data

class Test_github(unittest.TestCase):
    ''' for testing HW_04A_pshiyani.py '''
    @mock.patch('urllib.request.urlopen')
    def test_get_data_user(self, mock_return):
        mock_return.side_effect = [
            '[{"name" : "567"}, {"name" : " 567_HW_04A"}]',
            '[{"1" : "richk"}, {"2" : "richk"}]',
            '[{"1" : "richk"}, {"2" : "richk"}, {"3" : "richk"}]'
        ]
        self.assertEqual(get_user_data('richkempinski'),
                         {'Mocks': 10,
                          'Project1': 2,
                          'hellogitworld': 30,
                          'helloworld': 6,
                          'threads-of-life': 1})

"""
    def test_get_data_user(self):
        check = {
            'hellogitworld': 2,
            'helloworld': 2,
            'Mocks': 2,
            'Project1': 2,
            'threads-of-life': 2
        }
        self.assertEqual(get_data_user('richkempinski'), check)
"""

if __name__ == '__main__':
    print('Running HW_04A_test_pshiyani.py testing suite.')
    unittest.main(exit = False, verbosity=2)





    
