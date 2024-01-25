import psutil
import socket
import requests

class SystemMonitor:
    def __init__(self):
        pass

    def check_disk_usage(self):
        disk_usage = psutil.disk_usage('/')
        return disk_usage.percent > 20

    def check_cpu_utilization(self):
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < 75

    def check_localhost(self):
        try:
            localhost_status = socket.gethostbyname('localhost')
            return localhost_status == '127.0.0.1'
        except socket.error:
            return False

    def check_internet_access(self):
        try:
            response = requests.get('http://www.google.com', timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

def main():
    monitor = SystemMonitor()

    disk_status = monitor.check_disk_usage()
    cpu_status = monitor.check_cpu_utilization()
    localhost_status = monitor.check_localhost()
    internet_status = monitor.check_internet_access()

    if not (disk_status and cpu_status):
        print("ERROR! Disk usage or CPU usage failed.")
    elif localhost_status and internet_status:
        print("Everything is OK.")
    else:
        print("Network checks failed.")
        if not localhost_status:
            print("Localhost is not operational.")
        if not internet_status:
            print("Internet access is not operational.")

if __name__ == "__main__":
    main()
