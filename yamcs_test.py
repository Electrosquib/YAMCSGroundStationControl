from yamcs.client import YamcsClient
client = YamcsClient('localhost:8090')

instance = 'myproject'

mdb = client.get_mdb(instance=instance)
archive = client.get_archive(instance=instance)
processor = client.get_processor(instance=instance, processor='realtime')
# inst = client.create_instance("Ground Station")

print(list(client.list_instance_templates()))

# client.create_instance(
#     name="my-instance",
#     template="myproject"
# )