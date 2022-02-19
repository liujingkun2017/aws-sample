import manage_instance
import sys

if __name__ == '__main__':

    print("delete instance")

    if len(sys.argv) == 1:
        print("fail")
    else:
        num = sys.argv[1]
        for i in range(0, int(num)):
            manage_instance.delete_instance("ec2-stack-" + str(i))
