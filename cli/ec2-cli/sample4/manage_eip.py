import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
ec2 = boto3.resource('ec2')


def allocate_address():
    ec2_client = boto3.client('ec2')
    allocation = ec2_client.allocate_address(
        Domain='vpc',
        TagSpecifications=[
            {
                'ResourceType': 'elastic-ip',
                'Tags': [
                    {
                        'Key': 'EIPStatus',
                        'Value': 'off'
                    },
                ]
            },
        ]
    )


def release_address():
    unbond_eip_ids = describe_unbond_eip()

    ec2_client = boto3.client('ec2')
    for unbond_eip_id in unbond_eip_ids:
        ec2_client.release_address(
            AllocationId=unbond_eip_id
        )


def associate_elastic_ip(allocation_id, instance_id):
    """
    Associates an Elastic IP address with an instance. When this association is
    created, the Elastic IP's public IP address is immediately used as the public
    IP address of the associated instance.

    :param allocation_id: The allocation ID assigned to the Elastic IP when it was
                          created.
    :param instance_id: The ID of the instance to associate with the Elastic IP.
    :return: The Elastic IP object.
    """
    try:
        elastic_ip = ec2.VpcAddress(allocation_id)
        elastic_ip.associate(InstanceId=instance_id)
        logger.info("Associated Elastic IP %s with instance %s, got association ID %s",
                    elastic_ip.public_ip, instance_id, elastic_ip.association_id)
    except ClientError:
        logger.exception(
            "Couldn't associate Elastic IP %s with instance %s.",
            allocation_id, instance_id)
        raise
    return elastic_ip


def disassociate_elastic_ip(allocation_id):
    """
    Removes an association between an Elastic IP address and an instance. When the
    association is removed, the instance is assigned a new public IP address.

    :param allocation_id: The allocation ID assigned to the Elastic IP address when
                          it was created.
    """
    try:
        elastic_ip = ec2.VpcAddress(allocation_id)
        elastic_ip.association.delete()
        logger.info(
            "Disassociated Elastic IP %s from its instance.", elastic_ip.public_ip)
    except ClientError:
        logger.exception(
            "Couldn't disassociate Elastic IP %s from its instance.", allocation_id)
        raise


def create_tags(tags, allocationId):
    try:
        ec2_client = boto3.client('ec2')
        ec2_client.create_tags(
            Resources=[
                allocationId,
            ],
            Tags=tags)

    except ClientError:
        logger.exception("Couldn't create_tags tags %s allocationId %s.", tags, allocationId)
        raise


def describe_unbond_eip():
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:EIPStatus',
                    'Values': ['off']
                }
            ]
        )

        addresses = response["Addresses"]
        unbond_eip_ids = []
        for address in addresses:
            unbond_eip_ids.append(address["AllocationId"])

    except ClientError:
        logger.exception("Couldn't describe eip %s.")
        raise
    else:
        return unbond_eip_ids


def describe_eips(filters):
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_addresses(
            Filters=filters
        )

        addresses = response["Addresses"]
        unbond_eip_ids = []
        for address in addresses:
            unbond_eip_ids.append(address["AllocationId"])

    except ClientError:
        logger.exception("Couldn't describe eip %s.")
        raise
    else:
        return unbond_eip_ids
