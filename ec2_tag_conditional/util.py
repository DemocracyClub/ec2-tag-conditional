import sys
from collections import defaultdict

from boto import ec2
from boto.utils import get_instance_metadata


class InstanceTags(defaultdict):
    def __init__(self):
        self.metadata = get_instance_metadata(timeout=0.5, num_retries=1)
        tags = self._get_tags()
        for tag in tags:
            self[tag.name] = tag.value


    @property
    def _is_on_ec2(self):
        if self.metadata.keys():
            return True
        else:
            return False

    def _get_tags(self):
        if not self._is_on_ec2:
            raise ValueError('Not on an EC2 instance')
        region = self.metadata['placement']['availability-zone'][:-1]
        instance_id = self.metadata['instance-id']

        conn = ec2.connect_to_region(region)
        return conn.get_all_tags(filters={'resource-id': instance_id})


def command_line():
    tags = InstanceTags()
    print(sys.argv)
    assert len(sys.argv) == 2, "Exactly one argument required"
    name, value = sys.argv[-1].split('=')
    name = name.strip()
    value = value.strip()
    if tags.get(name) and tags[name] == value:
        sys.exit(0)
    sys.exit(1)
