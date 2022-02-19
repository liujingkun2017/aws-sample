import manage_instance

if __name__ == '__main__':

    print("start instance")

    filters = [
        {
            'Name': 'instance-state-code',
            'Values': [
                '80',
            ]
        },
        {
            'Name': 'tag:Name',
            'Values': [
                'ec2-from-template',
            ]
        },
    ]
    stop_instance_ids = manage_instance.describe_instances(filters)
    print("stop_instance_ids: ")
    print(stop_instance_ids)

    for instance_id in stop_instance_ids:
        manage_instance.start_instance(instance_id)
        print("start success: ")
        print(instance_id)

    print("---------------------------------------------")
    print("exec finished !")
