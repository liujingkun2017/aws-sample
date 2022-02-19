import manage_instance

if __name__ == '__main__':
    # running_instanceIds = manage_instance.describe_running_instances()
    # print("running_instanceIds: ")
    # print(running_instanceIds)
    #
    # stop_instanceIds = manage_instance.describe_stop_instances()
    # print("stop_instanceIds: ")
    # print(stop_instanceIds)

    # manage_instance.delete_instance("myteststack1")
    manage_instance.new_instance("myteststack000")

