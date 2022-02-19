import manage_eip
import sys

if __name__ == '__main__':

    print("new eip")

    if len(sys.argv) == 1:
        print("fail")
    else:
        num = sys.argv[1]
        for i in range(0, int(num)):
            manage_eip.allocate_address()

    print("---------------------------------------------")
    print("exec finished !")
