class ConsumerGroupManager:

    def __init__(self,client):
        self.client = client

    def list_consumer_groups(self):
        group_ids = []
        future = self.client.list_consumer_groups(request_timeout=10)
        list_consumer_groups_result = future.result()
        for consumer_group in list_consumer_groups_result.valid:
            group_ids.append(consumer_group.group_id)
        return group_ids

    def describe_consumer_groups(self,group_ids):
        groups = []
        futureMap = self.client.describe_consumer_groups(group_ids,request_timeout=10)
        for _, future in futureMap.items():
            group = future.result()
            groups.append(group)
        return groups