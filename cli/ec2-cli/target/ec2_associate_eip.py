import manage_instance
import sys

if __name__ == '__main__':

    print("ec2_associate_eip")

    # 查询未绑定eip的ec2

    # 查询未绑定ec2的eip


    # 绑定之后修改ec2的标签

    if len(sys.argv) == 1:
        print("fail")
    else:
        num = sys.argv[1]
        for i in range(0, int(num)):
            manage_instance.delete_instance("ec2-stack-" + str(i))
