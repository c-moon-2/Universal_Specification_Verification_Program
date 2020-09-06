import psutil
import math

def ram_info():
    print ("--------- RAM INFO ------------------------------------------------------------------")
    print("RAM 총 용량                       : ", math.ceil(psutil.virtual_memory().total/(1024.0 **3)), "GB") 
    print()