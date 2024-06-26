# Register the flags with the subcommands defined in the flags.py and 
# also specify the function to be called defined in the corresponding
# utils module
from argparse import ArgumentParser
from kafka_utils.pkg import flags
from kafka_utils.pkg.subcommands import topic

def topic_subcommands(parser: ArgumentParser):

    subparsers = parser.add_subparsers()
    
    unsed_parser = subparsers.add_parser("list-unused")
    flags.unused_topic_flags(unsed_parser,topic.list_unused)


