import psutil
import math

def hdd_info():    
    # 하드디스크
    print ("--------- HDD INFO ------------------------------------------------------------------")
    hardInfo=psutil.disk_partitions()
    for hard in hardInfo :
        print("하드디스크 이름                   : ", hard.mountpoint)
        print (" - 하드디스크 용량(남은 량/총 량) : ", math.floor(psutil.disk_usage(hard.mountpoint).free/(1024.0 **3)),"/", math.ceil(psutil.disk_usage(hard.mountpoint).total/(1024.0 **3)), "GB")
        print()
    print()