# Create top level command and register subcommands defined in subcommand.py
import argparse
import traceback
import os

from confluent_kafka.admin import AdminClient

from pkg import subcommand
from pkg.utils.cli_utils import load_profile_from_config



def init_cli():
    parser = argparse.ArgumentParser("kafka-utils",description="CLI for managing kafka",add_help=True)
    parser.add_argument("--profile",help="Profile to use",default=os.getenv("KAFKA_PROFILE","default"))
    parser.add_argument("--config-file",help="Configuration file",default=os.getenv("KAFKA_CONFIG_FILE","~/.kafka-utils/config.yaml"))
    
    subparsers = parser.add_subparsers()

    topic_parser = subparsers.add_parser("topic",add_help=True)
    subcommand.topic_subcommands(topic_parser)

    cg_parser = subparsers.add_parser("cg",add_help=True)
    subcommand.cg_subcommands(cg_parser)

    args = parser.parse_args()

    # create a kafka client based on a profile, which will be passed to the func
    # load profile from the config
    config = load_profile_from_config(args.profile,args.config_file)
    
    client = AdminClient(config)

    try:
        args.func(args,client=client)
    except AttributeError:
        print(traceback.format_exc())
        parser.print_help()
        parser.exit()
    except Exception:
        print(traceback.format_exc())





