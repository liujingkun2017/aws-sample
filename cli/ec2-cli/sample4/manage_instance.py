import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
ec2 = boto3.resource('ec2')
cf = boto3.client('cloudformation')


def new_instance_with_eip(stack_name):
    'new instance with eip'

    template_data = _parse_template("ec2-with-eip.yaml")
    params = {
        'StackName': stack_name,
        'TemplateBody': template_data,
    }
    stack_result = cf.create_stack(**params)

def new_instance(stack_name):
    'new instance'

    template_data = _parse_template("ec2.yaml")
    params = {
        'StackName': stack_name,
        'TemplateBody': template_data,
    }
    stack_result = cf.create_stack(**params)


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


def terminate_instance(instance_id):
    """
    Terminates an instance. The request returns immediately. To wait for the
    instance to terminate, use Instance.wait_until_terminated().

    :param instance_id: The ID of the instance to terminate.
    """
    try:
        ec2.Instance(instance_id).terminate()
        logger.info("Terminating instance %s.", instance_id)
    except ClientError:
        logging.exception("Couldn't terminate instance %s.", instance_id)
        raise


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


def create_tags(tags, instance_id):
    try:
        ec2_client = boto3.client('ec2')
        ec2_client.create_tags(
            Resources=[
                instance_id,
            ],
            Tags=tags)

    except ClientError:
        logger.exception("Couldn't create_tags tags %s instance_id %s.", tags, instance_id)
        raise


def describe_instances(filters):
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_instances(Filters=filters)

        reservations = response["Reservations"]
        instance_ids = []
        for reservation in reservations:
            instances = reservation["Instances"]
            for instance in instances:
                instance_ids.append(instance["InstanceId"])


    except ClientError:
        logger.exception("Couldn't describe instance %s.")
        raise
    else:
        return instance_ids
