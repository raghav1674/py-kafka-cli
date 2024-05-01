# Add the flags to the subcommands
def unused_topic_flags(parser,init_func):
    parser.set_defaults(func=init_func)

def list_cg_flags(parser,init_func):
    parser.set_defaults(func=init_func)
