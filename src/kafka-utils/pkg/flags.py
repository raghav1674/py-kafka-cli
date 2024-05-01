# Add the flags to the subcommands
def describe_topic_flags(parser,init_func):
    parser.add_argument("--name",help="Name of the topic")
    parser.set_defaults(func=init_func)

def unused_topic_flags(parser,init_func):
    parser.set_defaults(func=init_func)

