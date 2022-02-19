import manage_instance

if __name__ == '__main__':

    stop_instanceIds = manage_instance.describe_stop_instances()
    print("stop_instanceIds: ")
    print(stop_instanceIds)

    for instanceId in stop_instanceIds:
        manage_instance.start_instance(instanceId)
        print("start success: ")
        print(instanceId)
