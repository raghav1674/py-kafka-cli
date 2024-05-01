import os
import yaml

def load_profile_from_config(profile,config_file):

    config_file = os.path.expanduser(config_file)

    if not os.path.exists(config_file):
        raise Exception(f"Config file {config_file} not found")

    with open(config_file) as f:
        config = yaml.load(f,Loader=yaml.FullLoader)
    
    if not config:
        raise Exception(f"Config file {config_file} is empty")

    if profile not in config:
        raise Exception(f"Profile {profile} not found in the config file")
    
    return config[profile]

