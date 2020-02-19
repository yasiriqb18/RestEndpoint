import unittest
import total
"""
Flask requires app to be imported and then send in the test case. 
to do so you can instantiate the test client and then route the application to it
and make requests for the testing.

 
"""

class testcase(unittest.TestCase):



    def setUp(self):# all the test client instatiation is done in the setip method.

        total.app.testing = True

        self.app = total.app.test_client ()

    def testsum(self):

        result = self.app.get('/total') #send the request to the path.

        #add assetion on the assumtion that app is receiving request and responding to it.

        self.assertEqual(result.status_code, 200)

