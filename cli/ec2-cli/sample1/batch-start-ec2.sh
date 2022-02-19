# 列出停止状态的实例
stop_instances=`aws ec2 describe-instances  --filters Name=instance-state-code,Values=80 --query 'Reservations[*].Instances[*].[InstanceId]' --output text`

# 启动每一个停止状态的实例
for line in $stop_instances
do
  echo  $line;
  aws ec2 start-instances --instance-ids "$line"
done

