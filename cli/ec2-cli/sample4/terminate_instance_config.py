import manage_instance
import manage_eip

if __name__ == '__main__':

    print("terminate_instance_config")

    file = open("terminate_instance_config_file.txt")

    for instance_id in file.readlines():
        instance_id = instance_id.strip('\n')
        print(instance_id)

        # 修改标签
        tags = [
            {
                'Key': 'EIPStatus',
                'Value': 'off'
            },
        ]

        # 修改ec2标签
        manage_instance.create_tags(tags, instance_id)

        # 修改eip标签
        eip_filters = [
            {
                'Name': 'instance-id',
                'Values': [
                    instance_id,
                ]
            }
        ]
        eips = manage_eip.describe_eips(eip_filters)
        if len(eips) > 0:
            # 解绑ec2和eip
            manage_eip.disassociate_elastic_ip(eips[0])
            # 修改eip标签
            manage_eip.create_tags(tags, eips[0])

        # 释放
        manage_instance.terminate_instance(instance_id)

        print("terminate success: ")
        print(instance_id)

    file.close()

    print("---------------------------------------------")
    print("exec finished !")
