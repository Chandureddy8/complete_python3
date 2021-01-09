import unittest
from unittest.mock import patch
from web_request import WebRequest

class WebRequestTest(unittest.TestCase):
    @patch('web_request.urlopen')
    def test_execute_with_success_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 200
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "SUCCESS")

    @patch('web_request.urlopen')
    def test_execute_with_failure_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 404
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "FAILURE")

if __name__ == "__main__":
    unittest.main()