import requests
import json
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        print("start")
        pass
    def tearDown(self):
        print("end")
        pass

class test_shanghai_get(MyTest):

    def test_shanghai_get(self):
        self.url = "http://192.168.0.186:6008/saferycom/login.do"
        self.headers = {"Content-Type":"application/json"}
        self.data ={
            "token": "abcdefg",
            "id": 1,
            "param": {
                "QuId": 14
            }
        }
        r = requests.post(url=self.url,json=self.data,headers=self.headers)
        print(r.text)
        print(r.status_code)
        self.assertIn("true",r.text)


if __name__ == '__main__':
    unittest.main()

