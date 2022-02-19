import manage_instance

if __name__ == '__main__':

    running_instanceIds = manage_instance.describe_running_instances()
    print("running_instanceIds: ")
    print(running_instanceIds)

    for instanceId in running_instanceIds:
        manage_instance.stop_instance(instanceId)
        print("stop success: ")
        print(instanceId)
