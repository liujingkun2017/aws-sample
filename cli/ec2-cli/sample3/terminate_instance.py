import manage_instance
import sys

if __name__ == '__main__':

    print("terminate_instance")

    # 从文件里面读取要释放的机器id
    instanceIds = [""]

    # 释放ec2
    manage_instance.terminate_instance("")
