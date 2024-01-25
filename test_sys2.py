# test_system_monitor.py
import unittest
from unittest.mock import patch
from sys2 import SystemMonitor # assuming system_monitor.py is in the same directory

class TestSystemMonitor(unittest.TestCase):
    @patch('psutil.disk_usage')
    def test_check_disk_usage(self, mock_disk_usage)
        mock_disk_usage.return_value.percent = 25
        monitor = SystemMonitor()
        self.assertTrue(monitor.check_disk_usage())

    @patch('psutil.cpu_percent')
    def test_check_cpu_utilization(self, mock_cpu_percent)
        mock_cpu_percent.return_value = 50
        monitor = SystemMonitor()
        self.assertFalse(monitor.check_cpu_utilization())

    @patch('socket.gethostbyname')
    def test_check_localhost(self, mock_gethostbyname)
        mock_gethostbyname.return_value = '127.0.0.1'
        monitor = SystemMonitor()
        self.assertTrue(monitor.check_localhost())

    @patch('requests.get')
    def test_check_internet_access(self, mock_get)
        mock_get.return_value.status_code = 200
        monitor = SystemMonitor()
        self.assertTrue(monitor.check_internet_access())

if __name__ == '__main__'
    unittest.main()
