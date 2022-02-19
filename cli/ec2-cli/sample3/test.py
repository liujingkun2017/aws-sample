import manage_eip

if __name__ == '__main__':

    print("start-----")
    unbond_eip_ids = manage_eip.describe_unbond_eip()
    print(unbond_eip_ids)

