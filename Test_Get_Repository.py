import unittest
import Get_Repository

class Test_Get_Repository(unittest.TestCase):
    def test_get_repository(self):

        # Correct input
        expected_result = ['User : PreethikaL' ,
                          'HW-01-Testing-triangle-classification Number of commits: 1' ,
                          'HW04 Number of commits: 6' ,
                          'HWK04a Number of commits: 1' ,
                          'plakshmi Number of commits: 3' ,
                          'Triangle_Test Number of commits: 7']
        actual_result = Get_Repository.get_repo_details('PreethikaL')
        self.assertEqual(actual_result, expected_result)

    #     Bad input
        self.assertEqual(Get_Repository.get_repo_details('123abc'), 'unable to fetch repository details from user')
    #  Empty input
        self.assertEqual(Get_Repository.get_repo_details(''), 'unable to fetch repository details from user')

    if __name__ == 'main':

        unittest.main()
