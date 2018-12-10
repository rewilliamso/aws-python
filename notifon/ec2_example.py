import boto3
session = boto3.Session(profile_name='pythonAutomation")
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
img=ec2.Image('ami-0cd3dfa4e37921605')
img.name
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-0cd3dfa4e37921605')
img_apse2.name
img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20181129-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
img
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst=instances[0]
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.public_ip_address

sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])

sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '199.134.170.146/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80 , 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
