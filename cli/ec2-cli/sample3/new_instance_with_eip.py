import manage_instance
import sys

if __name__ == '__main__':

    print("new stack")

    if len(sys.argv) == 1:
        print("fail")
    else:
        num = sys.argv[1]
        for i in range(0, int(num)):
            manage_instance.new_instance_with_eip("ec2-stack-" + str(i))
