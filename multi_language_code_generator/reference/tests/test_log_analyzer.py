import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_1_valid_200(self):
        line = '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" 200 2326'
        self.assertEqual(self.analyzer.parse_line(line)["status"], 200)

    def test_2_valid_404(self):
        line = '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" 404 2326'
        self.assertEqual(self.analyzer.parse_line(line)["status"], 404)

    def test_3_valid_500(self):
        line = '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" 500 2326'
        self.assertEqual(self.analyzer.parse_line(line)["status"], 500)

    def test_4_analyze_empty(self):
        res = self.analyzer.analyze([])
        self.assertEqual(res["total_requests"], 0)

    def test_5_analyze_single_success(self):
        lines = ['127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" 200 2326']
        res = self.analyzer.analyze(lines)
        self.assertEqual(res["total_requests"], 1)
        self.assertEqual(res["error_rate"], 0.0)

    def test_6_analyze_single_error(self):
        lines = ['127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" 404 2326']
        res = self.analyzer.analyze(lines)
        self.assertEqual(res["total_requests"], 1)
        self.assertEqual(res["error_rate"], 100.0)

    def test_7_analyze_mixed(self):
        lines = [
            '1.1.1.1 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" 200 123',
            '1.1.1.2 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" 500 123'
        ]
        res = self.analyzer.analyze(lines)
        self.assertEqual(res["total_requests"], 2)
        self.assertEqual(res["error_rate"], 50.0)

    def test_8_malformed_line(self):
        self.assertEqual(self.analyzer.parse_line("bad_log_entry")["status"], 200)

    def test_9_analyze_many_success(self):
        lines = ['1.1.1.1 - - [date] "GET / HTTP/1.0" 200 123'] * 10
        res = self.analyzer.analyze(lines)
        self.assertEqual(res["total_requests"], 10)
        self.assertEqual(res["error_rate"], 0.0)

    def test_10_analyze_all_errors(self):
        lines = ['1.1.1.1 - - [date] "GET / HTTP/1.0" 502 123'] * 5
        res = self.analyzer.analyze(lines)
        self.assertEqual(res["total_requests"], 5)
        self.assertEqual(res["error_rate"], 100.0)

if __name__ == "__main__":
    unittest.main()
