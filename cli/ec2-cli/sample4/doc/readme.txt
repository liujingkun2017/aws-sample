一、ec2新开实例，eip，并关联ec2和eip
命令：python3 new_instance_with_eip.py [前缀] [数量]
例如：python3 new_instance_with_eip.py test 10
解释：表示使用test前缀开10个ec2和10个eip，并建立关联关系
注意：每次使用的前缀不能一样

二、ec2新开实例
命令：python3 new_instance.py [前缀] [数量]
例如：python3 new_instance.py test 10
解释：表示使用test前缀开10个ec2
注意：每次使用的前缀不能一样

三、ec2批量关机
命令：python3 stop_instance.py
解释：会查询'正在运行'状态，并带有标签 Name=ec2-from-template 的ec2实例，并调用脚本批量关闭这批ec2实例
注意：ec2需要带有 Name=ec2-from-template 标签

四、ec2批量开机
命令：python3 start_instance.py
解释：会查询'已停止'状态，并带有标签 Name=ec2-from-template 的ec2实例，并调用脚本批量开启这批ec2实例
注意：ec2需要带有 Name=ec2-from-template 标签

五、自动关联ec2和eip
命令：python3 ec2_associate_eip.py
解释：查询带有标签 EIPStatus=off 的ec2实例，并同时查询带有标签 EIPStatus=off 的eip，将ec2和eip进行自动关联
注意：ec2需要带有 EIPStatus=off 标签，eip需要带有 EIPStatus=off 标签

六、ec2批量释放
命令：python3 terminate_instance.py
解释：查询带有标签 Name=ec2-from-template 的ec2实例，并调用脚本批量释放这批ec2实例
注意：ec2需要带有 Name=ec2-from-template 标签

七、ec2批量释放（使用配置文件）
命令：python3 terminate_instance_config.py
解释：解析terminate_instance_config_file.txt里面包含的ec2的实例id（例如：i-0dfdfcdeb498112e5），解析每个ec2实例id，并释放ec2实例
注意：terminate_instance_config_file.txt里面格式要正确，不能有空格或者空行

八、eip批量创建
命令：python3 new_eip.py [数量]
例如：python3 new_eip.py 5
解释：批量创建5个eip，并且带有 EIPStatus=off 标签

九、eip批量释放
命令：python3 release_eip.py
解释：删除没有和ec2关联，带有 EIPStatus=off 标签的eip


注意：所有的命令执行完成后，会输出：exec finished !，命令执行完成后，ec2或者eip可能还在处理中




