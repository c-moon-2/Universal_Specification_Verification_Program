import psutil

def lan_info():
    # LAN
    print ("--------- LAN INFO ------------------------------------------------------------------")
    lanInfo=psutil.net_if_addrs()
    for card_name in lanInfo:
        print("LAN 이름                          : ", card_name)
        print(" - IP 주소                        : ", lanInfo[card_name][1].address)
        print()
    print()        