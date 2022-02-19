import manage_eip
import manage_instance
import sys

if __name__ == '__main__':
    print("ec2_associate_eip")

    # 查询未绑定ec2的eip
    eips = manage_eip.describe_unbond_eip()
    print(eips)
    if len(eips) == 0:
        sys.exit()

    # 查询未绑定eip运行中　的ec2
    unbond_ec2_filters = [
        {
            'Name': 'instance-state-code',
            'Values': [
                '16',
            ]
        },
        {
            'Name': 'tag:EIPStatus',
            'Values': ['off']
        },
    ]
    instance_ids = manage_instance.describe_instances(unbond_ec2_filters)
    print(instance_ids)
    if len(instance_ids) == 0:
        sys.exit()

    # 绑定之后修改ec2的标签
    length = 0
    if len(instance_ids) > len(eips):
        length = len(eips)
    else:
        length = len(instance_ids)

    for i in range(0, int(length)):
        eip_id = eips[i]
        instance_id = instance_ids[i]
        # 绑定
        manage_eip.associate_elastic_ip(eip_id, instance_id)

        tags = [
            {
                'Key': 'EIPStatus',
                'Value': 'on'
            },
        ]
        # 修改ec2标签
        manage_instance.create_tags(tags, instance_id)
        # 修改eip标签
        manage_eip.create_tags(tags, eip_id)

    print("---------------------------------------------")
    print("exec finished !")
