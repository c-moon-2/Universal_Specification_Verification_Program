import platform
import psutil

def cpu_info():
    # CPU
    print ("--------- CPU INFO ------------------------------------------------------------------")
    print("CPU 정보                          : ", platform.processor())
    print("CPU 아키텍처                      : ", platform.machine())
    print("CPU 코어 수                       : ", psutil.cpu_count(),"개") 
    print()