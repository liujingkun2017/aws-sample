import manage_instance

if __name__ == '__main__':

    print("terminate_instance")

    filters = [
        {
            'Name': 'tag:Name',
            'Values': [
                'ec2-from-template',
            ]
        },
    ]

    terminate_instance_ids = manage_instance.describe_instances(filters)
    print("terminate_instance_ids: ")
    print(terminate_instance_ids)

    for instance_id in terminate_instance_ids:
        manage_instance.terminate_instance(instance_id)
        print("terminate success: ")
        print(instance_id)

    print("---------------------------------------------")
    print("exec finished !")
