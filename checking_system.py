import shutil
import psutil
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free_space = du.free * 100 / du.total
    return free_space < 50
def check_cpu_usage():
    cu = psutil.cpu_percent(1)
    return cu < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("Error")
else:
    print("Everything is fine!!")
