import manage_instance

if __name__ == '__main__':

    print("stop instance")

    filters = [
        {
            'Name': 'instance-state-code',
            'Values': [
                '16',
            ]
        },
        {
            'Name': 'tag:Name',
            'Values': [
                'ec2-from-template',
            ]
        },
    ]

    running_instance_ids = manage_instance.describe_instances(filters)
    print("running_instance_ids: ")
    print(running_instance_ids)

    for instance_id in running_instance_ids:
        manage_instance.stop_instance(instance_id)
        print("stop success: ")
        print(instance_id)

    print("---------------------------------------------")
    print("exec finished !")
