from pylib.os_search import os_info
from pylib.cpu_search import cpu_info
from pylib.ram_search import ram_info
from pylib.lan_search import lan_info
from pylib.hdd_search import hdd_info
import argparse

parser = argparse.ArgumentParser(description='''범용 컴퓨터 사양 확인 프로그램 입니다.''')
parser.add_argument('--os', action='store_true', help='show os info')
parser.add_argument('--cpu', action='store_true', help='show cpu info')
parser.add_argument('--ram', action='store_true', help='show ram info')
parser.add_argument('--lan', action='store_true', help='show lan info')
parser.add_argument('--hdd', action='store_true', help='show hdd info')

args = parser.parse_args()

def run_search():
    if args.os :
        os_info()
    elif args.cpu :
        cpu_info()
    elif args.ram :
        ram_info()
    elif args.lan :
        lan_info()
    elif args.hdd :
        hdd_info()
    else :
        os_info()
        cpu_info()
        ram_info()
        lan_info()
        hdd_info()

def main() :
    run_search()


if __name__ == '__main__' :
    main()