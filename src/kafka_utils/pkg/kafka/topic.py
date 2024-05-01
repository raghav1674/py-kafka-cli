from confluent_kafka import TopicCollection

class TopicManager:

    def __init__(self,client):
        self.client = client

    def list_topics(self):
        return list(self.client.list_topics().topics.keys())

    def describe_topics(self,topics):
        topic_list = []
        futureMap = self.client.describe_topics(TopicCollection(topic_names=topics), request_timeout=10)
        for _, future in futureMap.items():
            topic_list.append(future.result())
        return topic_list