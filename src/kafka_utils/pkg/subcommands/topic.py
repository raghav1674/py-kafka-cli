from kafka_utils.pkg.kafka.topic import TopicManager
from kafka_utils.pkg.kafka.consumer_group import ConsumerGroupManager


def list_unused(args,client):

    topic_manager = TopicManager(client)
    cg_manager = ConsumerGroupManager(client)

    group_ids = cg_manager.list_consumer_groups()
    topics = topic_manager.list_topics()

    all_topics = set(topic.name for topic in topic_manager.describe_topics(topics) if not topic.is_internal)
    used_topics = set()

    for each_group in group_ids:
        group = cg_manager.describe_consumer_groups([each_group])[0]
        for member in group.members:
            if member.assignment:
                for toppar in member.assignment.topic_partitions:
                    used_topics.add(toppar.topic)

    unused_topics = all_topics - used_topics

    if len(unused_topics) == 0:
        print("No unused topics found")
    else:
        print(unused_topics)
