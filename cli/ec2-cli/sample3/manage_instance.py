import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
ec2 = boto3.resource('ec2')
cf = boto3.client('cloudformation')


def new_instance(stack_name):
    'new instance'

    template_data = _parse_template("ec2-with-eip.yaml")
    params = {
        'StackName': stack_name,
        'TemplateBody': template_data,
    }
    stack_result = cf.create_stack(**params)
    print(stack_result)


def _parse_template(template):
    with open(template) as template_fileobj:
        template_data = template_fileobj.read()
    cf.validate_template(TemplateBody=template_data)
    return template_data


def delete_instance(stack_name):
    'delete instance'
    cf.delete_stack(StackName=stack_name)


def start_instance(instance_id):
    """
    Starts an instance. The request returns immediately. To wait for the instance
    to start, use the Instance.wait_until_running() function.

    :param instance_id: The ID of the instance to start.
    :return: The response to the start request. This includes both the previous and
             current state of the instance.
    """
    try:
        response = ec2.Instance(instance_id).start()
        logger.info("Started instance %s.", instance_id)
    except ClientError:
        logger.exception("Couldn't start instance %s.", instance_id)
        raise
    else:
        return response


def stop_instance(instance_id):
    """
    Stops an instance. The request returns immediately. To wait for the instance
    to stop, use the Instance.wait_until_stopped() function.

    :param instance_id: The ID of the instance to stop.
    :return: The response to the stop request. This includes both the previous and
             current state of the instance.
    """
    try:
        response = ec2.Instance(instance_id).stop()
        logger.info("Stopped instance %s.", instance_id)
    except ClientError:
        logger.exception("Couldn't stop instance %s.", instance_id)
        raise
    else:
        return response


def describe_running_instances():
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_instances(Filters=[
            {
                'Name': 'instance-state-code',
                'Values': [
                    '16',
                ]
            },
            {
                'Name': 'tag-value',
                'Values': [
                    'ec2-from-template',
                ]
            },
        ])

        reservations = response["Reservations"]
        instanceIds = []
        for reservation in reservations:
            instanceIds.append(reservation["Instances"][0]["InstanceId"])

    except ClientError:
        logger.exception("Couldn't describe instance %s.")
        raise
    else:
        return instanceIds


def describe_stop_instances():
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_instances(Filters=[
            {
                'Name': 'instance-state-code',
                'Values': [
                    '80',
                ]
            },
            {
                'Name': 'tag-value',
                'Values': [
                    'ec2-from-template',
                ]
            },
        ])

        reservations = response["Reservations"]
        instanceIds = []
        for reservation in reservations:
            instanceIds.append(reservation["Instances"][0]["InstanceId"])

    except ClientError:
        logger.exception("Couldn't describe instance %s.")
        raise
    else:
        return instanceIds
