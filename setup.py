from setuptools import setup, find_packages
import os 



setup(
    name = 'kafka-utils',
    version = "0.0.1",
    description = 'Cli for interacting with kafka',
    packages = find_packages("src"),
    package_dir = {
        "kafka_utils": os.path.join("src", "kafka_utils"),
    },
    install_requires = [
    "confluent-kafka==2.3.0",
    "PyYAML==6.0.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    entry_points = {'console_scripts': ['kafka-utils=kafka_utils.main:main'],}
)