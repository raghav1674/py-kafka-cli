from pkg.kafka.consumer_group import ConsumerGroupManager


def list(args,client):

    cg_manager = ConsumerGroupManager(client)

    group_ids = cg_manager.list_consumer_groups()

    if len(group_ids) == 0:
        print("No consumer groups found")
    else:
        print(group_ids)
