一、开ec2实例，eip，并关联ec2和eip
命令：python3 new_instance_with_eip.py [前缀] [数量]
例如：python3 new_instance_with_eip.py test 10
解释：表示使用test前缀开10个ec2和10个eip，并建立关联关系
注意：每次使用的前缀不能一样

二、开ec2实例
命令：python3 new_instance.py [前缀] [数量]
例如：python3 new_instance.py test 10
解释：表示使用test前缀开10个ec2
注意：每次使用的前缀不能一样

三、批量关机
命令：python3 stop_instance.py
解释：会查询'正在运行'状态，并带有标签 Name=ec2-from-template 的ec2实例，并调用脚本批量关闭这批ec2实例
注意：ec2需要带有 Name=ec2-from-template 标签

四、批量开机
命令：python3 start_instance.py
解释：会查询'已停止'状态，并带有标签 Name=ec2-from-template 的ec2实例，并调用脚本批量开启这批ec2实例
注意：ec2需要带有 Name=ec2-from-template 标签

五、自动关联ec2和eip
命令：python3 ec2_associate_eip.py
解释：查询带有标签 EIPStatus=off 的ec2实例，并同时查询带有标签 EIPStatus=off 的eip，将ec2和eip进行自动关联
注意：ec2需要带有 EIPStatus=off 标签，eip需要带有 EIPStatus=off 标签




