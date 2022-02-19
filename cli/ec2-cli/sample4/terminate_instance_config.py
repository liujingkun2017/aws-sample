import manage_instance

if __name__ == '__main__':

    print("terminate_instance_config")

    file = open("terminate_instance_config_file.txt")

    for instance_id in file.readlines():
        instance_id = instance_id.strip('\n')
        print(instance_id)
        # 释放ec2
        manage_instance.terminate_instance(instance_id)

    file.close()

    print("---------------------------------------------")
    print("exec finished !")
