# Register the flags with the subcommands defined in the flags.py and 
# also specify the function to be called defined in the corresponding
# utils module
from argparse import ArgumentParser
from pkg import flags
from pkg.subcommands import topic
from pkg.subcommands import consumer_group as cg

def topic_subcommands(parser: ArgumentParser):

    subparsers = parser.add_subparsers()
    
    unsed_parser = subparsers.add_parser("list-unused")
    flags.unused_topic_flags(unsed_parser,topic.list_unused)
    
def cg_subcommands(parser: ArgumentParser):

    subparsers = parser.add_subparsers()
    
    list_parser = subparsers.add_parser("list")
    flags.list_cg_flags(list_parser,cg.list)